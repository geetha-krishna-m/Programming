class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        sums = 0 
        banned = set(banned)
        cnt = 0
        for i in range(1,n+1):
            if(i not in banned):
                sums = sums + i
                if(sums>maxSum):
                    return cnt
                cnt = cnt + 1
        return cnt