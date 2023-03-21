from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    
    articles = Article.objects.all()
    
    context = {
        'articles' : articles
    }
    
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    
    article = Article.objects.get(pk=pk)
    
    context = {
        'article' : article
    }
    
    return render(request, 'articles/detail.html', context)

# 글 생성을 위한 페이지
def new(request):
    return render(request, 'articles/new.html')


# 글 생성후 데이터베이스에 저장하는 view
def create(request):
    
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # DB에 새로운 Article 저장
    # 1번 방법
    # Article.objects.create(title=title,content=content)
    
    # 2번 방법 *** 이 방법이 주로 사용됨
    article = Article(title=title, content=content)
    # ~~~~ DB 저장전에 들어온 자료 처리 로직 -> 유효성 검사 과정이 주로 들어감
    article.save()
    
    return redirect('articles:index')