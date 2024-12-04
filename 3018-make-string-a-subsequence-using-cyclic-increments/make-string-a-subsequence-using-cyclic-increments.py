class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s1,s2 = len(str1),len(str2)
        i,j=0,0
        while(i<s1 and j<s2):
            source,target = ord(str1[i]),ord(str2[j])
            if((target-source)%26 <= 1):
                j = j + 1
                if(j == s2):
                    return True
            i = i+1
        return False