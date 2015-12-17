#CHALLENGE:

"""Writing coding interview questions hasn't made me rich. Maybe trading Apple stocks will.
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:"""

#with indices as time, generates random fluctuations of prices across the day
def generate_stock_prices(minutes, open, close):
    import random
    return [random.randrange(open, close) for i in range(minutes)]

#must buy before selling to get best profit
#continously checks times of max vs min prices, and then removes recursively
def get_maxprofit(stockprices):
    if len(stockprices) < 2: #case where all stock price continuously decreased
        return "No Profit Possbile"
    elif stockprices.index(min(stockprices)) < stockprices.index(max(stockprices)):
        return max(stockprices) - min(stockprices)
    else:
        stockprices.remove(max(stockprices)), stockprices.remove(min(stockprices))
        return get_maxprofit(stockprices)

#gets all the changes of stock prices
def get_pricechanges(stockprices):
    return [stockprices[i]-stockprices[i+1] for i in range(len(stockprices)-1)]

def largest_rise(stockprices):
    return max(get_pricechanges(stockprices))

def largest_fall(stockprices):
    return min(get_pricechanges(stockprices))

