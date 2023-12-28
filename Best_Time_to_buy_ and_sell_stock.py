def maxProfit( prices):
        profit = 0
        minimumprice = prices[0]
        length = len(prices)
        for x in range(1, length):
            if prices[x]>minimumprice:
                profit = max(prices[x] - minimumprice, profit)  
            if prices[x]<minimumprice:
                    minimumprice = prices[x]
        return profit

prices= [7,1,5,3,6,4]
print(maxProfit(prices))