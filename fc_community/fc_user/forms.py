from django.contrib.auth.hashers import check_password
from fc_user.models import Fcuser
from django import forms


# Django에서의 form : 폼을 개발하는 것은 복잡한 작업이 될 수도 있다.
# 만약 여러개의 폼을 관리해야 하는 경우 html을 작성해야 하며(id,password, email, address, phonenumber...)
# 데이터의 유효성을 검증하고, 유효하지 않은 입력에 대해서는 사용자가 알수 있도록 에러메시지를 표시해줘야 하며,
# 성공적으로 제출된 데이터를 적절히 처리하고,
# 마지막으로 성공했을 경우 사용자가 알수 있게 응답할 수 있도록 개발해야한다.
# 하지만 django 폼은 폼과 그에 연관된 필드를 정의하여 객체를 만들고,
# 폼 html 코드를 작성하는 작업과 데디터 유효성 검증에 이 객체들을 사용하여,
# 좀 더 효율적으로 코드를 구성할 수 있다.


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required' : '아이디를 입력해주세요'},
        max_length=32, label="사용자이름")
    password = forms.CharField(
        error_messages={'required' : '비밀번호를 입력해주세요'},
        widget=forms.PasswordInput, label="비밀번호") # PasswordInput : 비밀번호 마스킹 처리

    # 기본적 유효성검사 : 사용자이름과 비밀번호를 입력받았는지 받지 않았는지 검사는 해줌
    # 이외의 유효성검사를 만들어야함
    def clean(self): # 유효성 검사를 위해 clean 내장 함수 사용
        cleaned_data = super().clean() # clean 함수가 유효성 검사를 한후 cleaned_data를 반환함
        username = cleaned_data.get('username') # cleaned_data에는 form 데이터들이 dictionary 형태로 저장됨
        password = cleaned_data.get('password')

        if username and password:
            # 예외처리 필요 : 만약 login시 존재하지 않는 아이디로 로그인 시도시 DoesNotExist Excetpion 발생
            try :
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '아이디가 없습니다')
                return
                
            if not check_password(password, fcuser.password):
                self.add_error('password','비밀번호를 틀렸습니다.')
            else:
                # view에 id key 전달
                self.user_id=fcuser.id