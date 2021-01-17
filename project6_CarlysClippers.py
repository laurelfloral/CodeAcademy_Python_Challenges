hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

#find the sum of all haircuts 
for i in prices:
  total_price += i

print(total_price)

#Calculate the average price of a haircut 
average_price = total_price / len(prices)
print("Average Haircut Price: $", 
average_price)

#make list comprehension with all prices $5 cheaper
new_prices=[(i - 5) for i in prices]
print("New Prices: $", new_prices)

#Calculate how much revenue was brought in last week 
total_revenue=0

#calculate how much was made for each hairstyle last week 

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: $", total_revenue)

#Calculate Avg Daily Revenue
average_daily_revenue= total_revenue/7
print("Average Daily Revenue: $", average_daily_revenue)

#find the haircuts that are less $30
cuts_under_30=[hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print("The following haircuts are less than $30:", cuts_under_30)



  
