def main():
    a= eval(input("숫자 입력하세요"))
    b= int(input("몇번 곱하겠?"))
    sum=1

    if type(a)==int:
        for i in range(1,b+1):
            sum=sum*a
            print(sum, end= ' ')
    elif not type(a) == int:
        print("정수가 아닙니다.")



main()