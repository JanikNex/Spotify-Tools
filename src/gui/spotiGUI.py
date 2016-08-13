from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sys import exit


class SpotiGUI(object):
    def __init__(self, controller):
        self.controller = controller
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
        #except:
        #    # Kommt es beim erstellen des Fensters zu einem Fehler wird das Programm mit einem Fehler geschlossen
        #    messagebox.showerror(self.controller.getLanguageHandler().getString("error"))
        #    self.fenster.quit()
        #    self.fenster.destroy()
        #    sys.exit(0)
