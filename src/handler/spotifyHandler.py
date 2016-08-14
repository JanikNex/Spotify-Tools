from src.spotipy.client import *
from src.spotipy.util import *
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
        self.scope = "user-top-read"
        self.spotifyAPIConnector = None

    def tryLogIn(self):
        try:
            jsonHandler = JSONHandler()
            jsonHandler.openNewFile("secret")
            self.token = prompt_for_user_token(jsonHandler.getData()["username"], self.scope,
                                               jsonHandler.getData()["clientID"],
                                               jsonHandler.getData()["clientSecret"])
            del jsonHandler
            if self.token is None:
                return False
            elif self.token is not None:
                self.spotifyAPIConnector = Spotify(self.token, True)
                return True
        except:
            return False

    def cachedTokenAvailable(self):
        jsonHandler = JSONHandler()
        jsonHandler.openNewFile("secret")
        result = needLogIn(jsonHandler.getData()["username"], self.scope,
                                               jsonHandler.getData()["clientID"],
                                               jsonHandler.getData()["clientSecret"])
        if result:
            self.token = getCachedToken(jsonHandler.getData()["username"], self.scope,
                                               jsonHandler.getData()["clientID"],
                                               jsonHandler.getData()["clientSecret"])
        if self.token is not None:
            self.spotifyAPIConnector = Spotify(self.token, True)
        del jsonHandler
        return result

    def logInWithURL(self, url):
        #try:
            jsonHandler = JSONHandler()
            jsonHandler.openNewFile("secret")
            self.token = getTokenFromURL(jsonHandler.getData()["username"], url, self.scope,
                                                   jsonHandler.getData()["clientID"],
                                                   jsonHandler.getData()["clientSecret"])
            del jsonHandler
            self.spotifyAPIConnector = Spotify(self.token, True)
        #except:
        #    pass

    def isConnected(self):
        return isinstance(self.spotifyAPIConnector, Spotify)

    def getSpotifyAPIConnector(self):
        return self.spotifyAPIConnector
