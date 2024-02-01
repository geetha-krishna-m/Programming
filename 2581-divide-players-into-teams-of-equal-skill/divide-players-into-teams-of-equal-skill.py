class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        prodSum,sums, prev = 0, 0, 0
        for i in range(n//2):
            sums = skill[i] + skill[n-i-1]
            if(sums!=prev and prev!=0):
                flag = -1
                return -1
            prev = sums
            prodSum += skill[i]*skill[n-i-1]
        if(sums!=prev):
            return -1
        else:
            return prodSum
            
                
            
        