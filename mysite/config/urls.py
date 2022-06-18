"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
##--edit
from stock import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    ##--edit
    ##--path에서 'stock'이라는 이름으로 url을 사용할 것이고, 이는 views.py 내부의 index 함수에서 값을 받아온다는 의미이다.
    path('stock/', views.index),
]
