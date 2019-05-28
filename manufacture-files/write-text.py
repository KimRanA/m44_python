# 파일을 여는 함수 open
# 1번째 매개변수로 파일 이름이 옴
# 2번째 매개변수로 open option
#   r : 읽기 - read
#   w : 쓰기 - write(overwrite)
#   a : 추가 - append
# open한 파일 객체를 반환한다.



# f = open('mulcam_for5.txt', 'w')  #파일명을 정하고 w(write)옵션을 넣음.
# for i in range(5) :
#     f.write(f'Happy Hacking {i}\n')
#
#
# for i in range(5) :
#     f.write(fd)
# f.close()


'''
파이썬에서 with 구문은 '컨텍스트 매니저' 이다.
with 블럭을 통해 명시적으로 파일을 불러서 작업하는 코드 블럭을 만들 수 있다.
with 블럭이 종료되면 자동으로 파일을 닫는다.
'''

with open('mulcam.txt', 'w') as f :
    for i in range(5) :
        f.write(f'Happy Hacking{i + 1}\n')