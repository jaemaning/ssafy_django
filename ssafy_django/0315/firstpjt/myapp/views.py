from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "myapp/index.html")


def profile(request):
    
    context = {
        'name' : 'minseok',
        'age' : 25,
    }
    
    return render(request, "myapp/profile.html", context)


def fruits(request):
    
    fruits = ['apple', 'banana', 'melon']
    
    context = {
        "fruits" : fruits
    }
    
    return render(request, "myapp/fruits.html", context)


def templates(request):
    return render(request, "myapp/templates.html")