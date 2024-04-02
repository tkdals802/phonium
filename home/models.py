from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
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
    birth_date = models.DateField(verbose_name="생일", default='1111-01-01')
    level = models.CharField(choices=grade, default='junior', max_length=10)
    sex = models.CharField(choices=gender, max_length=1)
    phone_num = PhoneNumberField(verbose_name="전화번호",unique=True)


class Comment(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목", null=False)
    content = models.TextField(verbose_name="내용", null=False)
    create_date = models.DateField(verbose_name="생성날짜")
    author = models.ForeignKey(User, on_delete=models.CASCADE)



