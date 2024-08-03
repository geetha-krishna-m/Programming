class Solution {
    public int minSwaps(int[] nums) {
        int k = (int)Arrays.stream(nums).filter(num -> num == 1).count();
        int count = (int)Arrays.stream(nums,0,k).filter(num -> num == 1).count();
        int swaps = k-count;
        int n = nums.length,dummy=swaps;
        for(int i=k;i<n+k;i++){
            if(nums[i%n] == 1){
                dummy -= 1;
            }
            if(nums[(i-k+n)%n] == 1){
                dummy += 1;
            }
            swaps = swaps<dummy?swaps:dummy;
        }
        return swaps;
    }

}