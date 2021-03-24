def sum_digits(num):
    total = 0
    while num:
        total += num % 10
        num //= 10
    return total


nums = list(map(int, input("숫자 입력(공백으로 구분) : ").split()))
ans = list(map(sum_digits, nums))
print(nums[ans.index(max(ans))])
