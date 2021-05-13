from __future__ import unicode_literals
from django.shortcuts import render
from .models import Cal


# Create your views here.
def index(request):
    return render(request, 'index.html')


def calc(request):
    return render(request, 'calc.html')


def rst(request):
    value_a = request.POST['valueA']
    value_b = request.POST['valueB']
    result = int(value_a) + int(value_b)
    Cal.objects.create(value_a=value_a, value_b=value_b, result=result)
    return render(request, 'result.html', {'result': result, 'value_a': value_a, 'value_b': value_b})
