class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        for j in range(k, n, k):
            for i in range(n - j):
                if word[i] != word[i + j]:
                    break
            else:
                return j // k
        return (n + k - 1) // k