# 1 + 2 + 3 + 4 + 5 = 15
# 함수 파라메타의 기본값을 지정하는 문법
def main(a): # 함수의 정의
#   main(a=5)하면 밑에 main에 값 안넣어줘도됨
    sum = 0
    for i in range(1,a+1):
        sum= sum+i
    print("sum= ",sum,end='')

main(5)