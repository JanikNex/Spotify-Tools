import src.handler.configHandler
import src.handler.languageHandler
import src.handler.spotifyHandler
from src.gui.controller import *

class SpotifyTools(object):
    def __init__(self):
        self.configHandler = src.handler.configHandler.ConfigHandler(self)
        self.languageHandler = src.handler.languageHandler.LanguageHandler(self)
        self.SpotifyHandler = src.handler.spotifyHandler.SpotifyHandler(self)
        self.gui = GUIController(self)

    def getConfigHander(self):
        return self.configHandler

    def getLanguageHandler(self):
        return self.languageHandler

    def getGUI(self):
        return self.gui

    def getSpotifyHandler(self):
        return self.SpotifyHandler
