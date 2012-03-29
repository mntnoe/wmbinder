#!/usr/bin/env python

import gtk

from wmbinder.commands import *


if __name__ == '__main__':

    bind("<Mod5>z"      , spawn , "xclip -selection primary -o | xclip -selection clipboard -i")
    bind("<Mod5>x"      , spawn , "xterm")
    bind("<Mod5>t"      , focus , "Firefox", cmd="firefox")
    bind("<Mod5>Return" , focus , "XTerm"  , cmd="xterm")
    bind("<Mod5>s"      , focus , "File Manager"   , cmd="nautilus ~")
    bind("<Mod5>v"      , focus , "Vim"   , cmd="gvim --servername VIM")
    bind("<Mod5>n"      , next_window)
    bind("<Mod5>e"      , prev_window)
    bind("<Mod5>y"      , goto_workspace, PREV_WS, EMPTY_WS)
    bind("<Mod5>l"      , goto_workspace, PREV_WS, USED_WS)
    bind("<Mod5>u"      , goto_workspace, NEXT_WS, USED_WS)
    bind("<Mod5>j"      , goto_workspace, NEXT_WS, EMPTY_WS)
    bind("<Mod5>i"      , move_to_workspace, NEXT_WS, EMPTY_WS)
    bind("<Mod5>k"      , close)

    try:
        gtk.main()
    except KeyboardInterrupt:
        pass



