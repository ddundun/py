def greet():
    str = input("인사를 몇번할까요?")
    result = eval(str)
    for i in range(result):
        print("반갑습니다.")

greet()