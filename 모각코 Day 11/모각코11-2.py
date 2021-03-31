## Problem
welcome_message = "★☆★ Rock, Paper, Scissors! ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
print("가위바위보! 컴퓨터를 이겨라!")
choice = input("당신의 선택은? : ")
while choice not in ['가위', '바위', '보']:
    print("가위, 바위, 보 중에 하나를 입력해주세요!")
    choice = input("다시, 당신의 선택은? : ")


## Compete!
# Module import
import random
import time


# Function declaration
def RPS(player1, player2):
    if player1 == "가위":
        if player2 == "보":
            return "win"
        elif player2 == "바위":
            return "lose"
    elif player1 == "바위":
        if player2 == "가위":
            return "win"
        elif player2 == "보":
            return "lose"
    elif player1 == "보":
        if player2 == "바위":
            return "win"
        elif player2 == "가위":
            return "lose"
    return "draw"


def ComputerChoice():
    choices = ["가위", "바위", "보"]
    return choices[ random.randint(0, 2)]

print("컴퓨터와 가위바위보 대결을 합니다!")
time.sleep(1)
print("자, 그럼 시작합니다!")
time.sleep(1)
for idx, countdown in enumerate(["가위", "바위", "보"]):
    print('\t' * (idx + 1) + countdown + '!')
    time.sleep(0.5)

comp_choice = ComputerChoice()
print(f"나\t: {choice}")
time.sleep(0.2)
print(f"컴퓨터\t: {comp_choice}")

result = RPS(choice, comp_choice)
if result == "win":
    print("\n\t\t당신이 이겼습니다!!!")
elif result == "lose":
    print("\n\t\t당신이 졌습니다...")
else:
    print("\n\t\t비겼습니다!")

result_message = '-' * 20 + " 게임 끝 " + '-' * 20
print(f"\n\t {result_message}")