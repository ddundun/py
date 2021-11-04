def doA():
    return 10,20,30
# (10,20)이던지 10,20이던지 tuple적용.
# tuple: 오로지 파이썬에서만 tuple이용해서 return값 여러개가능.
a,b,c = doA()
print("a= ",a, "b= ",b,"b= ",c)