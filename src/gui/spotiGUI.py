from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sys import exit


class SpotiGUI(object):
    def __init__(self, controller, callback):
        self.controller = controller
        self.callback = callback
        #try:
        self.fenster = Tk()
        self.fenster.title("PyTools for Spotify")
        self.width = 1200
        self.height = 600
        self.fenster.geometry(str(self.width)+'x'+str(self.height))
        # self.fenster.attributes("-topmost", 1)
        self.fenster.resizable(0, 0)
        self.masterFrame = Frame(master=self.fenster)
        self.masterFrame.place(x=0, y=0, width=self.width, height=self.height)
        # Menu
        self.menuFrame = Frame(master=self.masterFrame)
        self.menuFrame.place(x=0, y=0, width=self.width, height=self.height//12)
        self.menuButton1 = Button(master=self.menuFrame, command=self.callback[0])
        self.menuButton1.pack(side=LEFT)
        self.menuButton2 = Button(master=self.menuFrame, command=self.callback[1])
        self.menuButton2.pack(side=LEFT)
        # Optionen
        self.optionFrame = Frame(master=self.masterFrame)
        self.optionButton1 = Button(master=self.optionFrame)
        self.optionButton2 = Button(master=self.optionFrame, command=self.callback[2])
        self.optionButton3 = Button(master=self.optionFrame)
        self.optionButton4 = Button(master=self.optionFrame, command=self.callback[3])
        self.optionTextVar1 = StringVar()
        self.optionEntry1 = Entry(master=self.optionFrame, textvar=self.optionTextVar1)
        # Dashboard
        self.dashboardFrame = Frame(master=self.masterFrame)
        self.dashboardLabel1 = Label(master=self.dashboardFrame)

        #except:
        #    messagebox.showerror(self.controller.getLanguageHandler().getString("error"))
        #    self.fenster.quit()
        #    self.fenster.destroy()
        #    sys.exit(0)
