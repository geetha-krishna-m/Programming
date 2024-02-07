class Solution:
    def isHappy(self, n: int) -> bool:
        def find(num):
            squares = 0
            while(num!=0):
                squares += (num%10)**2
                num = num // 10
            return squares
        visited = set()
        while n!=1 and n not in visited:
            visited.add(n)
            n = find(n)
        return True if n ==1 else False