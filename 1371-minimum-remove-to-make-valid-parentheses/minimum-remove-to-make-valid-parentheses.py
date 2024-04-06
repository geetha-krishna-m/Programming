class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = []
        cnt = 0
        for i in range(len(s)):
            if(s[i]!=')' and s[i]!='('):
                l.append(s[i])
            elif(s[i]=='('):
                l.append(s[i])
                cnt += 1
            elif(s[i]==')' and cnt>0):
                l.append(s[i])
                cnt -= 1
        if(cnt == 0):
            return "".join(l)
        else:
            for i in range(len(l)-1,-1,-1):
                if(l[i]=='('):
                    l[i] = ''
                    cnt -= 1
                if(cnt == 0):
                    break
            return "".join(l)

