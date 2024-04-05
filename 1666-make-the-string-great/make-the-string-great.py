class Solution:
    def makeGood(self, s: str) -> str:
        def good(s):
            temp = ""
            for i in range(len(s)-1):
                if(ord(s[i])-97==ord(s[i+1])-65 or ((ord(s[i])-65) == (ord(s[i+1])-97))):
                    return False
            return True
        temp = s
        while(not good(temp)):
            for i in range(len(s)-1):
                if((ord(s[i])-97) == (ord(s[i+1])-65) or ((ord(s[i])-65) == (ord(s[i+1])-97))):
                    
                    temp = s[:i] + s[i+2:]
                    break
            s = temp
        return temp

        