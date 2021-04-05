## Problem
welcome_message = "★☆★ Ascending sort ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
# getInt()
def getInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print("유효하지 않은 입력")
        else:
            return num

print("오름차순 정렬할 5개의 숫자를 입력해주세요.")
numbers = []
for i in range(5):
    num = getInt(f"\t{i+1} 번째 숫자 입력 ({i+1}/5) :\t")
    numbers.append(num)


## Preparation
# import module
import copy     # to preserve original list
import random

# Function declaration
# Bubble sort
def BubbleSort(numArray):
    for i in range( len(numArray) - 1):     # Total sorted count
        for j in range( len(numArray) - i - 1):     # Sorting phase
            if numArray[j] > numArray[j + 1]:
                numArray[j], numArray[j + 1] = numArray[j + 1], numArray[j]     # Swap

# Insertion sort
def InsertSort(numArray):
    for i in range(1, len(numArray)):
        key = numArray[i]
        pos = 0     # 삽입 위치
        while numArray[pos] < key and pos < i:
            pos += 1
        if pos < i:     # 삽입 위치 존재
            del numArray[i]
            numArray.insert(pos, key)   # Insert


## Sort!
origin = copy.deepcopy(numbers)
BubbleSort(numbers)

print("\n\t정렬이 완료되었습니다.\n")
print('\t' + str(origin) + "\t원본 숫자 배열")
print('\t' + str(numbers) + "\tBubble Sort 정렬 결과")

test = []
for i in range(5):
    test.append( random.randint(1, 1000))
print('\t' + str(test) + "\t임의 원본 숫자 배열")
InsertSort(test)
print('\t' + str(test) + "\tInsertion Sort 정렬 결과")