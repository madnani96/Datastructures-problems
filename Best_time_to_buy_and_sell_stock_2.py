#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

def maxProfit(prices):
        profit = 0
        length = len(prices)
        for x in range(1,length):
            if prices[x]>prices[x-1]:
                profit+=prices[x]-prices[x-1]
        return profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))