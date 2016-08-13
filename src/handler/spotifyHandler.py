from spotipy import *
from spotipy.util import *
from src.handler.configHandler import *
from src.util.controller import *
from src.handler.jsonHandler import *


class SpotifyHandler(object):
    def __init__(self, controller):
        """
        :param controller: SpotifyTools()
        """
        self.controller = controller
        self.token = None
        self.scope = None

    def tryLogIn(self):
        try:
            jsonHandler = JSONHandler()
            jsonHandler.openNewFile("secret")
            self.token = prompt_for_user_token(jsonHandler.getData()["username"], self.scope,
                                               jsonHandler.getData()["clientID"],
                                               jsonHandler.getData()["clientSecret"])
            del jsonHandler
            return True
        except:
            return False
