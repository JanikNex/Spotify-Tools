import json as js


class ConfigHandler(object):
    def __init__(self, controller):
        self.data = None
        self.controller = controller
        self.refreshData()

    def refreshData(self):
        self.data = None
        try:
            with open('src/json/config.json') as data:
                self.data = js.load(data)
        except:
            print('[DEBUG] FileSystem Error: Could not open JSON File!')

    def getData(self):
        return self.data

    def getParameter(self, param):
        return self.data[param]

    def updateData(self, newData):
        try:
            with open('src/json/config.json') as data:
                data.seek(0)
                js.dump(newData, data)
        except:
            print('[DEBUG] FileSystem Error: Could not open JSON File!')
