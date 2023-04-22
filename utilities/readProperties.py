import configparser

config = configparser.RawConfigParser()
config.read('C:/Users/bar-ge/PycharmProjects/pythonProject/gk8/configurations/config.ini')


class ReadConfig:

    @staticmethod
    def getApplicationStartTransactionId():
        url = config.get('common info', 'transactionId')
        return url

    @staticmethod
    def getApplicationBaseURL():
        url = config.get('common info', 'baseURL')
        return url
