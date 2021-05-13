from django.shortcuts import render
from blog import models


# Create your views here.
def index(request):
    blog_index = models.Articles.objects.all().order_by('id')
    return render(request, 'blog.html', {'blog_index': blog_index})
