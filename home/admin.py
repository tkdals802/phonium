from django.contrib import admin
from .models import User, Comment
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(User, UserAdmin)
admin.site.register(Comment)