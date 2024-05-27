class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        if 8 * children == money:
            return children

        money -= children

        if money < 7:
            return 0

        c = money // 7
        r = money % 7

        if r == 3 and c == children - 1:
            return children - 2
        
        return min (c, children -1)