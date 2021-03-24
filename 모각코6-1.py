## module import
import math     # for math.pi

## Problem
welcome_message = "★☆★ Plane figure's area calculator ★☆★"
print(f"\n\t {welcome_message} \n")

# Figure list
"""
figures = {'Circle': ['circle', 'Circle', '원'],
           'Triangle': ['triangle', 'Triangle', '삼각형'],
           'Rectangle': ['rectangle', 'Rectangle', '직사각형'],
           'Square': ['square', 'Square', '정사각형']}
"""
figures = ['circle',
           'triangle',
           'rectangle',
           'square']

print('-' * 5 + " Figure List " + '-' * 5)
for idx, figure in enumerate(figures):
    print("{idx:3}. {fig:^18}".format(idx=idx+1, fig=figure))
print('-' * 23)


## Get input
while True:
    try:
        print("넓이를 계산할 도형을 선택하세요")
        menu = int(input("\t\t 도형 번호 : "))
        while menu <= 0 or menu >= len(figures):    # out of range
            print("1번부터 %d번 사이의 번호를 입력하세요" % len(figures))
            menu = int(input("\t\t 도형 번호 : "))

    except: # ValueError
        print("올바른 값을 입력하세요\n")
    else:   # Exception unrisen
        menu -= 1   # 메뉴 번호 - 인덱스 획일화
        break


# Functions for calculation
def getCircleArea():
    while True:
        try:
            radius = float(input("원의 반지름을 입력해주세요 : "))
        except:
            print("올바른 값을 입력하세요")
        else:
            return radius, math.pi * (radius ** 2)

def getTriangleArea():
    while True:
        try:
            width = float(input("삼각형의 밑변 길이를 입력해주세요 : "))
            height = float(input("삼각형의 높이를 입력해주세요 : "))
        except:
            print("올바른 값을 입력하세요. 다시 입력해주세요")
        else:
            return width, height, width * height / 2

def getRectangleArea(square=False):
    while True:
        try:
            if square:
                width = float(input("정사각형의 한 변의 길이를 입력해주세요 : "))
            else:
                width = float(input("직사각형의 가로 길이를 입력해주세요 : "))
                height = float(input("직사각형의 세로 길이를 입력해주세요 : "))
        except:
            print("올바른 값을 입력하세요. 다시 입력해주세요")
        else:
            if square:
                return width, width ** 2
            else:
                return width, height, width * height


## Calculation
select = figures[menu]
print("선택한 도형 : %s" % select)
if select == 'circle':
    radius, area = getCircleArea()
    print("반지름이 {rad}인 원의 넓이는 [ {area:.2f} ] 입니다.".format(rad=radius, area=area))


elif select == 'triangle':
    width, height, area = getTriangleArea()
    print("밑변이 {width}이고 높이가 {height}인 삼각형의 넓이는 [ {area:.2f} ] 입니다.".format(width=width, height=height, area=area))


elif select == 'rectangle':
    width, height, area = getRectangleArea()
    print("가로의 길이가 {width}이고 세로가 {height}인 직사각형의 넓이는 [ {area:.2f} ] 입니다.".format(width=width, height=height, area=area))

elif select == 'square':
    width, area = getRectangleArea(True)
    print("한 변의 길이가 {width}인 정사각형의 넓이는 [ {area:.2f} ] 입니다.".format(width=width, area=area))