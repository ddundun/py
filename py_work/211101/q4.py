lcm=45
while lcm >= 0:
    lcm = lcm + 1
    if lcm % 6 == 0 and lcm % 45 ==0:
        break
print(lcm)