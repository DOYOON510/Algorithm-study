import sys

    def temp():
    sys.stdin = open("input.txt", "r")

    T = int(input())
    for test_case in range(1, T + 1):
        n=int(input())
        price = list(map(int,input().split()))
        result=0
        max_price=0
        for i in range(len(price)-1,-1,-1):
            if max_price < price[i]:
                max_price=price[i]
            else:
                result+= max_price-price[i]
        print('#{} {}'.format(test_case,result))

def main():
    # 메인 함수의 코드를 여기에 작성하세요.
    print("안녕하세요, 파이참!")
    temp()


if __name__ == '__main__':
    main()


