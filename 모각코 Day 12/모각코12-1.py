## Problem
welcome_message = "★☆★ Gugudan until die ★☆★"
print(f"\n\t {welcome_message} \n")


## Solve!

# Function declaration
def getInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print("유효하지 않은 입력입니다. 정수 범위의 숫자만 입력하세요.")
        else:
            return num

def printGugudan(dan):
    print(f"~~~ {dan}단을 외자 ~~~")
    for i in range(1, 10):
        print("\t%d x %d = %d" % (dan, i, dan * i))
    print("\n")


while True:
    message = "외우고 싶은 구구단의 단을 입력하세요(2부터 9까지, 1 입력 시 종료) : "
    num = getInt(message)

    if num == 1:
        result_message = '--' * 10 + " 구구단 외우기 끝! " + '--' * 10
        print(f"\n\t {result_message}")
        break
    elif 2 <= num <= 9:
        printGugudan(num)
    else:
        print("2단부터 9단까지만 볼 수 있습니다.\n")