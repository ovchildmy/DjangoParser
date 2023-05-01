from Parser.autoru.AutoruParserBuilder import AutoruParserBuilder


class AutoruParserManager:
    builder = None

    def __init__(self):
        self.builder = AutoruParserBuilder()
        self.builder.create_parser()
        self.builder.set_host('https://auto.ru/')
        self.builder.set_listing('https://auto.ru/-/ajax/desktop/listing/')

    def get_builder(self):
        return self.builder

    def init_builder(self):
        pass

    def get_result(self):
        self.builder.get_result()
