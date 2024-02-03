class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        dummy = [12,123,1234,12345,123456,1234567,12345678,123456789]
        n,k = len(dummy),11
        res = []
        for i in range(n):
            news = dummy[i]
            for j in range(n-i):
                if(news >= low and news <= high):
                    res.append(news)
                news += k
            k = k * 10 + 1
        return res
        