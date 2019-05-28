#lunch-menu.py
import random

# menu 리스트를 만들어주세요.
menu = ["20층", "먹지마", "순대국", "내장탕"]
phonebook = {
    '20층' : '123-456',
    '먹지마' : '8464-5215',
    '순대국' : '789-456',
    '내장탕' : '555-4444'
}
choice = random.choice(menu) #랜덤한 식당
print('오늘의 점심은 ' + choice + '입니다.')
print(f'오늘의 점심은 {choice} 입니다.') #파이썬 3점대부터 가능.
print('식당의 전화번호는 ' + phonebook[choice] + '입니다.')
print(f'식당의 전화번호는 {phonebook[choice]} 입니다.') #파이썬 3점대부터 가능.
