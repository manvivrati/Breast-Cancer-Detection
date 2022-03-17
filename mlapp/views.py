from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def printval(request):
    txt = "<h1 style='color:blue; text-align:center'>" \
          "Welcome to the world! </h1>"
    return HttpResponse(txt)


def index(request):
    return render(request, "index.html", {})
