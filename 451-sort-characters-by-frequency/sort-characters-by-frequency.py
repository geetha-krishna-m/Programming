class Solution:
    def frequencySort(self, s: str) -> str:
        d = dict()
        for i in s:
            d[i] = d.get(i,0) + 1
        keys_ = sorted(d.keys(),key = lambda x:d[x],reverse = True)
        s = ""
        for i in keys_:
            s += i*d[i]
        return s
        