from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('comment/create/<int:user_id>/', views.comment_create, name="comment_create"),
    path('user/create/',views.user_create, name="user_create")
]