from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>Sommaire Home</h1>')
    return render(request,'summarizer/home.html')

def about(request):
    # return HttpResponse('<h1>Sommaire About Page</h1>')
    return render(request,'summarizer/about.html')

# Create your views here.
