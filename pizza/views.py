from django.http import HttpResponse
import datetime

def hello(request):
    now = datetime.datetime.now()
    html = f"<html><body><h1>{now}</h1></body></html>"
    return HttpResponse(html)
