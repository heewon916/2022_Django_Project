from django.shortcuts import render
##--edit
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("안녕하세요, 기본 페이지입니다.")
