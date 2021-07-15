from django.contrib.auth.hashers import check_password
from fc_user.models import Fcuser
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required' : '아이디를 입력해주세요'},
        max_length=32, label="사용자이름")
    password = forms.CharField(
        error_messages={'required' : '비밀번호를 입력해주세요'},
        widget=forms.PasswordInput, label="비밀번호") # PasswordInput : 비밀번호 마스킹 처리

    # 기본적 유효성검사 : 사용자이름과 비밀번호를 입력받았는지 받지않았는지 검사는 해줌
    # 이외의 유효성검사를 만들어야함
    def clean(self): # 유효성 검사를 위해 clean함수 사용
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):
                self.add_error('password','비밀번호를 틀렸습니다.')
            else:
                self.user_id=fcuser.id