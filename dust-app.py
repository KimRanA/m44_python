import requests  # 라이브러리 호출
# 특정 주소로 요청을 보내서 응답을 받는 라이브러리
# http : 요청과 응답으로 이루어진 프로토콜

from bs4 import BeautifulSoup

# 응답받은 html문서나 xml등을 파이썬에서 사용하기 좋도록 예쁘게 파싱해줌.
# 의미있는 코드로 변환시켜 파이썬에서 사용할 수 있도록 함.
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=QaGapZXPV5DTM72fy6lrf3hJnrJxhila1UVkPlUCo0N0g0F0RZ9WEngT8RkNjNo4IF%2BikV%2BthQLze39nK4IQjA%3D%3D&numOfRows=10&pageSize=10&pageNo=3&startPage=3&sidoName=%EC%84%9C%EC%9A%B8&ver=1.6'
# api란? 응용프로그램들이 서로 데이터를 주고받는 방법.
# 어떠한 방식으로 정보를 주고 받을지를 정의해놓은 것.

request = requests.get(url).text
soup = BeautifulSoup(request, 'xml')
# print(soup)
print(type(soup))  # <class 'bs4.BeautifulSoup'>
gangnam = soup('item')[7]
location = gangnam.stationName.text
time = gangnam.dataTime.text
dust = int(gangnam.pm10Value.text)  # dust를 10시 기준으로 가져오겠다.

# dust 변수에 들어 있는 내용을 출력해보세요.
print('{0} 기준 {1}의 미세먼지 농도는 {2}입니다.'.format(time, location, dust))
print(f'{time} 기준 {location}의 미세먼지 농도는 {dust}입니다.')

if 150 < dust:
    print('매우나쁨')
elif 80 < dust <= 150:
    print('나쁨')
elif 30 < dust and dust <= 80:
    print('보통')
else:
    print('좋음')
