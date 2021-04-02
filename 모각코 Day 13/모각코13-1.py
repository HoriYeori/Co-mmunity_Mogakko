## Problem
welcome_message = "★☆★ Factorization ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
while True:
    try:
        num = int(input("소인수분해 할 숫자를 입력해주세요 : "))
        while num < 2:
            print("1 이상의 정수를 입력해야 합니다! 다시 입력해주세요.")
            num = int(input("소인수분해 할 숫자를 입력해주세요 : "))
    except:
        print("정수 범위의 숫자만 입력해야 합니다. 다시 입력해주세요.")
    else:
        break


## Factorize!
# Function declaration
def isPrime(num):
    i = 2
    while i ** 2 <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def Factorization(num):
    factors = {}    # 소인수분해 목록
    div = 2     # 시작 인수
    while num > 1:
        if num % div == 0:  # 인수에 해당함
            num /= div
            if factors.get(div) == None:    # 처음 등장한 인수일 경우 목록에 추가
                factors[div] = 0
            factors[div] += 1   # 인수 개수 증가
        else:   # 인수가 아님
            div += 1    # 다음 인수로
            while not isPrime(div):     # 인수가 소수일 때까지 +1
                div += 1

    return factors


if isPrime(num):
    print(f"\t{num}은 소수입니다.")
else:
    factors = Factorization(num)
    print(f"\t{num} 의 소인수분해 결과입니다.\n")
    print(f"\t--> {num} = ", end='')
    for factor in sorted(list(factors.keys())):
        if factors[factor] == 1:
            print("%d x " % factor, end='')
        else:
            print("%d^%d x " % (factor, factors[factor]), end='')
    print("\b\b")   # 마지막 x 지우기