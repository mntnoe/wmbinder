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
    bind("<Mod5>n"      , nextWindow)
    bind("<Mod5>e"      , prevWindow)
    bind("<Mod5>y"      , gotoWorkspace, PREV_WS, EMPTY_WS)
    bind("<Mod5>l"      , gotoWorkspace, PREV_WS, USED_WS)
    bind("<Mod5>u"      , gotoWorkspace, NEXT_WS, USED_WS)
    bind("<Mod5>j"      , gotoWorkspace, NEXT_WS, EMPTY_WS)
    bind("<Mod5>k"      , close)

    gtk.main()


