from django.contrib import admin
from .models import Board # class Board(models.Model):

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Board,BoardAdmin)
# Fcuser을 admin.site.register에 등록함으로써, Django는 디폴트 관리자 폼 표현을 구성할 수 있음