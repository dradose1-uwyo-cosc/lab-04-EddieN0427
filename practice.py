items = ["lego","shirt","icecream","pop","shoes"]
prices = [30, 20, 7, 4, 25]
for index in range(len(items)):
    print("I bought {items[index]} for ${prices[index]}")
total = 0
for price in prices:
    total = price + total
    print(total)
del items[0]
del prices[0]
print(items)
print(prices)
largestprice = max(prices)
indextoremove = prices.index