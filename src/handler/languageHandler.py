from src.util.controller import *
from src.handler.jsonHandler import *


class LanguageHandler(object):
    def __init__(self, controller):
        """
        :type controller: SpotifyTools
        """
        self.controller = controller
        self.lang = controller.getConfigHander().getParameter("lang")
        jsonHandler = JSONHandler('lang')
        jsonHandler.openNewFile(self.lang)
        self.langData = jsonHandler.getData()
        del jsonHandler


    def getString(self, ident):
        return self.langData[ident]

    def updateLang(self):
        self.lang = self.controller.getConfigHander().getParameter("lang")
        jsonHandler = JSONHandler('lang')
        jsonHandler.openNewFile(self.lang)
        self.langData = jsonHandler.getData()
        del jsonHandler
