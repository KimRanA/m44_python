#numbers.txt의 내용을 뒤집어서 작성한다.
# with open('number.txt', 'r') as f :
#     all_text = list(f.read())
#     all_text.reverse()
#     print(all_text)
#     for i in range(10) :
#         print(all_text[i])
#     print(all_text)

with open('number.txt', 'r') as f :
    lines = f.readlines()

#리스트 뒤집기
lines.reverse()
print(lines)



# with open('number.txt', 'w') as f :
#     for line in lines :
#         f.write(line)

with open('number.txt', 'w') as f :
     for line in lines :
         #String.strip() : 문자열의 처음과 끝의 공백을 지워주는 매소드

         f.write(line.rstrip() + '\n')