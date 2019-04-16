
import tkinter as tk
import tkinter.font as tk_font
import extra_functions

from startup import *
from signup import *
from signin import *
from mainpage import *
from profile import *


#import database
#import urllib.request, json

class EntryWithPlaceholder():
    def __init__(self, entry, placeholder="PLACEHOLDER"):
        self.entry = entry
        self.placeholder = placeholder
        self.default_fg_color = self.entry['fg']

        self.entry.bind("<FocusIn>", self.foc_in)
        self.entry.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.entry.insert(0, self.placeholder)
        self.entry.config(fg="gray")

    def foc_in(self, *args):
        if self.entry['fg'] == "gray":
            self.entry.delete('0', 'end')
            self.entry['fg'] = self.default_fg_color

    def foc_out(self, *args):
        # print("foc_out")
        if not self.entry.get():
            self.put_placeholder()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Crypto-Portal")
        # self.state("zoomed")
        self.title_font = tk_font.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.padding = ""

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SignIn, SignUp, MainPage, Profile):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
