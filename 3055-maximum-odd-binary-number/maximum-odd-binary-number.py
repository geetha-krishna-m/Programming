class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt_1 = 0
        for i in s:
            if i == '1':
                cnt_1 += 1
        res = ''
        for i in range(cnt_1-1):
            res += '1'
        for i in range(len(s)-cnt_1):
            res += '0'
        res += '1'
        return res