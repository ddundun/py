def dan7(dan):
    for i in range(1,10):
        print(dan,"*",i,"=",dan*i)

def dan7reverse(dan):
    for i in range(9,0,-1):
        print(dan,"*",i,"=",dan*i)

def exp(a,b):
        result = 1
        for i in range(b):
            result= result*a
        return result

def greet():
    i = eval(input("몇번씩 인사할까요?"))
    for _ in range(i):
        # 몇번씩하는지알라고..?
        print("반갑습니다.")