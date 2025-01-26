class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        elif(x<10):
            return True
        else:
            temp,reverse_num = x,0
            while(temp>0):
                val = temp%10
                reverse_num = reverse_num*10 + val
                temp //= 10
            return reverse_num==x


        