height = int(input("삼각형 높이 : "))

for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * i)
