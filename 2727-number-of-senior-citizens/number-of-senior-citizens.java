class Solution {
    public int countSeniors(String[] details) {
        int ageAboveSixty = 0;
        for(String s:details)
        {
            char characters[] = s.toCharArray();
            int tens = (characters[11] - '0');
            int units = (characters[12]-'0');
            if( (tens*10+units)>60 ){
                        ageAboveSixty += 1;
            }  
        }
        return ageAboveSixty;
    }
}