wmbinder - Window Management Key Bindings
=========================================

Update
------

wmbinder now works with GTK3, meaning that you can use it with
Unity and Gnome Shell.


Description
-----------

wmbinder is a script that makes window management operations
available that many mainstream window managers lack. wmbinder is
configured by editing the python code directly, and coexists with
your favorite window manager.

Enjoy,

Mads Navntoft Noe 
mail@madsnoe.dk


Usage
-----

Download the files and customize main.py as you see fit.

The workspace commands expects the workspaces to be laid out
horizontally. If you want to use these, you can set this under
CCSM's General Options.


Dependencies
------------

- Python GTK bindings via GObject Introspection

- Python Wnck bindings via GObject Introspection

- keybinder-3.0

- xdotool (If you're using Gnome Shell)

These packages are available in the Ubuntu main repository.


Using the AltGr modifier
------------------------

Note that the example bindings in main.py are using the AltGr key
as modifier. In GTK3 this modifier has been masked by default. I
haven't been able to circumvent this masking other than patching
keybinder. If you want to use workspace commands, you can find
a patched fork here: https://github.com/mntnoe/keybinder

The patched version can be installed under Ubuntu 12.04 with the
following commands:

::

    $ sudo apt-get install gnome-common gtk-doc-tools libgtk-3-dev gobject-introspection libgirepository1.0-dev
    $ git clone https://github.com/mntnoe/keybinder.git
    $ cd keybinder
    $ ./autogen --prefix=/usr
    $ make
    $ sudo make install

