# LGRID & EGRID

__version__ = "0.2.6"
__author__ = "Michael E Mulvey"
from tkinter import Button, Entry, Label


def lgrid(self, text, gridcol, gridrow, **args):
    """Label Maker for quick labels in a GUI window.
    Example :
        lgrid(root,'text to enter',0,0,**args)

    Where root is the instance of tkinter ,
    'Text to enter' is just that,
    0,0 is the column and row to place them"""
    lbl = Label(self, text=text)
    lbl.grid(column=gridcol, row=gridrow, **args)


def egrid(self, col, row, *args, **kwarg):
    """Entry Maker for a quick entry in a GUI window.
    Example:
    egrid(root,1,0)
    """
    e1 = Entry(self)
    e1.grid(column=col, row=row)


def bgrid(self, text, col, row, *args, **kwarg):
    """Button Maker for quick entry in a grid"""
    btn1 = Button(self, text=text, command=quit)
    btn1.grid(column=col, row=row)
