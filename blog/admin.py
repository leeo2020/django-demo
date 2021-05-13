from django.contrib import admin

# Register your models here.
from .models import Articles


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'createdTime']
    list_display_links = ['title']


admin.site.register(Articles, ArticleAdmin)
