from django.contrib import admin
from .models import Comment, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(User, UserAdmin)
admin.site.register(Comment)