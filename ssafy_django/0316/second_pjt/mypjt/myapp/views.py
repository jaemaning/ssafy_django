from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request,'myapp/throw.html')


def catch(request):    
    
    context = {
        'msg' : request.GET.get('message'),
        'key' : request.GET.get('key'),
    }
    
    return render(request, 'myapp/catch.html', context)