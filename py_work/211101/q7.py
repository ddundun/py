num=2
while num<100:
    num=num+1
    if num%2==0 and num%3==0:
        continue
    if num%2!=0 and num%3!=0:
        print(num, end=' ')