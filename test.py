print("정수를 입력해주세요")
a = int(input())
i = 1

print('%s*1 = %s' % (a,a*1))
print('%s*2 = %s' % (a,a*2))
print('%s*3 = %s' % (a,a*3))
print('%s*4 = %s' % (a,a*4))
print('%s*5 = %s' % (a,a*5))
print('%s*6 = %s' % (a,a*6))
print('%s*7 = %s' % (a,a*7))
print('%s*8 = %s' % (a,a*8))
print('%s*9 = %s' % (a,a*9))

def cal():
    for i in range(1,10):
        print('%s * %s = %s' %(a, i+1, a*i))

cal()

