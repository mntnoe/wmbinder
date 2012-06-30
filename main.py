#!/usr/bin/env python

import gtk
from os.path import dirname

from wmbinder.commands import *
from wmbinder import util


if __name__ == '__main__':

    util.setup_service(dirname(__file__))

    bind("<Mod5>z"        , spawn , "xclip -selection primary -o | xclip -selection clipboard -i")
    bind("<Mod5>x"        , spawn , "xterm")
    bind("<Mod5>c"        , focus , "XTerm"     , cmd="xterm")
    bind("<Mod5>t"        , focus , "Firefox"   , cmd="firefox")
    bind("<Mod5>s"        , focus , "Nautilus"  , cmd="nautilus ~")
    bind("<Mod5>v"        , focus , "Gvim"      , cmd="gvim --servername VIM")
    bind("<Mod5>d"        , focus , "Eclipse"   , cmd="eclipse_p2p")
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

    try:
        gtk.main()
    except KeyboardInterrupt:
        pass


