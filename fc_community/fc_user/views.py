from django.http import HttpResponse
from .models import Fcuser
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm

# Create your views here.
def home(request):
    user_id = request.session.get('user')
    
    if user_id: # 로그인을 한 클라이언트
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('Home!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # is_valid()는 양식에서 clean()를 자동으로 호출합니다. 뷰에서 is_valid()를 사용하고 양식 클래스에서 clean()를 사용합니다.
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html',{'form':form})


    # if request.method == 'GET':
    #     return render(request,'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username',None)
    #     password = request.POST.get('password',None)

    #     res_data={}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야합니다.'
    #     else:
    #         fcuser = Fcuser.objects.get(username=username)
    #         if check_password(password, fcuser.password):
    #             # 비밀번호가 일치, 로그인 처리를!
    #             # 세션, 리다이렉트
    #             request.session['user'] = fcuser.id # user라는 key에 fcuser의 id를 저장
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비밀번호가 틀렸습니다.'

    #     return render(request,'login.html',res_data)

def register(request):
    if request.method == "GET":
        return render(request,'register.html')
    elif request.method == "POST":
        username = request.POST.get('username',None) # POST는 Dictionary 형태로 가져옴
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password',None)
        re_password=request.POST.get('re-password',None)

        res_data = {}

        if not (username and useremail and password and re_password):
           res_data['error'] = '모든값을 입력해야 합니다.'

        if password != re_password:
            # return HttpResponse("비밀번호가 다릅니다.") # 빈화면에 해당 메세지가 뜸
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser( # Fcuser 객체 생성
                username = username,
                useremail = useremail,
                password = make_password(password) # 함수 암호화
            )

            fcuser.save()

        return render(request,'register.html',res_data) # res_data가 html로 전달됨, html에서는 출력되는 부분을 만들어야 함