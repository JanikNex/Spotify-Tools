import json as js

class JSONHandler(object):
    def __init__(self, directory="json"):
        self.filepath = None
        self.data = None
        self.directory = directory

    def openNewFile(self, path):
        self.data = None
        self.filepath = path
        try:
            with open('src/' + str(self.directory) + '/' + str(path) + '.json') as data:
                self.data = js.load(data)
        except:
            print('[DEBUG] FileSystem Error: Could not open JSON File!')

    def getData(self):
        return self.data
