class Solution {
    public int maxDepth(String s) 
    {
       int cnt =0,maxy = 0;
       for(Character c:s.toCharArray()){
        if(c == '('){
            cnt++;
        }
        if(c == ')'){
            cnt--;
        }
        maxy = maxy > cnt ? maxy : cnt;
       }
       return maxy;   
    }
}