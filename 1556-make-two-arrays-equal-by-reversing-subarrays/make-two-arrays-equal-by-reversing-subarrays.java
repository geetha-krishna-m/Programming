class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        int t_len = target.length, a_len = arr.length;
        if(t_len != a_len){
            return false;
        }
        Map<Integer,Integer> map = new HashMap<>();
        for(int i:target){
          map.put(i,map.getOrDefault(i,0)+1);
        }
        for(int i:arr){
            if(!map.containsKey(i) || (map.get(i)<=0)){
                return false;
            }
            else{
                map.put(i,map.get(i)-1);
            }
        }
        return true;  
    }
}