class Solution:
    def kthCharacter(self, k: int) -> str:
        word  = "a"
        def recurse(word):
            n = len(word)
            if(n >= k):
                return word[k-1]
            for i in range(n):
                word = word + chr(ord(word[i])+1)
            return recurse(word)
        return recurse(word)

        