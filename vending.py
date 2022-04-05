from secrets import choice


def banding_machine():
    budget=int(input('금액을 넣어주세요: '))
    
    while True:
        lists = {'Prince':500,"Zebra":100,'Crown':300,'Unicorn':400}
        goods = list(lists.keys())
        price = list(lists.values())

        print("[나경's 보물상자]")
        print('현재 금액 : ', budget, '원')

        for i in range(len(goods)):
            print(i+1, ". ", goods[i], " - ", price[i], "원")

        choice = int(input('Choose the product: ')) - 1

        exchange = budget-price[choice]
        if exchange<0:
            print('금액이 부족합니다.')
            break
        elif exchange == 0:
            print('잔액은 ', exchange, '원입니다. 이용해주셔서 감사합니다.')
            break
        else:
            print('잔액은 ', exchange, '원입니다.')
            ask = input('추가로 구매하시겠습니까?(Y/N): ')

            if ask == 'Y':
                budget=exchange
                continue
            else:
                break

banding_machine()