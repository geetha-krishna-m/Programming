class Solution:
    def isHappy(self, n: int) -> bool:
        def find(num):
            squares = 0
            while(num!=0):
                squares += (num%10)**2
                num = num // 10
            return squares
        visited = set()
        while True:
            if n==1:
                return True
            if n in visited:
                return False
            visited.add(n)
            n = find(n)
        return False

        

        