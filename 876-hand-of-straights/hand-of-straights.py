import collections
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        c = collections.Counter(hand)
        s = sorted(c)
        cnt, prev = c[s[0]],0
        for i in s:
            if(c[i]> len(hand) //groupSize):
                return False
            if c[i]>0:
                for k in range(1,groupSize):
                    if(i+k not in c):
                        return False
                    if (c[i+k]<c[i]):
                        return False
                    c[i+k] -= c[i]
        return True
            
                
