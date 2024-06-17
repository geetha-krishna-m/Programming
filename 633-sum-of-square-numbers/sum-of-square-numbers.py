class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5)+1):
            rest = c - (a**2)
            low, high = 0, int(c**0.5)+1
            while low <= high:
                mid = low + (high - low) // 2
                if mid**2 == rest:
                    print(rest)
                    return True
                elif mid**2 < rest:
                    low = mid + 1
                else:
                    high = mid - 1
        return False