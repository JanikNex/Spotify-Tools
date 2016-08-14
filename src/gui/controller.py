from src.gui.spotiGUI import *


class GUIController(object):
    def __init__(self, controller):
        self.gui = SpotiGUI(self, [self.cb_tab1, self.cb_tab2])
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


    def GUIupdateMode(self):
        self.hideAll()
        if self.mode == 'STARTUP':
            if self.controller.getSpotifyHandler().cachedTokenAvailable():
                self.setMode('DASHBOARD')
            else:
                self.setMode('OPTIONS')
        if self.mode == 'OPTIONS':
            self.gui.optionButton1.pack(side=LEFT)
            self.gui.optionButton2.pack(side=LEFT)
            self.gui.optionButton3.pack(side=LEFT)
            self.gui.optionButton4.pack(side=LEFT)
        if self.mode == 'DASHBOARD':
            pass

    def setMode(self, mode):
        self.mode = mode
        self.GUIupdateMode()

    def hideAll(self):
        self.gui.optionButton1.pack_forget()
        self.gui.optionButton2.pack_forget()
        self.gui.optionButton3.pack_forget()
        self.gui.optionButton4.pack_forget()
        
    def cb_options_save(self):
        pass
    
    def cb_options_login(self):
        pass
    
    def cb_tab1(self):
        self.setMode('DASHBOARD')
        
    def cb_tab2(self):
        self.setMode('OPTIONS')
