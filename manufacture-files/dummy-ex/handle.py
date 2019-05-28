import os
# os.chdir('폴더 경로') : 지정한 폴더로 이동
# os.list('폴더 경로') : 폴더에 저장된 전체 파일 목록을 list로 반환
# os.rename('현재 파일명', '바꿀 파일명') :파일이름 변경
# os.path.splitext('파일 이동') : 파일 경로와 확장자를 분리하여 반환

# 폴더 경로 C:\Users\김란아\PycharmProjects\test\manufacture-files\dummy-ex

filename = os.path.splitext(r'C:\Users\김란아\PycharmProjects\test\manufacture-files\dummy-ex\dummy.py')
print(filename)
# ('C:\\Users\\김란아\\PycharmProjects\\test\\manufacture-files\\dummy-ex\\dummy', '.py') 출력됨.
# 파일이름과 확장자 .py가 떨어져서 반환됨.

os.chdir(r'C:\Users\김란아\PycharmProjects\test\manufacture-files\dummy-ex')
filenames = os.listdir('.')

for filename in filenames :
    txt = os.path.splitext(filename)[-1]
    if txt == '.txt' :
        # 앞에 지원자_ 를 붙인다.
        os.rename(filename, f'지원자_{filename}')
        #f string! 안에 변수 사용 가능.
        print(txt)