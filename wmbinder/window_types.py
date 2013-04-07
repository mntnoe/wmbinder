
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

WNCK_WINDOW_NORMAL        = Wnck.WindowType.__enum_values__[0]
WNCK_WINDOW_DESKTOP       = Wnck.WindowType.__enum_values__[1]
WNCK_WINDOW_DOCK          = Wnck.WindowType.__enum_values__[2]
WNCK_WINDOW_DIALOG        = Wnck.WindowType.__enum_values__[3]
WNCK_WINDOW_TOOLBAR       = Wnck.WindowType.__enum_values__[4]
WNCK_WINDOW_MENU          = Wnck.WindowType.__enum_values__[5]
WNCK_WINDOW_UTILITY       = Wnck.WindowType.__enum_values__[6]
WNCK_WINDOW_SPLASHSCREEN  = Wnck.WindowType.__enum_values__[7]

FOCUSABLE_TYPES = [
    WNCK_WINDOW_NORMAL,
    WNCK_WINDOW_DIALOG,
    WNCK_WINDOW_UTILITY,
]

def is_focusable_type(w):
    return w.get_window_type() in FOCUSABLE_TYPES
