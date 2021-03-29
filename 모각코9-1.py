## Problem
welcome_message = "★☆★ N's aliquots ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
print("약수를 구하고 싶은 수를 입력하세요.")
while True:
    try:
        n = int(input("\t수 입력 :\t"))
        while n <= 0:
            print("1 이상의 자연수를 입력하세요.")
            n = int(input("\t수 입력 :\t"))
    except:
        print("유효하지 않은 수입니다. 정수만 입력해야 합니다.")
    else:
        break

print("%d의 몇 번째 약수를 구하고 싶으신가요?" % n)
while True:
    try:
        k = int(input("\t몇 번째? :\t"))
        while n <= 0:
            print("1 이상의 자연수를 입력하세요.")
            k = int(input("몇 번째? :\t"))
    except:
        print("유효하지 않은 수입니다. 정수만 입력해야 합니다.")
    else:
        break


## Find out
i = 0       # 1부터 찾아 올라갈 수
cnt = 0     # 찾은 약수의 개수
while cnt < k and i <= n:   # k번째 약수를 찾거나 약수를 계속 찾아도 k번째 약수는 없을 경우
    i += 1
    if n % i == 0:
        cnt += 1

if cnt < k:
    print(f"{n}의 약수는 {k}개나 존재하지 않습니다.")
else:
    print(f"{n}의 {k}번째 약수는 {i}입니다.")

result_message = "\t---------- k번째 약수 찾기 끝 ----------"
print(f"\n{result_message}")