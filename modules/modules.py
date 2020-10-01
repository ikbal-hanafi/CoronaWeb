# Covid-19 Information Gathering
# Ditulis oleh Billal
# Versi 0.1
# Bahasa: python3.8

import requests

class DataNull(Exception):
    pass

class Covid:

    def __init__(self):
        self.globalData = []

    @property
    def country(self):
        if len(self.globalData) > 0:
            cname = []
            for dataLocal in self.globalData:
                cname.append(dataLocal["attributes"]["Country_Region"])
            return cname
        else:
            raise DataNull("Data tidak boleh kosong!")

    @property
    def all(self):
        if len(self.globalData) > 0:
            data = []
            for local in self.globalData:
                dataJson = {}
                dataJson["country"] = local["attributes"]["Country_Region"]
                dataJson["confirmed"] = local["attributes"]["Confirmed"]
                dataJson["deaths"] = local["attributes"]["Deaths"]
                dataJson["active"] = local["attributes"]["Active"]
                dataJson["recovered"] = local["attributes"]["Recovered"]
                data.append(dataJson)
            return data
        else:
            raise DataNull("Data tidak boleh kosong!")

    def search(self, country=""):
        if len(self.globalData) > 0:
            data = []
            for local in self.globalData:
                if country.lower() in (local["attributes"]["Country_Region"]).lower():
                    dataJson = {}
                    dataJson["country"] = local["attributes"]["Country_Region"]
                    dataJson["confirmed"] = local["attributes"]["Confirmed"]
                    dataJson["deaths"] = local["attributes"]["Deaths"]
                    dataJson["active"] = local["attributes"]["Active"]
                    dataJson["recovered"] = local["attributes"]["Recovered"]
                    data.append(dataJson)
            return data
        else:
            raise DataNull("Data tidak boleh kosong!")

    def getDeath(self, country=""):
        if len(self.globalData) > 0:
            data = []
            for local in self.globalData:
                if country.lower() in (local["attributes"]["Country_Region"]).lower():
                    dataJson = {}
                    dataJson["country"] = local["attributes"]["Country_Region"]
                    dataJson["deaths"] = local["attributes"]["Deaths"]
                    data.append(dataJson)
            return data
        else:
            raise DataNull("Data tidak boleh kosong!")

    def getActive(self, country=""):
        if len(self.globalData) > 0:
            data = []
            for local in self.globalData:
                if country.lower() in (local["attributes"]["Country_Region"]).lower():
                    dataJson = {}
                    dataJson["country"] = local["attributes"]["Country_Region"]
                    dataJson["active"] = local["attributes"]["Active"]
                    data.append(dataJson)
            return data
        else:
            raise DataNull("Data tidak boleh kosong!")

    def getConfirmed(self, country=""):
        if len(self.globalData) > 0:
            data = []
            for local in self.globalData:
                if country.lower() in (local["attributes"]["Country_Region"]).lower():
                    dataJson = {}
                    dataJson["country"] = local["attributes"]["Country_Region"]
                    dataJson["confirmed"] = local["attributes"]["Confirmed"]
                    data.append(dataJson)
            return data
        else:
            raise DataNull("Data tidak boleh kosong!")

    def getRecov(self, country):
        if len(self.globalData) > 0:
            data = []
            for local in self.globalData:
                if country.lower() in (local["attributes"]["Country_Region"]).lower():
                    dataJson = {}
                    dataJson["country"] = local["attributes"]["Country_Region"]
                    dataJson["recovered"] = local["attributes"]["Recovered"]
                    data.append(dataJson)
            return data
        else:
            raise DataNull("Data tidak boleh kosong!")
        
    def headers(self):
        reqHead = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'api.kawalcorona.com',
            'TE': 'Trailers',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
        }
        return reqHead
        
    def get(self):
        r = requests.get("https://api.kawalcorona.com/", headers=self.headers()).json()
        self.globalData = r
        return r