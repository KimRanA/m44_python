# 1-45의 숫자중에서 중복되지 않는 랜덤 6개의 숫자를 뽑아서 출력하는 앱

import random

numbers = list(range(1, 46))

lotto = random.sample(numbers, 6)
#sample : 비복원무작위추출
lotto.sort()

print(f'행운의 숫자는 {lotto} 입니다!')
