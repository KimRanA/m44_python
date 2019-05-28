# naver에서 html 파일을 가지고 온다.
# beautyfulSoup 를 이용해서 parsing 한다.
# 실시간 검색어 10위까지 출력한다.

import requests #네이버로 보내야하니깐.
from bs4 import BeautifulSoup
url = 'https://www.bithumb.com/'
html = requests.get(url).text

soup = BeautifulSoup(html,'html.parser')
#soup = bs4.BeautifulSoup(request,'html')도 같음.
coins = soup.select('.coin_list tr')

with open('bitumb.csv', 'w', encoding='utf-8') as f :
    for coin in coins :
        name = coin.select_one('td:nth-of-type(1) p a strong').text.strip()#공백지우기
    #td:nth-child라는 css 문법이 있음. (1)이면 첫번째 있는 것을 가져오겠다.
    #p태그, a태그 안의 strong을 가져오겠다.
    #코인 이름 가져오기 성공!
        """
        print(name)
        비트코인
        이더리움
        대시
        ...
        """
        price = coin.select_one('td:nth-of-type(2) strong').text.replace(',','') #콤마 지우기
        """
        print(name, price)
        비트코인  10,381,000원
        이더리움  320,700원
        대시  203,600원
        """
        f.write(f'{name},{price}\n')