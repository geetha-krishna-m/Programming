class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1 = [int(i) for i in bin(num1)[2:]]
        num2 = [int(i) for i in bin(num2)[2:]]
        m,n = len(num1),len(num2)
        num1 =  [0]*(31-m) + num1 
        num2 = [0]*(31-n) + num2
        def getCount(num):
            cnt = 0
            for i in num:
                if(i):
                    cnt += 1
            return cnt
        cnt_1,cnt_2 = getCount(num1),getCount(num2)
        x = num1
        if(cnt_1<=cnt_2):
            k =cnt_2-cnt_1
            print(k)
            for i in range(30,-1,-1):
                print(x,k,i)
                if(k == 0):
                    break
                if(x[i] == 0):
                    x[i] = 1
                    k -= 1
        else:
            k = cnt_1-cnt_2
            for i in range(30,-1,-1):
                if(k==0):
                    break
                if(x[i] == 1):
                    x[i] = 0
                    k -= 1
        sums = 0
        for i in range(31):
            sums = sums + (2**i)*x[30-i]
        return sums





        
            

        