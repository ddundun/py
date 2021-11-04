def so_simple(st):
    print(st)

def so_simple2(st):
    return st+[1,2,3]
# 반환도 가능

# 파이썬에선 int같은 자료형 선언안해도 알아서 사용가능
so_simple([1,2,3,4,5])
so_simple("abcdef")
so_simple(1.5)

print(so_simple2([1,2,3]))