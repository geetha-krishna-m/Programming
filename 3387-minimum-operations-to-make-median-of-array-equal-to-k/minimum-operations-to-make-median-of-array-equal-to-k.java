class Solution {
    public long minOperationsToMakeMedianK(int[] nums, int k) {
        Arrays.sort(nums);
        int mid = (int)nums.length/2;
        long cost = 0;
        if(nums[mid] == k){
            return 0;
        }
        else if(nums[mid] <k){
            while(mid<nums.length && nums[mid]<k){
                cost += k-nums[mid++];
            }
        }
        else{
            while(mid>-1 && nums[mid]>k){
                cost += nums[mid--]-k;
            }
        }
        return cost;
        
    }
}