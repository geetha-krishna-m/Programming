class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rotations = 0
        while(len(sandwiches)):
            if(rotations == len(students)):
                break
            if(sandwiches[0] == students[0]):
                sandwiches.pop(0)
                students.pop(0)
                rotations = 0    
            else:
                students.append(students.pop(0))
                rotations += 1
        return len(sandwiches)  