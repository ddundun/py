alist = list(range(1,10))

print(alist)

btuple = tuple(range(10,1,-1))
print(btuple)

btuple=tuple(alist)

s1= str(btuple)
''' 문자열로 바꾸기 '''
print(s1)
print(type(s1))

for i in s1:
    print(i,end='')