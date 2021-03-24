## Problem
welcome_message = "★☆★ 쿵쓰쿵쓰쿵쓰 쿵쿵따리 쿵쿵따 쿵쿵쿵쿵 ★☆★"
print(f"\n\t {welcome_message} \n")


## 게임 시작!
words = set()   # 대답으로 나온 단어 기억 공간

answer = input("\t시작: ")  # 시작!
words.add(answer)   # 단어 추가
cnt = 1
prev = answer   # 이전 단어 기억

while True:
    print(f"(쿵쿵따!) {prev[-1]} --> ", end='')   # 꾸미기
    answer = input()

    if prev[-1] == answer[0]:   # 끝말잇기 성립
        if answer in words: # 이미 나왔던 단어!
            print("\n이미 나왔던 단어입니다!! X-p")
            break   # 게임 종료
        prev = answer
        words.add(answer)   # 단어 추가
        cnt += 1
        if cnt % 5 == 0:
            print("\t[System]\t - 지금까지 %d 개의 단어가 나왔습니다 -" % cnt)
    else:   # 끝말잇기 미성립!
        print("\n끝말을 잇지 못했습니다!! X-p")
        break   # 게임 종료

result_message = "\t=-=-=-=-=-= 게임 종료 =-=-=-=-=-="
print(f"\n{result_message}")