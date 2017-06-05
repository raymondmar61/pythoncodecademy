#This mini-project will give you some practice with functions, lists, and translating mathematical formulae into programming statements.
#the scores are in a container, namely a list.
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print(grades)
def print_grades(grades):
	for eachgrade in grades:
		print(eachgrade)
print_grades(grades)

#"let's just use the built-in sum() function!" The built-in function would work beautifully, but it would be too easy. 
#print(sum(grades))
def grades_sum(scores):
	sum = 0
	for eachscore in scores:
		sum = sum + eachscore
	return sum
print(grades_sum(grades))

#The average test grade can be found by dividing the sum of the grades by the total number of grades.
def grades_average(grades):
	sumgrades = grades_sum(grades)
	return(float(sumgrades) / len(grades)) 
print(grades_average(grades))
#it appears I can call another function in a function.  Look at grades_sum(grades) set equal to variable sumgrades

#We're going to use the average for computing the variance. The variance allows us to see how widespread the grades were from the average.
#A very large variance means that the students' grades were all over the place, while a small variance (relatively close to the average) means that the majority of students did fairly well.
def grades_variance(scores):
	average = grades_average(scores) #call function grades_average() putting in scores in the function
	variance = 0
	for eachscore in scores:
		variance = variance + ((average - eachscore) ** 2)
	print(variance)
	print(len(scores))
	return(variance/len(scores))
print(grades_variance(grades))

#The standard deviation is the square root of the variance. You can calculate the square root by raising the number to the one-half power.
def grades_std_deviation(variance):
	return(variance**0.5)
variance = grades_variance(grades) #call function grades_variance() putting in grades in the function.  Save as a variable variance.  Going to use the value for grades_std_deviation() function
print(grades_std_deviation(variance))