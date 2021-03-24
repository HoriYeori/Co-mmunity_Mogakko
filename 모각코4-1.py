## Problem
welcome_message = "★☆★ 팩토리얼 값 계산기 ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
try:
    print("20 이하의 양의 정수를 입력하세요. (잘못된 값 입력시 에러)")
    num = int(input("\t\t: "))
    while num < 0 or num > 20:
        if num < 0:
            print("0 이상의 정수만 입력하세요.")
            num = int(input("\t\t: "))
        else:
            print("20 이하의 수만 입력하세요.")
            num = int(input("\t\t: "))

except: # int() ValueError handling
    print("올바른 값을 입력해주세요!")
    while True:
        try:
            num = int(input("\t\t재입력 : "))
            while num < 0 or num > 20:
                if num < 0:
                    print("0 이상의 정수만 입력하세요.")
                    num = int(input("\t\t: "))
                else:
                    print("20 이하의 수만 입력하세요.")
                    num = int(input("\t\t: "))
        except:
            pass
        else:
            break


# 팩토리얼 계산
result_message = "--" * 5 + " 결 과 " + "--" * 5

if num == 0:
    print("0 팩토리얼(0!)은 1입니다!")
    print(f"\n\t {result_message} \n")
    print("\t0! = 1")
else:
    factorial = 1

    print(f"\n\t {result_message} \n")
    print(f"\t{num}! = ", end ='')
    for digit in range(num, 1, -1):
        print(f"{digit} x ", end='')
        factorial *= digit
    print("1 = %d" % factorial)
    print("\t{num}!은 {factorial:,} 입니다.".format(num=num, factorial=factorial))