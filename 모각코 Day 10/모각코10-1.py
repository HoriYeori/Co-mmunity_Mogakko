## Problem
welcome_message = "★☆★ Time converter ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
while True:
    try:
        time = int(input("변환할 초 단위 시간 : "))
        while time < 1:
            print("1초 이상 입력하세요.")
            time = int(input("변환할 초 단위 시간 : "))
    except:
        print("정수만 입력해야 합니다. 다시 입력하세요.")
    else:
        break


## Convert

# Function definition
def TimeConverter(t):
    hour = t // (60 * 60)
    t %= (60 * 60)
    minute = t // 60
    t %= 60

    return hour, minute, t


h, m, s = TimeConverter(time)

print(f"전체 시간 {time}초의 변환 결과입니다.")
print(f"\t- 전체 시간 {time}초 = ", end='')

if h != 0:
    print(f"{h}시간 ", end='')
if m != 0:
    print(f"{m}분 ", end='')
if s != 0:
    print(f"{s}초")


result_message = '-' * 10 + " 변환 완료 " + '-' * 10
print(f"\n\t {result_message}")