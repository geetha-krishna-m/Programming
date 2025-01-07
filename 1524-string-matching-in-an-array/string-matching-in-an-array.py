class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res,w = [],len(words)
        for i in range(w):
            for j in range(w):
                if words[i] in words[j] and i!=j:
                    res.append(words[i])
                    break
        return res