class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        d = dict()
        for i in range(n):
            v=set()
            for j in words[i]:
                if j not in v:
                    v.add(j)
            d[i]=v
        lis = d.keys()
        cnt  = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if(d[i] == d[j]):
                    cnt +=1
        return cnt
                
            
        