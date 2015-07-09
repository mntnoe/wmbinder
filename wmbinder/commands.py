"""Command functions for wmbinder.py."""

import time
import re

from wmbinder import window_types
from wmbinder import workspace

import gi
gi.require_version('Keybinder', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Keybinder
from gi.repository import Wnck


PREV_WS = -1
NEXT_WS = 1

EMPTY_WS = 0
USED_WS = 1


def bind(binding, func, *args, **kwargs):
    """Wrapper for keybinder.bind() allowing kwargs."""

    def run(_, __): func(*args, **kwargs)
    try:
        Keybinder.unbind(binding)
    except:
        pass
    success = Keybinder.bind(binding, run, None)
    if not success:
        print "Error binding '%s'" % binding


def spawn(cmd):
    """Spawn a shell command in background."""
    import os
    from subprocess import Popen

    pid = os.fork()
    if pid == 0:
        os.setsid()
        Popen(cmd, shell=True)
        os._exit(0)


def focus(clazz, title=None, name=None, cmd=None, wnck=False):
    """
    Focus a window matching a class. Cycle between multiple windows matching the class.
    
    @ptype   clazz   str
    @param   clazz   Regular expression to match against the window's class.
    @keyword title   If given, also match the window's title against this regular expression.
    @keyword name    If given, also match the window's name against this regular expression.
    @keyword cmd     Shell command to run if now windows matches.
    @keyword no_wnck Uses xdotool instead of wnck to focus the window.
    """

    screen = Wnck.Screen.get_default()
    screen.force_update()

    windows = _get_windows_sorted(screen)
    windows = filter(window_types.is_focusable_type, windows)

    for w in windows:
        match = re.match(clazz, w.get_class_group().get_res_class()) is not None
        if title is not None:
            match &= re.match(title, w.get_name()) is not None
        if name is not None:
            match &= re.match(name, w.get_class_instance_name()) is not None

        if match:
            workspace.goto_workspace_for_window(w, screen)
            if not wnck:
                spawn('xdotool windowactivate %d' % w.get_xid())
            else:
                w.activate(int(time.time()))
            return

    if cmd is not None:
        spawn(cmd)


def next_window(wnck=False):
    """
    Focus the next window in the stack.
    """
    windows = _get_visible_windows()
    if len(windows) == 0: return
    if not wnck:
        spawn('xdotool windowactivate %d' % windows[0].get_xid())
    else:
        windows[0].activate(int(time.time()))


def prev_window(wnck=False):
    """
    Focus the previous window in the stack.
    """
    windows = _get_visible_windows()
    if len(windows) < 2: return
    if not wnck:
        spawn('xdotool windowactivate %d' % windows[-2].get_xid())
    else:
        windows[-2].activate(int(time.time()))


def close(wnck=False):
    if not wnck:
        # xdotool does not support gracefully closing a window
        spawn('wmctrl -c :ACTIVE:')
    else:
        screen = Wnck.Screen.get_default()
        screen.force_update()
        active = screen.get_active_window()
        active.close(int(time.time()))


def goto_workspace(direction, wsType):
    """
    @param   direction   PREV_WS or NEXT_WS
    @param   wsType      EMPTY_WS or USED_WS
    """
    screen = Wnck.Screen.get_default()
    screen.force_update()

    workspaces     = _build_workspaces(direction, screen)
    window_anchors = _build_window_anchors(screen)

    test = (     (lambda x, xs: x in xs) 
            if   wsType == USED_WS 
            else (lambda x, xs: x not in xs))

    for i in workspaces:
        if test(i, window_anchors):
            workspace.goto_workspace_no(i, screen)
            return


def move_to_workspace(direction, wsType):
    """
    @param   direction   PREV_WS or NEXT_WS
    @param   wsType      EMPTY_WS or USED_WS
    """
    screen = Wnck.Screen.get_default()
    screen.force_update()

    workspaces     = _build_workspaces(direction, screen)
    window_anchors = _build_window_anchors(screen)

    test = (     (lambda x, xs: x in xs) 
            if   wsType == USED_WS 
            else (lambda x, xs: x not in xs))

    w = screen.get_active_window()

    for i in workspaces:
        if test(i, window_anchors):
            workspace.move_to_workspace_no(w, i, screen)
            return


def _build_workspaces(direction, screen):
    wno  = workspace.active_workspace_no(screen)
    cnt  = workspace.get_workspace_count(screen)

    lim1 = cnt if direction > 0 else -1
    lim2 = 0   if direction > 0 else cnt-1

    workspaces = (range(wno+direction, lim1, direction) + 
                  range(lim2, wno+direction, direction))

    return workspaces


def _build_window_anchors(screen):
    ws = screen.get_workspace(0)
    vx = ws.get_viewport_x()
    sw = screen.get_width()
    
    window_anchors = []
    for w in screen.get_windows():
        if window_types.is_focusable_type(w):
            (x, y, w, h) = w.get_geometry()
            center_abs   = x+vx + w/2
            window_anchors.append(center_abs / sw)

    return window_anchors


def _get_windows_sorted(screen):
    active = screen.get_active_window()
    return _sort_active_last(active, screen.get_windows())


def _sort_active_last(active, windows):
    windows1 = []
    windows2 = []
    found_active = False
    for w in windows:

    
        if found_active:
            windows1.append(w)
        else:
            windows2.append(w)

        if w == active:
            found_active = True

    return windows1 + windows2

def _get_visible_windows():
    screen = Wnck.Screen.get_default()
    screen.force_update()
    ws = screen.get_active_workspace()

    windows = _get_windows_sorted(screen)
    windows = filter(window_types.is_focusable_type, windows)
    windows = filter(lambda w: w.is_in_viewport(ws), windows)
    return windows

