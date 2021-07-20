from django.http.response import Http404
from django.core.paginator import Paginator
from fc_user.models import Fcuser
from board.forms import BoardForm
from django.shortcuts import redirect, render
from .models import Board

# Create your views here.

def board_list(request):
    all_boards = Board.objects.all().order_by('-id') 
    # .all()은 모두 가지고 오겠다라는 의미
    # -은 역순으로(최신순으로) 가져오겠다라는 의미
    page = int(request.GET.get('p',1)) # page번호 받아오기, 없으면 첫번째 페이지
    # Paginator(분할될 객체, 한페이지에 담길 객체의 수)
    paginator = Paginator(all_boards,2) # 페이지마다 2개씩 보여주기
    
    boards = paginator.get_page(page)
    return render(request,'board_list.html',{'boards' : boards})

def board_write(request):
    # 예외처리 필요 : 만약 로그인을 하지 않은 상태로 글쓰기 시도시 DoesNotExist Excetpion 발생
    if not request.session.get('user'): # 로그인을 하지 않았다면
        return redirect('/fc_user/login/') # 로그인 페이지로 redirect 처리
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()
    else:
         form = BoardForm()
    return render(request,'board_write.html',{'form' : form})

# pk를 통해서 게시글의 인덱스로 가져오기
# pk는 urls.py에서 설정
def board_detail(request,pk):
     # 예외처리 필요 : 만약 존재하지 않는 index로 접속 시도시 DoesNotExist Excetpion 발생
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')
    return render(request,'board_detail.html',{'board':board})