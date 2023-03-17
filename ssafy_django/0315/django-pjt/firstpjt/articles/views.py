from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello JM</h1>')

def profile(request):
    return render(request, 'articles/profile.html')

def main(request):
    return render(request, 'articles/main.html')

