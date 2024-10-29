from django.contrib import admin
from .models import Create, Comment


class CreateAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Create, CreateAdmin)
admin.site.register(Comment)


