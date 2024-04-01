from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('comment/create/<int:user_id>/', views.comment_create, name="comment_create"),
    path('user/create/',views.user_create, name="user_create"),
    path('user/delete/<int:user_id>/', views.user_delete, name="user_delete"),
    path('comment/delete/<int:user_id>/<int:comment_id>/', views.comment_delete, name="comment_delete"),
    path('user/modify/<int:user_id>/', views.user_modify, name="user_modify"),
    path('user/modify2/<int:user_id>/', views.user_modify2, name="user_modify2"),
    path('comment/modify/<int:user_id>/<int:comment_id>', views.comment_modify, name="comment_modify"),
    path('comment/modify2/<int:user_id>/<int:comment_id>', views.comment_modify2, name="comment_modify2"),

]