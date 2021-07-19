from board.forms import BoardForm
from django.shortcuts import render
from .models import Board

# Create your views here.

def board_list(request):
    boards = Board.objects.all().order_by('-id') 
    # .all()은 모두 가지고 오겠다라는 의미
    # -은 역순으로(최신순으로) 가져오겠다라는 의미
    return render(request,'board_list.html',{'boards' : boards})

def board_write(request):

    
    form = BoardForm()
    return render(request,'board_write.html',{'form' : form})
