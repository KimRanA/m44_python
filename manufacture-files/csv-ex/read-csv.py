#read-csv.py

# 1. split 으로 가져오는 방법
with open('lunch.csv', 'r', encoding='utf-8') as f :
    lines = f.readlines()
    for line in lines :
        print(line.s,trip().split(','))
        #strip : 공백제거, #split('') : 공백을 기본으로 나누기.
        pass

#2. csv.reader
import csv
with open('lunch.csv', 'r', encoding = 'utf-8') as f :
    items = csv.reader(f)
    for item in items :
        print(item)