from src.gui.spotiGUI import *


class GUIController(object):
    def __init__(self, controller):
        self.gui = SpotiGUI(self)
        self.controller = controller
        # Registrierung des WindowClose Event-Handlers
        self.gui.fenster.protocol("WM_DELETE_WINDOW", self.windowCloseEvent)
        self.gui.fenster.mainloop()

    def windowCloseEvent(self):
        """
        Beendet das Mainfenster, wodurch nach einer okcancel Abfrage alle Fenster des Spiels geschlossen werden.
        """
        if messagebox.askokcancel("Exit",
                                  self.controller.getLanguageHandler().getString("error")):
            self.gui.fenster.quit()
            self.gui.fenster.destroy()
            sys.exit(0)