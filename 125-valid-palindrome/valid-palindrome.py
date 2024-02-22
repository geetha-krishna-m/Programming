class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ""
        for i in s.lower():
            if (i>=chr(97) and i<=chr(122)) or (i>=chr(48) and i<=chr(57)):
                k += i
        if(k==k[::-1]):
            return True
        return False
                
        