import code
import datetime
from urllib import response
from django.shortcuts import render
##--edit
from django.http import HttpResponse
from .models import Company
from bs4 import BeautifulSoup
import requests
import json
import MySQLdb
from datetime import date, datetime
import sqlite3
# Create your views here.

def getRank1to5():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    req = requests.get('https://finance.naver.com/', headers=header)  
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')

    ranks = []
    codes = []
    companys = []
    rates = []
    for i in range(1,6):
        rank = parse.select_one(f'#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child({i}) > th > em')
        rank = ''.join(rank.getText().split('.')[0])
        #print(tyrank))
        code = parse.select_one(f'#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child({i}) > td:nth-child(2)')
        code = ''.join(code.get_text().split(','))
        company  = parse.select_one(f'#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child({i}) > th > a')
        #print(company)
        company = ''.join(company.get_text().split(' '))
        ranks.append(rank)
        codes.append(code)
        companys.append(company)
        #print(code, company)
        
        #rates = parse.select_one(f'#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child({i}) > td:nth-child(3) > span')
        #container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr.up > td:nth-child(3) > span
        #container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > td:nth-child(3) > span
        #container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child(3) > td:nth-child(3) > span
        #container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr.up > td:nth-child(3) > span

        #container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr.up > td:nth-child(3) > em
        #container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > td:nth-child(3) > em

    #datefield = date.today()
    
    q = Company.objects.all()
    q.delete()
    
    for i in range(5):
        q = Company(rank=ranks[i], code=codes[i], company=companys[i], last_update=date.today(), last_update_time=datetime.now().strftime("%H:%M:%S"))
        q.save()
    #conn = sqlite3.connect("test.db", isolation_level=None)
    #cursor = conn.cursor()
    #cursor.execute("create table if not exists table1 ()")
    #for i in range(5):
    #    print(codes[i], companys[i])
    #    cursor.execute(f"INSERT INTO Com VALUES({codes[i]},\"{companys[i]}\",\"{datefield}\")")
        
'''
    conn = MySQLdb.connect(
        user="root",
        passwd="hkim916!@",
        host="localhost",
        db="stock_test"
        # charset="utf-8"
    )
    # ?????? ??????
    cursor = conn.cursor()

    # ????????? ????????? ???????????? ????????? ?????? ???????????? ???????????????
    #cursor.execute("DROP TABLE IF EXISTS melon")
    # ????????? ???????????? ?????? flush
    sql = "DELETE FROM stock_company"
    cursor.execute(sql)
    conn.commit()
    
    cursor = conn.cursor()
    # ????????? ????????????
    for i in range(5):
        print(codes[i], companys[i])
        cursor.execute(f"INSERT INTO stock_company VALUES({codes[i]},\"{companys[i]}\",\"{datefield}\")")
    # ????????????
    conn.commit()
    # ??????????????????
    conn.close()
''' 
def index(request):
    #edit
    getRank1to5()
    company_list = Company.objects.all() #Company ????????? ?????? ????????? ?????? ????????????
    context = {'company_list': company_list} #company_list??? ????????? context??? ?????????. 
    return render(request, 'stock/index.html', context)

'''
# naver finance ?????? ?????? ??????
    urls = 'https://finance.naver.com/sise/lastsearch2.naver'
    response = requests.get(urls)
        
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        company = soup.select_one('#contentarea > div.box_type_l > table > tbody > tr:nth-child(3) > td:nth-child(2) > a')
        code = soup.select_one('#contentarea > div.box_type_l > table > tbody > tr:nth-child(3) > td:nth-child(3)')
        rank = soup.select_one('#contentarea > div.box_type_l > table > tbody > tr:nth-child(3) > td.no')
        company_list = [code, company, rank]
        return_val = {'company_list':company_list}
    else : 
        #print(response.status_code)
        return_val = response.status_code
    return render(request, 'stock/index.html', return_val) # company??? ?????? ????????? ?????? ????????????, index.html????????? ????????? ?????????. 

'''

    
#headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
#res = requests.get(urls,headers=headers)

#soups = BeautifulSoup(res.text,'html.parser')

#top = soups.select("#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr > th")

#toplist = list()
#top2 = list()

#for tops in top:
#    toplist.append(tops.text.strip())

#for i in range(len(toplist)):
#    comp = top[i].text.strip()

    #item_objs={
    #   'comp':comp,
    #}
    #top2.append(item_objs)
    
#comps = top2
