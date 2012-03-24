
import wnck

WNCK_WINDOW_NORMAL        = wnck.WindowType.__enum_values__[0]
WNCK_WINDOW_DESKTOP       = wnck.WindowType.__enum_values__[1]
WNCK_WINDOW_DOCK          = wnck.WindowType.__enum_values__[2]
WNCK_WINDOW_DIALOG        = wnck.WindowType.__enum_values__[3]
WNCK_WINDOW_TOOLBAR       = wnck.WindowType.__enum_values__[4]
WNCK_WINDOW_MENU          = wnck.WindowType.__enum_values__[5]
WNCK_WINDOW_UTILITY       = wnck.WindowType.__enum_values__[6]
WNCK_WINDOW_SPLASHSCREEN  = wnck.WindowType.__enum_values__[7]

FOCUSABLE_TYPES = [
    WNCK_WINDOW_NORMAL,
    WNCK_WINDOW_DIALOG,
    WNCK_WINDOW_UTILITY,
]

def is_focusable_type(w):
    return w.get_window_type() in FOCUSABLE_TYPES
