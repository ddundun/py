# 1번문제
st = [1,2,3,4,5]
st[1:4]=[3]
print(st)

# 2번문제
st1 = [1,2,3,4,5,6,7,8,9,10]
st2= st1[0:10:2]
print(st2)

# 3번문제
st3 = [1,2,3,4,5,6,7,8,9,10]
st4= st3[1:10:2]
print(st4)

# 4번문제

def sum_all(st):
    sum=0
    for i in (st):
        sum+=i
    return sum

result= sum_all([1,2,3,4,5])
print(result)

# 5번문제

def show_reverse(st):
    for i in (st):
        print ((st)[-i])

show_reverse([1,2,3,4,5])

