class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        cnt = 0
        for i in range(len(seats)):
            if(seats[i] == students[i]):
                continue
            else:
                cnt += abs(students[i] - seats[i])
        return cnt
        