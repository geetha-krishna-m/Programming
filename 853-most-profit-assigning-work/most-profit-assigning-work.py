class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diffprofit = [(difficulty[i],profit[i]) for i in range(len(difficulty))]
        diffprofit.sort()
        worker.sort()
        j,profit,maxProfit = 0,0,0
        for i in range(len(worker)):
            while(j<len(diffprofit) and worker[i]>=diffprofit[j][0]):
                
                maxProfit = max(diffprofit[j][1],maxProfit)
                print(maxProfit)
                j += 1
            profit += maxProfit
        return profit

        