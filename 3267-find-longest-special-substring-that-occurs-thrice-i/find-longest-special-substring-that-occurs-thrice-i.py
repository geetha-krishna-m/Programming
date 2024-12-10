from collections import Counter
class Solution:
    def maximumLength(self, s: str) -> int:
        counter = defaultdict(int)
        n = len(s)
        for i in range(n):
            ind,temp = i,""
            while(ind<n and s[ind] == s[i]):
                temp = temp + s[ind]
                counter[temp] = counter.get(temp,0) + 1
                ind = ind + 1
        max_len = 0

        for j, n in counter.items():
            if n >= 3:
                if len(j) > max_len:
                    max_len = len(j)

        if max_len == 0:
            return -1
            
        return max_len
