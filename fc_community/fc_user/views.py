from django.http import HttpResponse
from .models import Fcuser
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm

# Create your views here.
def home(request):
    # user_id = request.session.get('user')
    
    # if user_id: # 로그인을 한 클라이언트
    #     fcuser = Fcuser.objects.get(pk=user_id) # 세션에서 가져온 user_id를 pk로 하여 fcuser 객체 데이터를 꺼내옴
    #     return HttpResponse(fcuser.username)
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/') # path('',home) -> home으로 돌아감

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # is_valid()는 forms.py에서 clean()를 자동으로 호출합니다. 뷰에서 is_valid()를 사용하고 form 클래스에서 clean()를 사용함
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
              # db에 저장되어 있는 username = post로 받아온 username, 즉 db에 데이터가 있으며 fcuser에 할당됨
    #         fcuser = Fcuser.objects.get(username=username)
    #         if check_password(password, fcuser.password):
    #             # 비밀번호가 일치, 로그인 처리를!
    #             # 세션, 리다이렉트
    #             request.session['user'] = fcuser.id # 세션의 user라는 key에 fcuser의 id를 저장
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비밀번호가 틀렸습니다.'

    #     return render(request,'login.html',res_data)

    # 세션.
    # 클라이언트가 서버에 요청을 할때,
    # 서버는 cookie를 생성해서 DB안에 저장을 하고, 클라이언트에게 주는 응답의 header에 cookie를 넣어서 보내준다.
    # 클라이언트는 해당 cookie 정보를 쿠키 저장소에 저장해 놓는다.(사이트별로 따로 관리된다.)

def register(request):
    if request.method == "GET":
        # render 함수 : 쉽게 말해서 화면에 html 파일을 띄우기 위해 사용,
        # 즉 view에서 사용하던 파이썬 변수를 html 템플릿으로 넘길 수 있으며, 세번째 인자는 템플릿에 전달할 데이터를 dictionary로 전달할 수 있음 
        return render(request,'register.html')
    elif request.method == "POST": # 사용자로부터 정보를 입력받았을 때
        username = request.POST.get('username',None) # POST는 Dictionary 형태로 가져옴
        useremail = request.POST.get('useremail',None) # None은 기본값
        password = request.POST.get('password',None)
        re_password=request.POST.get('re-password',None)

        # error 객체 전달
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
                password = make_password(password) # 비밀번호 암호롸를 위한 패키지
            )

            fcuser.save()

        return render(request,'register.html',res_data) # res_data가 html로 전달됨, html에서는 출력되는 부분을 만들어야 함