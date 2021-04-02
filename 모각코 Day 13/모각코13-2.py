## Problem
welcome_message = "★☆★ Round-robin discriminater ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
word = input("회문인지 판별할 단어를 입력해주세요 : ")
while len(word) < 3:
    print("3자 이상의 단어를 입력해주세요")
    word = input("\t\t\t\t(재입력) : ")


## Determine!
# Function declaration
def isRoundRobin(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True


if isRoundRobin(word):
    print(f"{word} 은(는) 회문입니다!")
else:
    print(f"{word} 은(는) 회문이 아닙니다!")