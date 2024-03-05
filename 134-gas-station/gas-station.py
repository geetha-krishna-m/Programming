class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sums = 0
        rest = 0
        pos = 0
        for i in range(len(cost)):
            diff = gas[i] - cost[i]
            sums += diff
            rest += diff
            if(rest<0):
                rest = 0
                pos = i + 1
        return pos if sums>=0 else -1

        