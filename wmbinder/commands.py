"""Command functions for wmbinder.py."""

import time
import wnck
import re

from wmbinder import window_types
from wmbinder import workspace

PREV_WS = 0
NEXT_WS = 1

EMPTY_WS = 0
USED_WS = 1


def bind(binding, func, *args, **kwargs):
    """Wrapper for keybinder.bind() allowing kwargs."""
    import keybinder
    def run(_): func(*args, **kwargs)
    keybinder.bind(binding, run, None)


def spawn(cmd):
    """Spawn a shell command in background."""
    from subprocess import Popen
    Popen(cmd, shell=True)


def focus(clazz, title=None, cmd=None):
    """
    Focus a window matching a class. Cycle between multiple windows matching the class.
    
    @ptype   clazz   str
    @param   clazz   Regular expression to match against the window's class.
    @keyword title   If given, also match the window's title against this regular expression.
    @keyword cmd     Shell command to run if now windows matches.
    """

    screen  = wnck.screen_get_default()
    screen.force_update()

    windows = _get_windows_sorted(screen)
    windows = filter(window_types.is_focusable_type, windows)

    for w in windows:
        match = re.match(clazz, w.get_class_group().get_name())
        if title is not None:
            match &= re.match(title, w.get_name())

        if match:
            workspace.goto_workspace_for_window(w, screen)
            w.activate(int(time.time()))
            return

    if cmd is not None:
        spawn(cmd)


def nextWindow():
    """
    Focus the next window in the stack.
    """
    windows = _get_visible_windows()
    if len(windows) == 0: return
    windows[0].activate(int(time.time()))


def prevWindow():
    """
    Focus the previous window in the stack.
    """
    windows = _get_visible_windows()
    if len(windows) < 2: return
    windows[-2].activate(int(time.time()))


def close():
    screen  = wnck.screen_get_default()
    screen.force_update()
    active  = screen.get_active_window()
    active.close(int(time.time()))


def gotoWorkspace(direction, wsType):
    # TODO
    pass

def _get_windows_sorted(screen=None):
    if screen is None:
        screen  = wnck.screen_get_default()
        screen.force_update()

    active  = screen.get_active_window()
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
    screen = wnck.screen_get_default()
    screen.force_update()
    ws = screen.get_active_workspace()

    windows = _get_windows_sorted(screen=screen)
    windows = filter(window_types.is_focusable_type, windows)
    windows = filter(lambda w: w.is_in_viewport(ws), windows)
    return windows
