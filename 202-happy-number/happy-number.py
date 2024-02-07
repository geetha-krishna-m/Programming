class Solution:
    def isHappy(self, n: int) -> bool:
        def find(num,squares):
            while(num!=0):
                squares += (num%10)**2
                num = num // 10
            return squares
        if(n==1):
            return True
        slow,fast = find(n,0),find(find(n,0),0)
        if slow == 1:
            return True
        while(slow!=fast):
            slow = find(slow,0)
            fast = find(find(fast,0),0)
        return slow==1