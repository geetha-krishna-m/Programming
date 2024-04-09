class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt=0
        while(tickets[k]!=0):
            i=0
            while(i<len(tickets)):
                if tickets[k]>0  and tickets[i]>0:
                    tickets[i]-=1
                    cnt+=1
                i+=1
        return cnt