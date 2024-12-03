class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        n, space_n = len(s), len(spaces)
        space_ind = 0
        for i in range(n):
            if(space_ind<space_n and i == spaces[space_ind]):
                res = res  +" "
                space_ind = space_ind + 1
            res = res + s[i]
        return res
            
