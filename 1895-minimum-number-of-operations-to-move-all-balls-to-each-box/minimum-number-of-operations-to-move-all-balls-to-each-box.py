class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        moves_left,balls_left = 0,0
        moves_right,balls_right = 0,0
        n = len(boxes)
        res = [0]*n
        for i in range(n):
            res[i] += moves_left
            balls_left += int(boxes[i])
            moves_left += balls_left
            
            res[n-1-i] += moves_right
            balls_right += int(boxes[n-1-i])
            moves_right += balls_right
        return res

        