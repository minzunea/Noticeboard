from django.contrib import admin

# Register your models here.

from .models import Create
admin.site.register(Create)

from .models import Comment
admin.site.register(Comment)