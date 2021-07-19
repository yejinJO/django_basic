from django.contrib.auth.hashers import check_password
from board.models import Board
from django import forms


# Django에서의 form : 폼을 개발하는 것은 복잡한 작업이 될 수도 있다.
# 만약 여러개의 폼을 관리해야 하는 경우 html을 작성해야 하며(id,password, email, address, phonenumber...)
# 데이터의 유효성을 검증하고, 유효하지 않은 입력에 대해서는 사용자가 알수 있도록 에러메시지를 표시해줘야 하며,
# 성공적으로 제출된 데이터를 적절히 처리하고,
# 마지막으로 성공했을 경우 사용자가 알수 있게 응답할 수 있도록 개발해야한다.
# 하지만 django 폼은 폼과 그에 연관된 필드를 정의하여 객체를 만들고,
# 폼 html 코드를 작성하는 작업과 데디터 유효성 검증에 이 객체들을 사용하여,
# 좀 더 효율적으로 코드를 구성할 수 있다.


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={'required' : '제목을 입력해주세요'},
        max_length=128, label="제목")
    contents = forms.CharField(
        error_messages={'required' : '내용을 입력해주세요'},
        widget=forms.Textarea, label="내용") 

   