class AbstractParser:
    filters = {
        'price': {
            'from': 0,
            'to': 0
        }
    }
    host = ''
    listing = ''
    novelty = 'all'

    def __init__(self):
        pass

    def set_listing(self, url):
        if '' != url:
            self.listing = url

    def set_host(self, url: str):
        if '' != url:
            self.host = url

    def get_filters(self) -> dict:
        return self.filters
