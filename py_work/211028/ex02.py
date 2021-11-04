
alist = []
# alist는 list당
for i in range(1,11,1):
    alist.append(i)
print(alist)

# 여기까지는 추가하는 것

for i in range(9,-1,-1):
    print("alist.pop(",i,")",alist.pop(i))
print("alist= ",alist)