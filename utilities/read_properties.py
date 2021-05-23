import configparser
config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig():
    
    @staticmethod
    def getApplicationURL(self):
        url=config.get('webapp nopcommerce','baseURL')
        return url
    
    @staticmethod
    def getUserEmail(self):
        username=config.get('webapp nopcommerce', 'username')
        return username
    
    @staticmethod
    def getPassword(self):
        password=config.get('webapp nopcommerce', 'password')
        return password