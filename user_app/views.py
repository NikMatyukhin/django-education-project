from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Hello world!</h1><br><h2>Hello world!</h2><br><h3>Hello world!</h3>')

def jsonify(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"data": 1})

def rendering(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', context={'data': 10})
