from django.db import models

# Create your models here.

class User(models.Model):
    gender = [
        ('M','Man'),
        ('W','Woman'),
    ]
    grade = [
        ('junior','주니어'),
        ('student','학생'),
        ('professor','교수님'),
        ('god','신'),
    ]
    name = models.CharField(max_length=20, verbose_name="이름", null=False)
    join_date = models.DateField(verbose_name="가입날짜", auto_now_add=True)
    birth_date = models.DateField(verbose_name="생일", null=False)
    level = models.CharField(choices=grade, default='junior', max_length=10)
    sex = models.CharField(choices=gender, max_length=1)

class Comment(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목", null=False)
    content = models.TextField(verbose_name="내용", null=False)
    create_date = models.DateField(verbose_name="생성날짜")
    author = models.ForeignKey(User, on_delete=models.CASCADE)



