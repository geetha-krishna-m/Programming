class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        res = 1
        while k * res < len(word):
            if word[res * k:] == word[:len(word) - res * k]:
                break
            res += 1
        return res