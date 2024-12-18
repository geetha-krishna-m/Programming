class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for i in range(n):
            ind = i
            for j in range(i+1,n):
                if(prices[i]>=prices[j]):
                    ind = j
                    break
            if(ind!=i):
                prices[i] -= prices[ind]
        return prices
            

        