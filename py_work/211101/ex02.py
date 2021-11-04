'''
tuple = immutable = 불변적인
list =  mutable
'''

alist= [1,2,3]
btuple=(1,2,3)

for i in alist:
    print("alist i = ",i)

for i in btuple:
    print("btuple i = ",i)

alist[1] =5
print(alist)

# btuple[1] = 5 -> 이거 주석처리안하면 오류뜸
# print(btuple) -> tuple은 변할수없음.