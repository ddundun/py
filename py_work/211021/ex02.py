from myfunc import doC
# doC()

'''
    자바에서는 문자열 + 숫자형이면
    자동으로 문자열 연산을 한다.
    하지만 파이썬에서는 문자열+숫자형이면
    cal only concatenate str (not "int") to str
    에러가 생긴다.
    따라서, 강제 형변환필요
'''

'''
    eval 함수는 문자열로 들어온걸 확인해서
    (1) 함수 호출이면 함수호출도 해주고 
    (2) 1+2 계산도 해줌
    (3) 숫자가 들어왔으면 숫자 타입으로 변경
    
    단축키
    ctrl +z 뒤로가기
    ctrl +y 앞으로가기
'''
str = input("뭐든 넣어요")
result =eval(str)
print(result)

# result= eval(input("뭐든넣어요"))
# print(result)