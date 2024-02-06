class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        # Sort the time array in increasing order
        time.sort()
        
        # Initialize the variables
        n = len(time)
        l = 0
        r = time[n-1] * totalTrips
        
        # Binary search for the minimum time
        while l < r:
            mid = (l + r) // 2
            trips = 0
            
            # Count the number of trips that can be completed in mid time
            for i in range(n):
                trips += (mid // time[i])
                if trips >= totalTrips:
                    break
            
            # Adjust the search range
            if trips >= totalTrips:
                r = mid
            else:
                l = mid + 1
        
        # Return the minimum time
        return l