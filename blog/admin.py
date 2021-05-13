from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Articles, Tags, Category, Author

admin.site.register(Tags)
admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Author)
