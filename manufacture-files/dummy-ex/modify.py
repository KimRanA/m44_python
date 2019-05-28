# 사실 handle.py에 있던 지원자들은 합격자였다?!
# 지원자_ -> 합격자_
# dummy-ex 폴더 내의 모든 txt 파일 이름의 '지원자_'를 '합격자_'로 변경합니다.
# 'abc'.replace('b','e') => aec
#               ('바꿔질 문자열', '바꿀 문자열')

import os

filename = os.path.splitext(r'C:\Users\김란아\PycharmProjects\test\manufacture-files\dummy-ex\handle.py')
print(filename)
# ('C:\\Users\\김란아\\PycharmProjects\\test\\manufacture-files\\dummy-ex\\dummy', '.py') 출력됨.
# 파일이름과 확장자 .py가 떨어져서 반환됨.

os.chdir(r'C:\Users\김란아\PycharmProjects\test\manufacture-files\dummy-ex')
filenames = os.listdir('.')

for filename in filenames :
    txt = os.path.splitext(filename)[1] #확장자를 따로 분리함.

    if txt == '.txt' : #이 확장자가 .txt 파일이면
        # 앞에 지원자_ 를 붙인다.
        newfilename = filename.replace('지원자', '합격자')
        os.rename(filename,newfilename)