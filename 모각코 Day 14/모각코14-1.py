## Problem
welcome_message = "★☆★ 24 to 12 ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
print("12시간제로 변환할 24시간제 시간을 입력해주세요.")
while True:
    try:
        time24 = list(map(int, input("\t\t\t24시간제 시간 :\t").split(':') ) )
        while not 0 <= time24[0] <= 23 \
            or not 0 <= time24[1] <= 59:
            print("시간 또는 분이 유효한 시간 범위를 벗어났습니다. 다시 입력해주세요.")
            time24 = list(map(int, input("\t\t\t24시간제 시간 :\t").split(':') ) )
    except:
        print("유효하지 않은 입력입니다. 다시 입력하세요.")
    else:
        break


## Transform
print()
print("\t12시간제로 변환된 24시간제 시간입니다.\n")

if time24[0] < 12:      # 오전
    print(f"\t24시간제 시간 %02d : %02d 은\n\t12시간제로 %02d : %02d AM 입니다."
          % (time24[0], time24[1], time24[0], time24[1]))
else:       # 오후
    if time24[0] == 12:
        print(f"\t24시간제 시간 %02d : %02d 은\n\t12시간제로 %02d : %02d PM 입니다."
              % (time24[0], time24[1], time24[0], time24[1]))
    else:
        print(f"\t24시간제 시간 %02d : %02d 은\n\t12시간제로 %02d : %02d PM 입니다."
              % (time24[0], time24[1], time24[0] - 12, time24[1]))