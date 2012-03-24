"""
Wrapper handling workspaces.

Compiz operates only with one workspace in WNCK terminology, and instead 
changes viewport coordinates when switching "workspaces". This wrapper 
has functions for determining and switching between compiz's workspaces.
"""

import wnck


def active_workspace_no(screen=None):
    if screen is None:
        screen  = wnck.screen_get_default()
        screen.force_update()

    ws = screen.get_active_workspace()
    return ws.get_viewport_x() / screen.get_width()

def goto_workspace_no(n, screen=None):
    if screen is None:
        screen  = wnck.screen_get_default()
        screen.force_update()
    
    ws = screen.get_active_workspace()
    screen.move_viewport(n * screen.get_width(), ws.get_viewport_y())

def goto_workspace_for_window(w, screen=None):
    if screen is None:
        screen  = wnck.screen_get_default()
        screen.force_update()

    active = active_workspace_no(screen)
    ws = get_workspace_for_window(w, screen)

    if (ws != active):
	goto_workspace_no(ws, screen)
    

def get_workspace_for_window(window, screen=None):
    if screen is None:
        screen  = wnck.screen_get_default()
        screen.force_update()
    
    (x, y, w, h) = window.get_geometry()
    ws = screen.get_active_workspace()
    x_abs = (ws.get_viewport_x() + x)
    if x_abs < 0: x_abs = 0
    return x_abs / screen.get_width()
    
