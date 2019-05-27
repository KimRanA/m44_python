#basic-syntax
# ' ' 로 감싸면 String
print('안녕하세요!')
print('저는 김란아 입니다.')
print('만나서 반갑습니다^.^')

# ''' 3개를 이어서 쓰면 줄바꿈 가능
print('''안녕하세요!
저는 김란아 입니다.
만나서 반갑습니다^.^''')

# Randge 숫자의 범위를 가지고 있음
print(range(5))  # => range(0, 5)

# List 형변환
a = list(range(5))
print(a)  # => [0, 1, 2, 3, 4]

for i in range(5) :
    print(i)

# List
# 배열이다. 여러개의 멤버변수를 가질 수 있으며 index를 통한 접근이 가능하다.
# 다른 언어에서는 Array라고 불린다.
numbers = [0, 1, 2, 3]
print(numbers[0])  # => 0
print(numbers[-1])  # => 3
print('----------')  # 구분선
numbers = [3, 1, 2]
print(sorted(numbers))  # => [1, 2, 3]
print(numbers)  # => [3, 1, 2] sorted() 함수는 배열을 정렬해주지만 원본을 바꾸지는 않는다.

print(numbers.sort())  # => None 아무것도 반환해주지않고 있음.
print(numbers)  # => [1, 2, 3] 정렬되어 있음. sort() 함수는 원본을 바꿔준다.

# Dictionary
# Key와 value로 이루어진 자료구조
# 다른 언어에서는 map(자바), object(자바스크립트) 라고도 불린다.
phonebook = {
    '중국집' : '123-456',
    '초밥집' : '8464-5215',
    '짬뽕집' : '789-456'
}

# 중국집에 전화번호로 접근하고 싶다면 어떻게 해야할까?
print(phonebook['중국집'])  # => 123-456