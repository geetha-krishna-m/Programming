class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = list(heights)
        heights.sort()
        cnt = len(heights)
        for i in range(len(heights)):
            if(heights[i] == expected[i]):
                cnt -= 1
        return cnt
        