class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # l = []
        # cnt = 0
        # for i in range(len(s)):
        #     if(s[i]!=')' and s[i]!='('):
        #         l.append(s[i])
        #     elif(s[i]=='('):
        #         l.append(s[i])
        #         cnt += 1
        #     elif(s[i]==')' and cnt>0):
        #         l.append(s[i])
        #         cnt -= 1
        # if(cnt == 0):
        #     return "".join(l)
        # else:
        #     for i in range(len(l)-1,-1,-1):
        #         if(l[i]=='('):
        #             l[i] = ''
        #             cnt -= 1
        #         if(cnt == 0):
        #             break
        #     return "".join(l)
        """
Given a string s that contains parentheses, remove the minimum number
of parens to make it valid, where each paren has a matching pair.

Example:

Test case:
    "a)b(cd"
    stack = [2]
    result = [a, b, "", c, d]

    a)e)
    
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack: List[int] = []
        result: List[str] = []
        for c in s:
            if c == '(':
                stack.append(len(result))
                result.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                    result.append(c)
            else:
                result.append(c)
        
        for i in stack:
            result[i] = ''
        
        return ''.join(result)