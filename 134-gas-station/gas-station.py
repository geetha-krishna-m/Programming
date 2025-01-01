class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sums = 0
        rest = 0
        n = len(gas)
        pos = 0
        for i in range(n):
            sums = sums + (gas[i]-cost[i])
            rest = rest + (gas[i]-cost[i])
            if(rest<0):
                rest = 0
                pos = (i + 1)%n
        if(sums>=0):
            return pos
        return -1
        