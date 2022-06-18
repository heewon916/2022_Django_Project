from bs4 import BeautifulSoup
import requests
import json
import MySQLdb
from datetime import date

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
req = requests.get('https://finance.naver.com/', headers=header)  
html = req.text
parse = BeautifulSoup(html, 'html.parser')

codes = []
companys = []
for i in range(1,6):
    code = parse.select_one(f'#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child({i}) > td:nth-child(2)')
    print(''.join(code.getText().split(',')))
    company  = parse.select_one(f'#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child({i}) > th > a')
    print(company.getText())
    codes.append(code)
    companys.append(company)
datefield = date.today()

conn = MySQLdb.connect(
    user="root",
    passwd="hkim916!@",
    host="localhost",
    db="stock_test"
    # charset="utf-8"
)
# 커서 생성
cursor = conn.cursor()

# 실행할 때마다 다른값이 나오지 않게 테이블을 제거해두기
#cursor.execute("DROP TABLE IF EXISTS melon")

# 데이터 저장하기
for i in range(5):
    cursor.execute(f"INSERT INTO stock_test VALUES({codes[i]},\"{companys[i]}\",\"{datefield}\")")
# 커밋하기
conn.commit()
# 연결종료하기
conn.close()