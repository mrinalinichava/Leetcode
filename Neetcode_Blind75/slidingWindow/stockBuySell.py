'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example-1:
Input: prices = [7,1,5,3,6,4]
Output: 5
'''

def maximumProfilt(prices):

    #[7,1,5,3,6,4]
    n = len(prices)
    start = 0
    end = start+1
    max_profit = 0
    while(start<n-1 and end < n-1):
        if(prices[start]>prices[end]):
            start = end
            end = end+1
        else:
            profit = prices[end]-prices[start]
            max_profit = max(profit,max_profit)
            end = end+1
    return max_profit


prices = [7,1,5,3,6,4]
print(maximumProfilt(prices))