class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        count = Counter(tasks)
        # Initialize a max heap with negative counts
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0  # Initialize time counter
        q = deque()  # Initialize a deque to track idle times
        while maxHeap or q:  # Continue until both maxHeap and deque are empty
            time += 1  # Increment time counter

            if not maxHeap:  # If maxHeap is empty, set time to next idle time
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)  # Pop the most frequent task
                if cnt:  # If count is nonzero, enqueue it with idle time
                    q.append([cnt, time + n])

            # Check if any tasks are ready to execute
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])  # Push task back to maxHeap

        return time  # Return total time elapsed