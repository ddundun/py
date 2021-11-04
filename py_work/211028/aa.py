class AA:
    def sum_all(self,alist):
        ''' self= this랑 사용방법 거의 동일(자동할당)'''
        # print(alist)
        sum=0
        for i in alist:
            sum=sum+i
        return sum

    def reverse(self,alist):
        temp =[]
        for i in range(len(alist)-1,-1,-1):
            '''4부터 0까지/ len길이: 5?'''
            temp.append(alist[i])
        return temp
