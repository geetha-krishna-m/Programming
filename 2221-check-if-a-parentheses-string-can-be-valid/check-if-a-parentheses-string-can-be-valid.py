class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if(n%2):
            return False
        unlocked = []
        openb = []
        for i in range(n):
            if(locked[i]=='0'):
                unlocked.append(i)
            elif(s[i] == '('):
                openb.append(i)
            else:
                if(openb):
                    openb.pop()
                elif(unlocked):
                    unlocked.pop()
                else:
                    return False
        while(openb and unlocked and openb[-1]<unlocked[-1]):
            openb.pop()
            unlocked.pop()
        if(openb):
            return False
        return True