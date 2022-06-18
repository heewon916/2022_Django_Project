from django.contrib import admin
from .models import Company
# Register your models here.

# 검색 기능 추가
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['company']

admin.site.register(Company, CompanyAdmin)