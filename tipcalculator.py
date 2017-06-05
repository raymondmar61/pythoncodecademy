meal = 44.50
tax = .0675  #percentage in decimal format
tip = .15

meal = meal + (meal * tax)
print(meal)
total = meal + (meal * tip)
print("%f" % total)
print("%.2f" % total) #float number rounded two decimal places
print("The total is" ,total)