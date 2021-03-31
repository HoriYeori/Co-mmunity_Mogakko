## Problem
welcome_message = "★☆★ Drink Vending Machine ★☆★"
print(f"\n\t {welcome_message} \n")


## Business begin!
drinks = {'물': {'price': 700,
                'quantity' : 2},
          '콜라': {'price': 1000,
                 'quantity': 5,},
          '사이다': {'price': 1000,
                  'quantity': 0},
          '과일 주스': {'price': 800,
                    'quantity': 2}
          }

print('-' * 5 + " 음료수 목록 " + '-' * 5)
for drink in drinks:
    print(f"{drink:>8}\t{drinks[drink]['price']}원")
print('-' * 21)


## Get input
while True:     # 보유 현금 액수 입력
    try:
        print("보유 중인 금액을 입력해주세요")
        balance = int(input("보유 중인 금액 :\t"))
    except:
        print("유효한 수가 아닙니다. 다시 입력하세요.\n")
    else:
        break

# 희망 음료 입력
print("구매를 원하는 음료를 입력해주세요")
drink = input("음료 이름 :\t")
while drink not in drinks.keys():
    print("그런 음료는 없습니다. 음료 이름을 다시 정확하게 입력해주세요.")
    drink = input("음료 이름\t: ")


## Sale
if drinks[drink]['quantity'] == 0:  # 수량 부족
    print("현재 %s의 재고가 없습니다. 죄송합니다." % drink)
elif balance < drinks[drink]['price']:    # 잔액 부족
    print("잔액이 부족합니다. %d원 부족합니다." % (drinks[drink]['price'] - balance) )

else:
    drinks[drink]['quantity'] -= 1    # 수량 차감
    balance -= drinks[drink]['price'] # 잔액 차감
    print("%s 구매가 완료되었습니다. 감사합니다." % drink)
    print("잔액이 %d원 남았습니다." % balance)


result_message = "\t---------- 프로그램 종료 ----------"
print(f"\n{result_message}")