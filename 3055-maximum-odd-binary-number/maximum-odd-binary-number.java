class Solution {
    public String maximumOddBinaryNumber(String s) 
    {
        int cnt_1 = 0;
        char res[] = s.toCharArray();
        for(int i=0;i<s.length();i++)
        {
            if(res[i] == '1'){
                cnt_1++;
            }
        }
        for(int i=0;i<cnt_1-1;i++){
            res[i] = '1';
        }
        for(int i=cnt_1-1;i<s.length()-1;i++){
            res[i] = '0';
        }
        res[s.length()-1] = '1';
        return String.valueOf(res);
    }
}