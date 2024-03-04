class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        if(n == 0):
            return 0
        tokens.sort()
        maxy = 0
        score = 0
        while(len(tokens)>0 and (power>=tokens[0] or score>0)):
            if(power>=tokens[0]):
                power -= tokens[0]
                score += 1
                tokens.pop(0)
            else:
                score -= 1
                power += tokens[-1]
                tokens.pop(-1)
            maxy = max(score,maxy)
        return maxy
        
            
            


        