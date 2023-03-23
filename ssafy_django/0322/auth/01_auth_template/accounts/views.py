from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        # 로그인 처리
        # 1. 입력 id, pw 확인 체크
        # 2. 세션 생성
        # 3. 쿠키 전송
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 위 3단계를 한방에 해결
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        # 로그인 화면 띄우기
        # django built-in form 을 사용
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')