from src.gui.spotiGUI import *
from src.spotipy.util import *
from src.spotipy.client import *
from src.handler.spotifyHandler import *
from src.util.controller import *
import json as js


class GUIController(object):
    def __init__(self, controller):
        """
        :param controller: SpotifyTools()
        """
        self.gui = SpotiGUI(self, [self.cb_tab1, self.cb_tab2, self.cb_options_login, self.cb_options_next])
        self.controller = controller
        self.GUIchangeLanguage()
        self.mode = 'STARTUP'
        self.GUIupdateMode()
        self.gui.fenster.protocol("WM_DELETE_WINDOW", self.windowCloseEvent)
        self.gui.fenster.mainloop()

    def windowCloseEvent(self):
        if messagebox.askokcancel("Exit",
                                  self.controller.getLanguageHandler().getString("exit")):
            self.gui.fenster.quit()
            self.gui.fenster.destroy()
            sys.exit(0)

    def GUIchangeLanguage(self):
        self.gui.menuButton1.config(text=self.controller.getLanguageHandler().getString("button_dashboard"))
        self.gui.menuButton2.config(text=self.controller.getLanguageHandler().getString("button_options"))
        self.gui.optionButton1.config(text=self.controller.getLanguageHandler().getString("button_options_save"))
        self.gui.optionButton2.config(text=self.controller.getLanguageHandler().getString("button_options_login"))
        self.gui.optionButton3.config(text=self.controller.getLanguageHandler().getString("button_options_reset"))
        self.gui.optionButton4.config(text=self.controller.getLanguageHandler().getString("button_options_next"))


    def GUIupdateMode(self):
        self.hideAll()
        if self.mode == 'STARTUP':
            if self.controller.getSpotifyHandler().cachedTokenAvailable():
                self.setMode('DASHBOARD')
            else:
                self.setMode('OPTIONS')
        elif self.mode == 'OPTIONS':
            self.gui.optionFrame.place(x=0, y=self.gui.height // 12, width=self.gui.width, height=self.gui.height // 12 * 11)
            if not self.controller.getSpotifyHandler().isConnected():
                self.gui.optionButton2.pack(side=LEFT)
            self.gui.optionButton1.pack(side=LEFT)
            self.gui.optionButton3.pack(side=LEFT)
        elif self.mode == 'DASHBOARD':
            self.gui.dashboardFrame.place(x=0, y=self.gui.height // 12, width=self.gui.width, height=self.gui.height // 12 * 11)
            self.gui.dashboardLabel1.pack()
            data = self.controller.getSpotifyHandler().getSpotifyAPIConnector().track("2q5IyYEn00qHegsCZo3sQF")
            print(data)
            show = data['name']+'\n'+data['artists']['name']
            print(show)
            self.gui.dashboardLabel1.config(text=show)

    def setMode(self, mode):
        self.mode = mode
        self.GUIupdateMode()

    def hideAll(self):
        self.gui.optionFrame.place_forget()
        self.gui.dashboardFrame.place_forget()
        self.gui.optionButton1.pack_forget()
        self.gui.optionButton2.pack_forget()
        self.gui.optionButton3.pack_forget()
        self.gui.optionEntry1.pack_forget()
        self.gui.optionButton4.pack_forget()
        
    def cb_options_save(self):
        pass
    
    def cb_options_login(self):
        if not self.controller.getSpotifyHandler().tryLogIn():
            self.gui.optionEntry1.pack(side=LEFT)
            self.gui.optionButton4.pack(side=LEFT)

    def cb_options_next(self):
        if self.gui.optionTextVar1.get() != "":
            self.gui.optionEntry1.pack_forget()
            self.gui.optionButton4.pack_forget()
            self.controller.getSpotifyHandler().logInWithURL(self.gui.optionTextVar1.get())
            self.gui.optionTextVar1.set('')

    def cb_tab1(self):
        self.setMode('DASHBOARD')
        
    def cb_tab2(self):
        self.setMode('OPTIONS')
