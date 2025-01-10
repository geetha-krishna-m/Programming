class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        m,n = len(words1),len(words2)
        min_RequiredFrequency = [0]*26
        res = []
        for i in range(n):
            c = [0]*26
            w, word = len(words2[i]),words2[i]
            for j in range(w):
                c[ord(word[j])-97] += 1
            for k in range(26):
                min_RequiredFrequency[k] = max(min_RequiredFrequency[k],c[k])     
        for i in range(m):
            c = [0]*26
            w, word = len(words1[i]),words1[i]
            for j in range(w):
                c[ord(word[j])-97] += 1
            k = 0
            while(k<26):
                if(min_RequiredFrequency[k] > c[k]):
                    break
                k = k + 1
            if(k==26):
                res.append(word)
        return res


            