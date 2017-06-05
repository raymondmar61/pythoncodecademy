def bigger(first, second):
	print(max(first, second))
	return bigger	
 
bigger(10, 50)

def hotel_cost(nights):
	return 140 * nights

nightsstay = 3
print(hotel_cost(nightsstay))

def plane_ride_cost(city):
	if city == "Charlotte":
		return 183
	elif city == "Tampa":
		return 220
	elif city == "Pittsburgh":
		return 222
	elif city == "Los Angeles":
		return 475
	else:
		print(city+ " is not on the list.")
		return

plane_ride_cost("San Jose")
print(plane_ride_cost("Charlotte"))

def rental_car_cost(days):
	if days >= 7:
		cost = (days * 40) - 50
		return cost
	elif days >= 3:
		cost = (days * 40) - 20
		return cost
	else:
		cost = (days * 40)
		return cost
print(rental_car_cost(4))

city = "Los Angeles"
days = 10
print(hotel_cost(days-1) + rental_car_cost(days) + plane_ride_cost(city))

#I can also create a function.  Same total trip cost answer.  I added spendingmoney to the function for a higher cost.
#Notice the three functions returns the answer using "return" keyword.  I call the three functions with print()
def totaltripcost(city, days, spendingmoney):
	print(hotel_cost(days-1) + rental_car_cost(days) + plane_ride_cost(city) + spendingmoney)
	return

spendingmoney = 1000
totaltripcost(city, days, spendingmoney)