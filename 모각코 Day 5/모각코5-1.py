## Problem
welcome_message = "★☆★ OX퀴즈 점수 계산기 ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
ox_answers = input("OX퀴즈의 결과 : ")


# 점수 계산
result_message = "OX퀴즈 답안 \"%s\" 의 점수는" % ox_answers
print(f"\n{result_message}")

score = 0

seq = 0
for elem in ox_answers:
   if elem in ['O', 'o']:   # 대소문자 무시
       seq += 1         # 누적 'O' 개수 점수화
       score += seq     # 누적 'O' 개수 점수 합산
   elif elem in ['X', 'x']: # 대소문자 무시
       seq = 0          # 누적 점수 초기화

print("\t\t\t[%d 점] 입니다." % score)