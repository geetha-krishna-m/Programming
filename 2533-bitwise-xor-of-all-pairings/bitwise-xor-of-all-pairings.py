class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num1,num2 = 0,0
        m,n = len(nums1),len(nums2)
        if(n%2):
            for i in nums1:
                num1 ^= i
        if(m%2):
            for i in nums2:
                num2 ^= i
        return num1^num2
        

        