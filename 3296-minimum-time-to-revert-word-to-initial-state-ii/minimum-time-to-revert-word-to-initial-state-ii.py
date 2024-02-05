class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        res = 1
        n = len(word)
        while(res*k<n):
            if(word[res*k:] == word [:n-res*k]):
                break
            res += 1
        return res