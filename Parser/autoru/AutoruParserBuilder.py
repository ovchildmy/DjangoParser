from Parser.AbstractParser import AbstractParser
import requests

class AutoruParserBuilder(AbstractParser):
    def __init__(self):
        pass

    def create_parser(self):
        return self

    def get_result(self, limit=0):
        """ Возвращает результат поиска по лимиту """
        response = requests.get(self.url)
        if response.ok:
            return response.text
        return 'No response'