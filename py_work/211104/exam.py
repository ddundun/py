
class Exam:
    '''
    9에서부터 값을 하나씩 감소시키며 0까지 출력을 보이는 코드를 while 루프를 기반으로 작성해보자.
    '''
    def doTwo(self):
        cnt=9
        while True:
            print("cnt",cnt)
            cnt -=1
            if cnt ==0:
                break
    def doThree(self):
        num =1
        while True:
            num +=1
            if 3*num/2 ==63:
                break
        print("num",num)

    def doFour(self):
        lcm=45
        while True:
            if (lcm %6 ==0) and (lcm %45 )==0:
                break
            lcm +=1
        print("최소공배수 = ",lcm)

    def doFive(self):
        gcm=42
        while True:
            if 42% gcm==0 and 120% gcm  ==0:
                break
            else: gcm -=1
        print("최대 공약수 = ",gcm)

    def doSix(self):

        for i in range(1, 10):
            if (7 * i) % 2 == 0:
                print(7 * i, end=' ')
            else:
                continue

    def doSeven(self):
        num = 2  # 2~100
        while True:
            num += 1
            if num % 2 != 0 and num % 3 != 0:
                print(num, end=' ')
            if num > 100:
                break


