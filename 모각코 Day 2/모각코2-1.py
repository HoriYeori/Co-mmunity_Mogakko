num = float(input("숫자 입력 : "))
fn = lambda x: int(x) if x * 10 % 10 < 5 else int(x) + 1
print(fn(num))
