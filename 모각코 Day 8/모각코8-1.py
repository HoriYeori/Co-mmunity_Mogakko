## Problem
welcome_message = "★☆★ Perimeter and Area of Rectangle ★☆★"
print(f"\n\t {welcome_message} \n")


## Class definition
class Rectangle():
    ## Constructor
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height


    ## Methods
    # Getter
    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_area(self):
        return self.width * self.height


## Get input
print("직사각형을 하나 생성합니다.")
while True:     # Get width
    try:
        width = int(input("\t가로 길이 : "))
        while width <= 0:
            print("\t길이는 자연수여야 합니다.")
            width = int(input("\t (재입력) 가로 길이 : "))
    except:
        print("정수 범위의 수를 입력하세요.")
    else:
        break

while True:     # Get height
    try:
        height = int(input("\t세로 길이 : "))
        while height <= 0:
            print("\t길이는 자연수여야 합니다.")
            height = int(input("\t (재입력) 세로 길이 : "))
    except:
        print("정수 범위의 수를 입력하세요.")
    else:
        break

rect = Rectangle(width, height)
print("가로 %d, 세로 %d의 직사각형은" % (rect.width, rect.height))
print("둘레가 [ %d ], 넓이가 [ %d ]입니다." % (rect.get_perimeter(), rect.get_area()))