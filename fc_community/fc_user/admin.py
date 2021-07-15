from django.contrib import admin
from .models import Fcuser # class Fcuser(models.Model):

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username','useremail','password','registered_dttm')

admin.site.register(Fcuser,FcuserAdmin)
# Fcuser을 admin.site.register에 등록함으로써, Django는 디폴트 관리자 폼 표현을 구성할 수 있음