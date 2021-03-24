## Problem
welcome_message = "★☆★ 배수 찾기 ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
try:
    print("숫자 두 개를 입력하세요. (공백으로 구분)")
    a, b = map(int, input("\t : ").split())

except: # int() ValueError handling
    print("정수 두 개를 공백으로 구분해서 입력해주세요.")
    while True:
        try:
            a, b = map(int, input("\t : ").split())
        except:
            print("다시 입력하세요.")
        else:
            break

try:
    print("입력한 두 수 사이의 알고 싶은 배수를 입력해주세요.")
    multiple = int(input("\t : "))
    while multiple < 2:
        if multiple == 1:
            print("2 이상의 정수를 입력해주세요.")
        else:
            print("자연수를 입력해주세요.")
        multiple = int(input("\t : "))

except:
    print("자연수만 입력해주세요.")
    while True:
        try:
            multiple = int(input("\t : "))
            while multiple < 2:
                if multiple == 1:
                    print("2 이상의 정수를 입력해주세요.")
                else:
                    print("자연수를 입력해주세요.")
                multiple = int(input("\t : "))
        except:
            print("다시 입력하세요")
        else:
            break


# 배수 찾기
if a > b:   # 만약 a부터 b가 아니라 b부터 a라면
    tmp = a
    a = b
    b = tmp

result_message = "{a} 부터 {b} 까지 {multiple}의 배수 목록".format(a=a, b=b, multiple=multiple)
print(f"\n{result_message}")

while a % multiple != 0:    # 시작점 끌어올리기
    a += 1

cnt = 0
for n in range(a, b + 1, multiple):
    if cnt % 5 == 0:
        print()
    print("%d  " % n, end='')
    cnt += 1

print(f"\n\t - 총 {cnt} 개")