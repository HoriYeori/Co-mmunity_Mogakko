## Problem
welcome_message = "★☆★ Coordinate Set-up ★☆★"
print(f"\n\t {welcome_message} \n")


## Class definition
class Point():
    ## Constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print("새로운 좌표가 생성되었습니다. 좌표 : ( %d, %d )\n" % (self.x, self.y))


    ## Methods
    # Setter
    def setX(self, new_x):
        old = self.x
        self.x = new_x
        print("새로운 X좌표가 설정되었습니다. ( %d --> %d )" % (old, new_x))
        print("\t현재 좌표 : ( %d, %d )" % (self.x, self.y))
        print()

    def setY(self, new_y):
        old = self.y
        self.y = new_y
        print("새로운 Y좌표가 설정되었습니다. ( %d --> %d )" % (old, new_y))
        print("\t현재 좌표 : ( %d, %d )" % (self.x, self.y))
        print()

    # Getter
    def getCoordinate(self):
        return self.x, self.y

    # Function
    def Move(self, new_x, new_y):
        old_x = self.x
        old_y = self.y
        self.x = new_x
        self.y = new_y

        print("새로운 좌표로 이동되었습니다.")
        print("\t좌표 이동 : ( %d, %d ) --> ( %d, %d )" % (old_x, old_y, new_x, new_y))
        print()


#############################################################################
## Main ##

print("좌표를 초기화합니다.")
while True:
    try:
        x = int(input("- X 좌표 : "))
    except:
        print("[Error] 정수만 입력 가능합니다.")
    else:
        break

while True:
    try:
        y = int(input("- Y 좌표 : "))
    except:
        print("[Error] 정수만 입력 가능합니다.")
    else:
        break

# New coordinate
coord = Point(x, y)

while True:
    print("-- Menu\t\t\t[메뉴 이름] . . . [선택 키]")
    print("--" * 15)
    print("X 좌표 설정\t . . . (x)")
    print("Y 좌표 설정\t . . . (y)")
    print("좌표 이동\t . . . (m)")
    print('--' * 15)
    print("좌표 설정 종료\t . . . (0)")
    print("==" * 15)
    print('\t' * 5, end='')
    menu = input("선택 :   ")

    if menu in ['X', 'x']:  # X 좌표 설정
        while True:
            try:
                new_x = int(input("새 X 좌표 입력 : "))
            except:
                print("정수만 입력하세요.")
            else:
                coord.setX(new_x)
                break

    elif menu in ['Y', 'y']:    # Y 좌표 설정
        while True:
            try:
                new_y = int(input("새 X 좌표 입력 : "))
            except:
                print("정수만 입력하세요.")
            else:
                coord.setY(new_y)
                break

    elif menu in ['M', 'm']:    # 좌표 이동
        while True:     # 새 X 좌표 입력
            try:
                new_x = int(input("새 X 좌표 입력 : "))
            except:
                print("정수만 입력하세요.")
            else:
                break

        while True:     # 새 Y 좌표 입력
            try:
                new_y = int(input("새 Y 좌표 입력 : "))
            except:
                print("정수만 입력하세요.")
            else:
                break

        coord.Move(new_x, new_y)

    elif menu == '0':   # 좌표 설정 종료
        print("좌표 설정 종료")
        print("좌표 설정됨 : ( %d, %d )" % (coord.getCoordinate()))
        break
    else:
        print("[System]\t Invalid menu\n")

result_message = "\t---------- Program Terminated ----------"
print(f"\n{result_message}")