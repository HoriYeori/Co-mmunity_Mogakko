import re   # 정규표현식 활용

sentence = input("문장 입력 : ").lower()

for word in sentence.split('.'):    # 문장 별로 대소문자 정리 및 capitalization
    origin = word
    word = word.strip().capitalize()
    sentence = sentence.replace(origin, word)

sentence = sentence.replace(" i ", " I ")   # 단독 i 교정
for idx, word in enumerate(sentence.split()):   # 단어별 교정
    if re.match('^i[^A-Za-z0-9]+', word):    # 해당 단어가 i로 시작하는데, 그 i가 주어 I일 경우
        sentence = sentence.replace(word, word.capitalize())

sentence = sentence.replace('.', '. ').rstrip()
print("corrected sentence : " + sentence)
