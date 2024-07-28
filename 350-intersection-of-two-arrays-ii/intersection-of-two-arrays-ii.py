class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n = len(nums1),len(nums2)
        d_m, d_n = dict(),dict()
        for i in nums1:
            d_m[i] = d_m.get(i,0) + 1
        for i in nums2:
            d_n[i] = d_n.get(i,0) + 1
        res = []
        for i in set(nums1):
            if(i in d_n):
                for k in range(min(d_n[i],d_m[i])):
                    res.append(i)
        return res