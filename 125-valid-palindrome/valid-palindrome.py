class Solution:
    @cache
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        n = len(s)
        for i in range(n):
            if(s[i]!=s[n-i-1]):
                return False
        return True
                
        