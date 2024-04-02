from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Comment
from django.utils import timezone
from django.db.models import Q
# Create your views here.

def index(request):
    context = {'User_list' : User.objects.order_by('-date_joined')}
    return render(request, 'home/user_list.html', context)

def detail(request, User_id):
    user_obj = get_object_or_404(User, pk=User_id)
    Comment_list = Comment.objects.filter(author_id=user_obj.id)
    context = {'User' : user_obj, 'Comment_list' : Comment_list}
    return render(request, 'home/user_detail.html', context)

def comment_create(request, User_id):
    user = get_object_or_404(User, pk=User_id)
    #comment = get_object_or_404(Comment, pk=comment_id)
    user.comment_set.create(
        title=request.POST.get('title'),
        content=request.POST.get('content'),
        author=user,
        create_date=timezone.now(),
    )
    return redirect('home:detail', User_id=user.id)

def user_create(request):
    user = User(
        username=request.POST.get('username'),
        birth_date=request.POST.get('birth_date'),
        sex=request.POST.get('sex'),
        phone_num=request.POST('phone_num'),
    )
    user.save()
    return redirect('home:index')

def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('home:index')

def comment_delete(request, user_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('home:detail', user_id=user_id)

def user_modify(request, user_id):
    user=get_object_or_404(User, pk=user_id)
    content = {'modify' : user}
    return render(request, 'home/user_modify.html', content)

def user_modify2(request, user_id):
    user=get_object_or_404(User, pk=user_id)
    user.name=request.POST.get('name')
    birth_date=request.POST.get('birth_date')
    sex=request.POST.get('sex')
    user.save()
    return redirect('home:index')

def comment_modify(request, user_id, comment_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    content = {'User' : user, 'comment' : comment}
    return render(request, 'home/comment_modify.html', content)

def comment_modify2(request, user_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.title = request.POST.get('title')
    comment.content = request.POST.get('content')
    comment.create_date = timezone.now()
    comment.save()
    return redirect('home:detail', user_id=user_id)