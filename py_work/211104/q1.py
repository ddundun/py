# a= range(1,10,1)
# alist = list(a)
# print(alist)
# atuple = tuple(a)
# print(atuple)
def to_list(a):
   return list(a)

ds = (1,2,3)
ds = to_list(ds)
print(ds)

ds2 = "hello"
ds2 = to_list(ds2)
print(ds2)


