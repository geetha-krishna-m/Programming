class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i)
            else:
                if(len(stack)):
                    if(i==')' and stack[-1]!='('):
                        return False
                    elif(i=='}' and stack[-1]!='{'):
                        return False
                    elif(i==']' and stack[-1]!='['):
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if(len(stack)):
            return False
        return True
