"""
Wrapper handling workspaces.

Compiz operates only with one workspace in WNCK terminology, and instead 
changes viewport coordinates when switching "workspaces". This wrapper 
has functions for determining and switching between compiz's workspaces.
"""

import wnck


def active_workspace_no(screen):
    ws = screen.get_active_workspace()
    return ws.get_viewport_x() / screen.get_width()

def get_workspace_count(screen):
    return screen.get_workspace(0).get_width() / screen.get_width()

def goto_workspace_no(n, screen):
    n = max(0, n)
    n = min(n, get_workspace_count(screen) - 1)
    
    ws = screen.get_active_workspace()

    screen.move_viewport(n * screen.get_width(), ws.get_viewport_y())

def goto_workspace_for_window(w, screen):
    active = active_workspace_no(screen)
    ws = get_workspace_for_window(w, screen)

    if (ws != active):
	goto_workspace_no(ws, screen)
    

def get_workspace_for_window(window, screen):
    (x, y, w, h) = window.get_geometry()
    ws = screen.get_active_workspace()
    x_abs = (ws.get_viewport_x() + x)
    if x_abs < 0: x_abs = 0
    return x_abs / screen.get_width()


def move_to_workspace_no(w, n, screen):
    n = max(0, n)
    n = min(n, get_workspace_count(screen) - 1)
    new_x = n * screen.get_width()

    ws = screen.get_active_workspace()
    
    #(x, y, width, height) = w.get_geometry()
    #x += new_x - ws.get_viewport_x()
    #w.set_geometry(wnck.WINDOW_GRAVITY_CURRENT, wnck.WINDOW_CHANGE_X, x, y, width, height)

    w.stick()
    screen.move_viewport(new_x, ws.get_viewport_y())
    w.unstick()

    
