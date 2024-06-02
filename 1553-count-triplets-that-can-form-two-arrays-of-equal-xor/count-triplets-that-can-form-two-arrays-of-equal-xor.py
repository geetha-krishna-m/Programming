class Solution:
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        count = 0
        prefixXOR = [0] * (n + 1)
        
        for i in range(n):
            prefixXOR[i+1] = prefixXOR[i] ^ arr[i]
        """
        prefix array has 0 at the very first index in this solution so we are using j+1 to check in prefix array so no worries
        checking with (j+1) because here we need xor from (j to k) i.e., y and (i to j-1) is already precomputed so we use prefix at i compare to the prefix at j+2


        In short at prefix[i] we have required computed so far xor of a and 
        to find b we remove a from i to k which gives j to k. but instead of using another loop for j we came to know that number of pairs (j,k) w.r.to i can be included in result if the prefix at k is equal to prefix at i if so all the elements b/w i to k are responsible for the result too.
        """
        for i in range(n):
            for j in range(i + 1, n):
                if (prefixXOR[i] == prefixXOR[j+1]):
                    count += j - i
        
        return count