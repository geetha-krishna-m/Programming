class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1) & set(nums2)
        if nums1:
            return min(nums1)
        else:
            return -1
        