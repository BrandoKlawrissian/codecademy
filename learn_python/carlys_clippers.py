hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
total_price = sum(prices)

average_price = total_price / len(prices)
print(average_price)

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0

for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: ", total_revenue)

average_daily_revenue = total_revenue / 7

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)

# revised code for simplicity
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Total price of all haircuts
total_price = sum(prices)
average_price = total_price / len(prices)
print("Total Price:", total_price)
print("Average Price:", average_price)

# New prices after $5 discount
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

# Total revenue
total_revenue = sum(price * customers for price, customers in zip(prices, last_week))
print("Total Revenue:", total_revenue)

# Average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

# Haircuts under $30 after discount
cuts_under_30 = [hairstyle for hairstyle, price in zip(hairstyles, new_prices) if price < 30]
print("Cuts Under $30:", cuts_under_30)
