def stockBuySell(prices):
    # [7,6,4,3,1]
    # [2,3,1,4,9,10]
    n = len(prices)
    left = 0
    right = 1
    maxPrice = 0
    while(left<right and right<n):
        if(prices[left]>prices[right]):
            left = right
        else:
            price = prices[right] - prices[left]
            maxPrice = max(maxPrice,price)
        right = right +1
    return maxPrice

prices1 = [2,3,1,4,9,10]
prices2 = [7,1, 5 ,3 ,6, 4]
print(stockBuySell(prices1))
print(stockBuySell(prices2))



