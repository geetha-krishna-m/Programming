class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Initialize an array to store the minimum prices to reach each city
        prices = [float("inf")] * n
        # Set the price to reach the source city to 0
        prices[src] = 0

        # Iterate through k + 1 iterations to consider up to k stops
        for i in range(k + 1):
            # Create a copy of the current prices array
            tmpPrices = prices.copy()

            # Iterate through each flight
            for s, d, p in flights:  # s=source, d=destination, p=price
                # Check if there's a flight from the source city and the price to reach it is not infinity
                if prices[s] == float("inf"):
                    continue
                # Update the temporary prices array if the new price is cheaper
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            # Update the prices array with the values from the temporary prices array
            prices = tmpPrices

        # If the price to reach the destination city is still infinity, return -1; otherwise, return the price
        return -1 if prices[dst] == float("inf") else prices[dst]