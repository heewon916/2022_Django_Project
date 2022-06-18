from django.shortcuts import render
##--edit
from django.http import HttpResponse

from .models import Company
# Create your views here.

def index(request):
    #edit
    company_list = Company.objects.all() #Company 모델에 있는 정보를 전부 가져와서
    context = {'company_list': company_list} #company_list의 정보를 context에 담는다. 
    return render(request, 'stock/index.html', context) # company에 있는 정보를 모두 가져와서, index.html파일로 넘겨줄 것이다. 
