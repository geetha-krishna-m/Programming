class Solution {
    public int minimumPushes(String word) {
        int arr[] = new int[26];
        for(Character c:word.toCharArray()){
            arr[c-'a']++;
        }
        int cost = 1,totalCost = 0,rounds=0,maximum = -9999,index = -1;
        while(maximum != 0){
            index = -1;
            maximum = -9999;
            for(int i=0;i<26;i++)
            {
                if(arr[i]>maximum){
                    maximum = arr[i];
                    index = i;
                }
            }
            rounds++;
            totalCost += cost*arr[index]; 
            arr[index] =  0;
            if(rounds%8==0)
                 cost++;
            
        }
        return totalCost;
        
    }
}