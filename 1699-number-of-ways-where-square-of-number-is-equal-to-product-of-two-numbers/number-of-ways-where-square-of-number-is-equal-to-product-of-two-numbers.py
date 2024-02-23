class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt = 0
        sums1,sums2 = dict(),dict()
        for i in nums1:
            sums1[i*i] = sums1.get(i*i,0)+1
        for i in nums2:
            sums2[i*i] = sums2.get(i*i,0)+1
        n = len(nums1)
        n2 = len(nums2)
        for i in range(n):
            prod = 1
            for j in range(i+1,n):
                prod = nums1[i] * nums1[j]
                if(prod in sums2):
                    cnt += sums2[prod]
                prod = 1
        
        for i in range(n2):
            prod = 1
            for j in range(i+1,n2):
                prod = prod * nums2[i] * nums2[j]
                if(prod in sums1):
                    cnt += sums1[prod]
                prod = 1
        return cnt