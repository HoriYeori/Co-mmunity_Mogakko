## Problem
welcome_message = "★☆★ Movie Reservation Program ★☆★"
print(f"\n\t {welcome_message} \n")


# Preparation
def getInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print("유효하지 않은 입력입니다. 정수 범위의 숫자만 입력하세요.")
        else:
            return num


class Theater():
    ## Variables
    movies = ["자산어보",
              "아무도 없는 곳",
              "조제, 호랑이 그리고 물고기들",
              "고질라 VS. 콩",
              "극장판 귀멸의 칼날: 무한열차편",
              "패왕별희 디 오리지널",
              "미나리",
              "디 아더 사이드",
              "해길랍",
              "커피 오어 티"]

    discounts = {"학생할인": 3000,
                 "지역할인": 4000,
                 "회원할인": 5000}

    price = 12000

    ## Functions
    # Constructor
    def __init__(self):
        pass

    def AskMovie(self):
        print("[System]\t관람하실 영화의 제목을 입력해주세요.")
        movie = input("\t\t영화 제목 :\t")
        while movie not in self.movies:
            print("\t해당 제목의 영화가 상영 중이지 않습니다. 다시 입력해주세요.")
            movie = input("\t\t영화 제목 :\t")

        return movie

    def AskNumber(self):
        print("[System]\t관람하는 인원수를 입력해주세요.")
        message = "\t\t관람 인원수 :\t"
        nPerson = getInt(message)
        while nPerson < 1:
            print("\t1명 이상 관람해야 합니다.")
            nPerson = getInt(message)

        return nPerson

    def AskDiscount(self):
        print("[System]\t사용하실 할인권 이름을 입력해주세요.")
        voucher = input("\t\t할인권 이름 :\t")
        while voucher not in list(self.discounts.keys()):
            print("\t해당하는 할인권이 존재하지 않습니다.")
            print("\t할인권 목록 :")
            print("\t\t" + ' / '.join(list(self.discounts.keys() ) ) )
            print("\t할인권을 다시 입력하시겠습니까?")
            answer = input("\t다시 입력 (Y) / 할인권 입력 취소 (N) :\t")
            while answer not in ['Y', 'y', 'N', 'n']:
                print("유효하지 않은 입력입니다. 다시 입력하세요.")
                answer = input("\t다시 입력 (Y) / 할인권 입력 취소 (N) :\t")

            if answer in ['Y', 'y']:
                voucher = input("\t\t할인권 이름 :\t")
            elif answer in ['N', 'n']:
                print("\t할인권 입력 취소")
                voucher = ''
                break
        return voucher

    def Reservation(self):
        ticket = {"movie": '',
                  "nPerson": 0,
                  "discount": 0,
                  "price": 0}

        # 영화 선택
        movie = self.AskMovie()
        print(f"[System]\t[ {movie} ] 을(를) 선택하셨습니다.")

        # 관람 인원 수 선택
        nPerson = self.AskNumber()
        print(f"[System]\t총 {nPerson} 명 관람")

        # 할인권 사용 여부 선택
        print("[System]\t할인권을 사용하시겠습니까? (할인권 사용 또는 금액 확인 화면으로 이동)")
        answer = input("\t할인권 사용 (Y) / 사용하지 않음(금액 확인) (N) :\t")
        while answer not in ['Y', 'y', 'N', 'n']:
            print("유효하지 않은 입력입니다. 다시 입력하세요.")
            answer = input("\t할인권 사용 (Y) / 사용하지 않음(최종 결제 금액 확인) (N) :\t")

        if answer in ['Y', 'y']:
            voucher = self.AskDiscount()
            if voucher != '':
                discount = self.discounts[voucher]
                print(f"[System]\t[ {voucher} ] 할인권이 적용되어 인당 [ {discount} ] 원이 할인됩니다.")
            else:
                print("[System]\t할인권을 사용하지 않습니다.")
                discount = 0
        elif answer in ['N', 'n']:
            print("[System]\t할인권을 사용하지 않습니다.")
            discount = 0

        # 티켓 예매
        ticket['movie'] = movie
        ticket['nPerson'] = nPerson
        ticket['discount'] = discount * nPerson
        ticket['price'] = self.price * nPerson
        return ticket


## Get input
megabox = Theater()

print("{:^43}".format("- BOXOFFICE TOP 10 -"))
print("=-=" * 5 + " Now Showing " + "=-=" * 5)
for idx, movie in enumerate(megabox.movies):
    print(f"\t{idx+1}.\t{movie}")
print("=-=" * 7 + '~' + "=-=" * 7)
print("\n")

ticket = megabox.Reservation()


## Reserved!
print("\t예매가 완료되었습니다.\n")
print("\t< 예매 내역 >")
print("==" * 20)
print(f"\t영화 제목:\t{ticket['movie']}")
print(f"\t관람 인원:\t{ticket['nPerson']}")
print(f"\t총 결제 금액:\t{ticket['price']}")
print(f"\t할인 금액:\t{ticket['discount']}")
print("--" * 20, end='\n\n')

total = ticket['price'] - ticket['discount']
print(f"\t\t최종 결제 금액:\t{total}")
print("==" * 20)

result_message = "--" * 10 + " 영화 예매 종료 " + "--" * 10
print(f"\n\t{result_message}")