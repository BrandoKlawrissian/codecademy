# Your code below:
# Step 1 Create toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# Step 2 Create prices
prices = [2, 6, 1, 3, 2, 7, 2]
# Step 3 count the number of $2 slices
num_two_dollar_slices = prices.count(2)
# Step 4 Find the length of the toppings list
num_pizzas = len(toppings)
# Step 5 print
print("We sell", num_pizzas, "different kinds of pizza!")
# Step 6 combine the two lists
pizza_and_prices = list(zip(prices, toppings))
# Step 7 print
print(pizza_and_prices)

# Sorting and Slicing Pizzas
# Step 8 Sort the combined list
pizza_and_prices.sort()
print(pizza_and_prices)
# Step 9 Store the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
# Step 10 Store the most expensive pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
# Step 11 We sold our last anchovies pizza, remove from list
pizza_and_prices.pop()
print(pizza_and_prices)
# Step 12 add a new pizza, "peppers"
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
# Step 13 store the 3 cheapest pizzas
three_cheapest = pizza_and_prices[:3]
# Step 14 print the 3 cheapest pizzas
print(three_cheapest)
