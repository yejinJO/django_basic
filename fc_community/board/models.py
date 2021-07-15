from django.db import models

# Create your models here.from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128,
                                verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fc_user.Fcuser',on_delete=models.CASCADE,
                                verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')

    # django가 자동으로 생성하는 admin에서도 객체의 표현이 사용되기 때문에 __str__메서드 사용
    # 

    def __str__(self):
        return self.title

    class Meta: # 테이블명 지정
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글들'
