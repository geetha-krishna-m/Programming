class Solution {
    public int countSeniors(String[] details) {
        int ageAboveSixty = 0;
        for(String s:details)
        {
            
            int tens = (s.charAt(11)- '0');
            int units = (s.charAt(12)-'0');
            if( (tens*10+units)>60 ){
                        ageAboveSixty += 1;
            }  
        }
        return ageAboveSixty;
    }
}