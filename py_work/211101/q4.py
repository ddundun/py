lcm=45
while True:
    lcm = lcm + 1
    if lcm % 6 == 0 and lcm % 45 ==0:
        break
print(lcm)