import telebot

class TelegramBot:
    def __init__(self):
        self._token = '713524902:AAEJCI6OuPYPfwi6XooDpcZW7fhtfj5nktQ'
        self._bot = telebot.TeleBot(self._token)

    def sendMessage(self, msg):
        self._bot.send_message(-335169556, msg)

    def sendDocument(self, docomentPath):
        doc = open(docomentPath, 'rb')
        self._bot.send_document(-335169556, doc)
