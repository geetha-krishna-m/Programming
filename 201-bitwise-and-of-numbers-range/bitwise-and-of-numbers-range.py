class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        sleft,sright = left,right
        cnt = 0
        while(sleft!=sright):
            sleft >>= 1
            sright >>=1
            cnt += 1
        sleft <<= cnt
        return sleft
        