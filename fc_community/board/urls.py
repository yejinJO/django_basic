from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.board_list),
    path('write/',views.board_write),
    path('detail/<int:pk>/',views.board_detail), # int형 pk변수로 받아오겠다
]
