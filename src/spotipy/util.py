# shows a user's playlists (need to be authenticated via oauth)

from __future__ import print_function
import os
import subprocess
from . import oauth2
import src.spotipy


def prompt_for_user_token(username, scope=None, client_id=None,
                          client_secret=None, redirect_uri="http://www.google.com"):
    ''' prompts the user to login if necessary and returns
        the user token suitable for use with the spotipy.Spotify
        constructor

        Parameters:

         - username - the Spotify username
         - scope - the desired scope of the request
         - client_id - the client id of your app
         - client_secret - the client secret of your app
         - redirect_uri - the redirect URI of your app

    '''

    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
                                   scope=scope, cache_path=".cache-" + username)

    # try to get a valid token for this user, from the cache,
    # if not in the cache, the create a new (this will send
    # the user to a web page where they can authorize this app)

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        try:
            subprocess.call(["open", auth_url])
        except:
            print("Please navigate here: %s" % auth_url)
    else:
        return token_info

def needLogIn(username, scope=None, client_id=None,
                          client_secret=None, redirect_uri="http://www.google.com"):

    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
                                   scope=scope, cache_path=".cache-" + username)

    # try to get a valid token for this user, from the cache,
    # if not in the cache, the create a new (this will send
    # the user to a web page where they can authorize this app)

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        return False
    else:
        return True


def getTokenFromURL(username, url, scope=None, client_id=None,
                    client_secret=None, redirect_uri="http://www.google.com"):
    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
                                   scope=scope, cache_path=".cache-" + username)

    code = sp_oauth.parse_response_code(url)
    token_info = sp_oauth.get_access_token(code)

    # Auth'ed API request
    if token_info:
        return token_info['access_token']
    else:
        return None

def getCachedToken(username, scope=None, client_id=None,
                          client_secret=None, redirect_uri="http://www.google.com"):

    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
                                   scope=scope, cache_path=".cache-" + username)

    # try to get a valid token for this user, from the cache,
    # if not in the cache, the create a new (this will send
    # the user to a web page where they can authorize this app)

    token_info = sp_oauth.get_cached_token()

    if token_info is not None:
        return token_info