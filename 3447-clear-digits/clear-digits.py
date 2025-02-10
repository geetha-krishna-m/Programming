class Solution:
    def clearDigits(self, s: str) -> str:
        stack = list()
        for i in s:
            if(i.isdigit() and stack):
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
                
        