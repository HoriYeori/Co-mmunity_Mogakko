## Problem
welcome_message = "★☆★ Grade sudoku! ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input
board = []
for i in range(9):  # 스도쿠는 9x9
    line = input().split()
    board.append(line)


## Grade!
# Function declaration
def check_duplication(board, way):
    # 세로줄 중복 확인
    if way == "vertical":
        for col in range(9):    # 세로줄 한 줄씩
            vertical_line = set()
            for row in range(9):
                vertical_line.add(board[row][col])
            if len(vertical_line) < 9:  # 수의 개수가 9개 이하 = 중복 존재
                return False
    # 가로줄 중복 확인
    elif way == "horizontal":
        for row in range(9):    # 가로줄 한 줄씩
            horizontal_line = set()
            for col in range(9):
                horizontal_line.add(board[row][col])
            if len(horizontal_line) < 9:  # 수의 개수가 9개 이하 = 중복 존재
                return False

    # 3x3 부분 구역 중복 확인
    elif way == "partial":
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                partial_board = [ line[col:col+3] for line in board[row:row+3] ]    # 3x3 부분 구역 추출
                partial_set = set()

                # 부분 집합 별로 숫자 취합
                for line in partial_board:
                    for digit in line:
                        partial_set.add(digit)

                # 부분 집합 숫자 종합 끝, 중복 확인
                if len(partial_set) < 9:
                    return False

    # Invalid argument value
    else:
        print("invalid direction")
        return False
    return True


def GradeSudoku(board):
    # Check duplication in vertical/horizontal lines
    if not check_duplication(board, "vertical"):
        return False
    elif not check_duplication(board, "horizontal"):
        return False
    elif not check_duplication(board, "partial"):
        return False
    return True


if GradeSudoku(board):
    print("\t\t !!! 정답입니다 !!!")
else:
    print("\t\t ... 틀렸습니다 ...")

