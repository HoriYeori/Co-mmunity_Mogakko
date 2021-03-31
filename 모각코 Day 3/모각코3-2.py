month = 3

print(f"\t\t    <{month}월 달력>")
print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % ("일", "월", "화", "수", "목", "금", "토"))

print("\t", end='')    # 시작점 맞추기
for day in range(1, 32):
    if day % 7 == 0:
        print("\n\n") # 다음 주
    print("%d\t" % day, end='')
