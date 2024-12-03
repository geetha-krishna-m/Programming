class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # res = ""  # time consuming since each concatenation creates new string object
        res = []
        n, space_n = len(s), len(spaces)
        space_ind = 0
        for i in range(n):
            if(space_ind<space_n and i == spaces[space_ind]):
                res.append(" ")
                space_ind = space_ind + 1
            res.append(s[i])
        return ''.join(res)