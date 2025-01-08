class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n, cnt = len(words), 0
        for i in range(n):
            for j in range(i+1,n):
                x = len(words[i])
                k = len(words[j])
                if(x<=k and words[j][:x] == words[i] and words[j][k-x:] == words[i]):
                    cnt +=1
        return cnt