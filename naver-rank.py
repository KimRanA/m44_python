# naver에서 html 파일을 가지고 온다.
# beautyfulSoup 를 이용해서 parsing 한다.
# 실시간 검색어 10위까지 출력한다.
import requests #네이버로 보내야하니깐.
from bs4 import BeautifulSoup
url = 'https://www.naver.com/'
response = requests.get(url).text #리퀘스트를 이용해서 GET요청을 보낼 것.
#그리고 text로 가져올 것임.
soup = BeautifulSoup(response,'html.parser')
#soup = bs4.BeautifulSoup(request,'html')도 같음.
results = soup.find_all('span', class_='ah_k')
#우리가 찾으려는 것은 span태그이고 class이름은 'ah_k'이다.
index = 0
for result in results :
  index = index + 1
  print(index, result.text)