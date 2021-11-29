# a = [1,2,3,4]
#
# a.append('문자열')
# a.append(55)
#
# print(a)


b1= dict(a=44,b=22,c=33,d=11)

print(b1)
print(b1['a'])

for temp in b1.items():
    print(temp)

alist = sorted(b1.items(),key =lambda x: x[0]) #x의 0번째를 기준으로 정렬
print(alist)

blist = sorted(b1.items(),key =lambda x: x[1])
print(blist)

