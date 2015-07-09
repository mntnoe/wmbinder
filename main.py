#!/usr/bin/env python

from os.path import dirname
from sys import argv

import gi
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')
from gi.repository import Gdk
from gi.repository import Gtk
from gi.repository import Keybinder

from wmbinder.commands import *
from wmbinder import util


if __name__ == '__main__':

    util.setup_service(dirname(__file__))

    Gtk.init(argv)
    Keybinder.init()

    bind("<Mod5>z"        , spawn , "xclip -selection primary -o | xclip -selection clipboard -i")
    bind("<Mod5>x"        , spawn , "xterm")
    bind("<Mod5><Shift>x" , spawn , "xterm -name xterm2")
    bind("<Mod5>c"        , focus , "XTerm", name="xterm$", cmd="xterm")
    bind("<Mod5><Shift>c" , focus , "XTerm", name="xterm2", cmd="xterm -name xterm2")
    bind("<Mod5>t"        , focus , "Firefox"   , cmd="firefox")
    bind("<Mod5>r"        , focus , "Google-chrome.*|Chromium-browser", cmd="google-chrome")
    bind("<Mod5>s"        , focus , "Nautilus"  , cmd="nautilus ~")
    bind("<Mod5>v"        , focus , "Gvim"      , cmd="gvim --servername VIM")
    bind("<Mod5>d"        , focus , "Eclipse|jetbrains-idea-ce|jetbrains-webstorm")
    bind("<Mod5>w"        , focus , "com-sun-javaws-Main")
    bind("<Mod5>n"        , next_window)
    bind("<Mod5>e"        , prev_window)
    bind("<Mod5>y"        , goto_workspace, PREV_WS, EMPTY_WS)
    bind("<Mod5>l"        , goto_workspace, PREV_WS, USED_WS)
    bind("<Mod5>u"        , goto_workspace, NEXT_WS, USED_WS)
    bind("<Mod5>j"        , goto_workspace, NEXT_WS, EMPTY_WS)
    bind("<Mod5><Shift>y" , move_to_workspace, PREV_WS, EMPTY_WS)
    bind("<Mod5><Shift>l" , move_to_workspace, PREV_WS, USED_WS)
    bind("<Mod5><Shift>u" , move_to_workspace, NEXT_WS, USED_WS)
    bind("<Mod5><Shift>j" , move_to_workspace, NEXT_WS, EMPTY_WS)
    bind("<Mod5>k"        , close)
    bind("<Mod5>Delete"   , spawn, "gnome-session-quit --power-off")

    try:
        Gtk.main()
    except KeyboardInterrupt:
        pass


