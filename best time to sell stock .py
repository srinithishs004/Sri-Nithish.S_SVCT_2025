def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0  # No profit can be obtained with less than two prices
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    
    return max_profit

# Example usage:
stock_prices = [7, 1, 5, 3, 6, 4]
result = max_profit(stock_prices)
print("Maximum Profit:", result)