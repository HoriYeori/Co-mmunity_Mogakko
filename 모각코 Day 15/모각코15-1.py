## Problem
welcome_message = "★☆★ Finding day of week ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input

# getInt()
def getInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print("유효하지 않은 입력입니다. 정수 범위의 숫자만 입력해주세요.")
        else:
            return num

print("요일을 찾을 날짜를 입력해주세요.")
month = getInt("\t 월 :\t")
while 1 > month or 12 < month:
    print("입력 가능한 월 범위를 벗어났습니다.")
    month = getInt("\t [재입력] 월 (1 ~ 12) :\t")

day = getInt("\t 일 :\t")
if month != 2:
    while 1 > day or 31 < day:
        print("입력 가능한 일 범위를 벗어났습니다.")
        day = getInt("\t [재입력] 일 (1 ~ 31) :\t")
else:
    while 1 > day or 28 < day:
        print("입력 가능한 일 범위를 벗어났습니다.")
        day = getInt("\t [재입력] 일 (1 ~ 28) :\t")


## Find!
# module import
import datetime


dayofweek = "일월화수목금토"   # 일: 0, 월: 1, 화: 2, 수: 3, ...

year = 2021
date = datetime.date(year, month, day)
print(f"\n\t{month}월 {day}일은 {dayofweek[ date.weekday()+1]}요일 입니다.")
# 또는 print(f"\n\t{month}월 {day}일은 {dayofweek[ date.isoweekday()]}요일 입니다.")


"""
dayofweek = "일월화수목금토"   # 일: 0, 월: 1, 화: 2, 수: 3, ...
days = [ 31, 28, 31, 30,
         31, 30, 31, 31,
         30, 31, 30, 31]    # from January to December

# 1월 1일부터 입력한 날짜까지 지난 날 수 계산
passed = 0
for i in range(month - 1):
    passed += days[i]
passed += day - 1   # 어제까지가 '지난' 날임

# 7로 나눈 나머지를 통해 요일 계산
base = 5    # 2021년의 시작은 금요일
print(f"\n\t{month}월 {day}일은 {dayofweek[ (passed + base) % 7]}요일이며,")
print(f"\t1월 1일로부터 {passed}일 지났습니다.")
"""