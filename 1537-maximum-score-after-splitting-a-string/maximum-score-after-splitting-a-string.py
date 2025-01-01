class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        count_0,count_1,maxy,n = [0]*n,[0]*n,0,len(s)
        for i in range(n):
            if(i>0):
                count_0[i] = count_0[i-1]
                count_1[n-i-1] = count_1[n-i]
            if(s[i] == '0'):
                if(i==0):
                    count_0[i] = 1
                else:
                    count_0[i] += 1
            if(s[n-i-1]=='1'):
                if(i==0):
                    count_1[n-i-1] = 1
                else:
                    count_1[n-i-1] += 1

        for i in range(n-1):
            maxy = max(count_0[i]+count_1[i+1],maxy)
        return maxy