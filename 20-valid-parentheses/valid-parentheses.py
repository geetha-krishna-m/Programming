class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        n = len(s)
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i)
            else:
                if(stack):
                    if((i==')' and stack[-1]=='(') or (i=='}' and stack[-1]=='{') or (i==']' and stack[-1]=='[')):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if(len(stack)):
            return False
        return True

        