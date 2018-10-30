from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def insert(request):
    for i in range(1, 1001):
        Board.objects.create(title='제목'+ str(i), content='내용'+str(i))
    return HttpResponse('insert 100')

def board_list(request):

    return render(request, '', {})