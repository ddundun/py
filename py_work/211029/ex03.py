# while 루프 사용

# 홀수만 출력하면서 continue를 사용해야함
# 100보다 큰 홀 수일때는 break
# 1, 3, 5, 7, 9, 11, 13
i = 0
while True:
    i = i+1
    if i%2 ==0:
        continue
    if i>100:
        break
    print(i, end=" ")
