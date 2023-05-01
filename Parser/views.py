from django.http import HttpResponse
from Parser.Processor import Processor

def index(request):
    processor = Processor()
    autoru_parser = processor.autoru_parser()
    result = autoru_parser.get_builder().get_result()
    return HttpResponse(result)
