class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if(n<3):
            return False
        cnt = 0
        for i in range(len(arr)):
            if(arr[i] & 1 == 1):
                cnt = cnt + 1
            else:
                cnt = 0
            if(cnt == 3):
                return True
        return False
            
        