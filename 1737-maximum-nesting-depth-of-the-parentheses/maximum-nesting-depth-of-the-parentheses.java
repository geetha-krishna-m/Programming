class Solution {
    public int maxDepth(String s) 
    {
       int cnt =0,maxy = 0;
       for(Character c:s.toCharArray()){
        if(c == '('){
            cnt += 1;
        }
        if(c == ')'){
            cnt -= 1;
        }
        maxy = maxy > cnt ? maxy : cnt;
       }
       return maxy;   
    }
}