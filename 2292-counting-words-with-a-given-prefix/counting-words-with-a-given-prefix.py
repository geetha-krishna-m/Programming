class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for word in words:
            m,j = len(pref),0
            if(len(word)<m):
                continue
            while(j<m):
                if(word[j]!=pref[j]):
                    break
                j = j + 1
            if(j == m):
                cnt = cnt + 1
        return cnt
        