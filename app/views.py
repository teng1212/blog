from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'app/index.html')


def details(request):
    pass