class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            j,k = 0,len(i)-1
            while(j<k):
                if i[j] != i[k]:
                    break
                j += 1
                k -= 1
            if(j>=k):
                return i
        return ""
            

