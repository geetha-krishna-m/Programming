class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = dict()
        for i in words[0]:
            d[i] = d.get(i,0) + 1
        for i in range(1,len(words)):
            for k in d:
                if k not in words[i]:
                    d[k] = 0
                else:
                    d[k] = min(d[k],words[i].count(k))
        res=[]
        for i in d:
            for k in range(d[i]):
                res.append(i)
        return res        