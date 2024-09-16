class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        target = 9
        two numbers: a, b with indices i,j
        find (i,j) pair such a+b = target 
        i!=j
        """
        indicesMap = dict()
        for ind,val in enumerate(nums):
            indicesMap[val] = ind
        for ind,val in enumerate(nums):   
            secondVal = target - val
            if(secondVal in indicesMap and ind!=indicesMap[secondVal]):
                return [ind,indicesMap[secondVal]]
        return [-1,-1]

        


        