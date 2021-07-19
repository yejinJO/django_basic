from django.db import models

# Create your models here.
class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                verbose_name='사용자이메일') # EmailField를 사용하면 이메일 형식을 알아서 검사해줌
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')

    # django가 자동으로 생성하는 admin에서도 객체의 표현이 사용되기 때문에 __str__메서드 사용
    # 

    def __str__(self):
        return self.username

    class Meta: # 테이블명 지정
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자들'
