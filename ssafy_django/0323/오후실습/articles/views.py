from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    
    articles = Article.objects.all()
    
    context = {
        'articles' : articles,
    }
    
    return render(request, 'articles/index.html', context)


def create(request):
    
    # POST 요청이면 db에 저장
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        
    # GET 요청이면 생성 양식 보여주기
    else:
        form = ArticleForm()
        
    context = {'form' : form}
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article}
    return render(request,'articles/detail.html',context)


def update(request,pk):
    article = Article.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
        
    context = {
        'form':form,
        'article':article
            }
    return render(request,'articles/update.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')