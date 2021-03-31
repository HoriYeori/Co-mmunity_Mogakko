## Problem
welcome_message = "★☆★ Find middle letter ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
word = input("단어를 입력하세요 : ")


## Find out

# Function declaration
def MiddleLetter(word):
    length = len(word)

    if length == 1:
        return word
    else:
        mid = int(length / 2)
        if length % 2 == 1:
            return word[mid]
        else:
            return word[mid - 1] + word[mid]


print(f"단어 \"{word}\"의 가운데 글자는 \'{MiddleLetter(word)}\' 입니다.")