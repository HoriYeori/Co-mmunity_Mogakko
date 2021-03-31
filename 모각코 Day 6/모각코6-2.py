## Problem
welcome_message = "★☆★ 뒤집은 수 소수 판별기 ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input

# 전체 수 개수 입력
while True:
    try:
        print("입력받을 수의 개수를 입력하세요.")
        n = int(input("\t 개수 : "))
        while n < 1:
            print("1 이상의 자연수를 입력해주세요.")
            n = input("\t 개수 : ")
    except:
        print("올바르지 않은 입력입니다. 다시 입력해주세요.\n")
    else:
        break

# 소수인지 판별할 수 입력
nums = []
for i in range(n):
    while True:
        try:
            print(f"수 입력(%d/%d) : " % (i+1, n), end='')
            num = int(input())
        except:
            print("자연수만 입력해주세요")
        else:
            nums.append(num)
            break



## Distinguish prime

# Function 1 - to reverse number
def number_reverser(num):
    num_str = str(num)
    reverse = []
    for i in range( len(num_str)-1, -1, -1):
        """
        주어진 수를 문자열로 바꿨을 때, 문자열의 중앙을 기준으로 대칭되는 위치의 수를 바꿔줍니다.
        문자열의 길이가 홀수라면 중앙에 있는 수는 건드릴 필요가 없고,
        문자열의 길이가 짝수라면 모든 수가 대칭되는 위치의 수와 자리가 바뀌게 됩니다.
        
        ( num_str[i], num_str[end-i] = Swap(num_str[i], num_str[end-i]) )
        라고 '안 파이썬 스럽게' 생각했었네요...
        """
        reverse.append(num_str[i])
    return int( ''.join(reverse))



# Function 2 - to differentiate whether prime or not
def isPrime(num):
    if num == 1:    # 1은 소수가 아님
        return False

    i = 2
    while i ** 2 <= num:    # 제곱근법 활용
        if num % i == 0:
            return False
        else:
            i += 1
    return True


primes = []
for idx, num in enumerate(nums):
    if isPrime(number_reverser(num)):
        primes.append([idx, num])

if len(primes) == 0:
    print("입력하신 수 중에 뒤집어서 소수가 되는 수는 없습니다.")
else:
    for i in range(len(primes)):
        idx, num = primes[i]
        print("{idx}번째로 입력하신 수 {num}는 뒤집었을 때 소수입니다. ({num} -> {reverse})".format(idx=idx+1, num=num, reverse=number_reverser(num) ) )


result_message = "\t---------- 프로그램 종료 ----------"
print(f"\n{result_message}")