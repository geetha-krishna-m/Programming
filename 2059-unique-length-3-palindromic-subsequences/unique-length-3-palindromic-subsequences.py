class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hashSet = set()
        n = len(s)
        hashMap,lastMap,cnt = dict(),dict(),0
        for i in range(n):
            if(s[i] not in hashMap):
                hashMap[s[i]] = i
                continue
            lastMap[s[i]] = i
        for i in range(26):
            char = chr(97+i)
            if(char  in hashMap and  char in lastMap):
                l,r = hashMap[char],lastMap[char]
                hashSet = set()
                for j in range(l+1,r):
                    hashSet.add(s[j])
                cnt += len(hashSet)
        return cnt


            

        