## Problem
welcome_message = "★☆★ Scores' average calculator ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
print("전체 과목 개수를 입력하세요.")
while True:
    try:
        nSubject = int(input("\t전체 과목 수 :\t"))
        while nSubject < 1:
            print("최소한 1개의 과목을 입력해야 합니다. 1 이상의 수를 입력하세요.")
            nSubject = int(input("\t전체 과목 수 :\t"))
    except:
        print("유효하지 않은 입력입니다. 정수만 입력해야 합니다. 다시 입력해주세요.")
    else:
        break


## Calculation

# Function definition
def getGrade(score):
    grade_boundary = {'A': 90,
                      'B': 80,
                      'C': 70,
                      'D': 60}

    if score >= grade_boundary['A']:
        return 'A'
    elif score >= grade_boundary['B']:
        return 'B'
    elif score >= grade_boundary['C']:
        return 'C'
    elif score >= grade_boundary['D']:
        return 'D'
    else:
        return 'F'

def calcAverage(scores):
    return sum(scores) / len(scores)


scores = []
for i in range(1, nSubject + 1):
    print("%d번째 과목의 점수를 입력하세요." % i)
    while True:
        try:
            score = float(input("\t%d번째 과목 점수 :\t" % i))
            while 0 > score and score < 100:
                print("점수는 0점 이상 100점 이하여야 합니다.")
                score = float(input("\t(재입력) %d번째 과목 점수 :\t" % i))
        except:
            print("입력이 유효하지 않습니다. 다시 입력해주세요.")
        else:
            scores.append(score)
            print("%d번째 과목의 등급은 [ %c ] 입니다.\n" % (i, getGrade(score)))
            break

print("= " * 15)
print("전체 과목의 점수 평균은 [ %.2f ]점 입니다." % calcAverage(scores))

result_message = '-' * 10 + " 등급 & 평균 계산 종료 " + '-' * 10
print(f"\n{result_message}")