from django.http import HttpResponse

def home(kwargs):
        return HttpResponse('test home')
