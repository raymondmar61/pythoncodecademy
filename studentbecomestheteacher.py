from statistics import mean

lloyd = {"name": "Lloyd", "homework":[90.0, 97.0, 75.0, 92.0], "quizzes":[88.0, 40.0, 94.0], "tests":[75.0, 90.0]}
alice = {"name": "Alice", "homework":[100.0, 92.0, 98.0, 100.0], "quizzes":[82.0, 83.0, 91.0], "tests":[89.0, 97.0]}
tyler = {"name": "Tyler", "homework":[0.0, 87.0, 75.0, 22.0], "quizzes":[0.0, 75.0, 78.0], "tests":[100.0, 100.0]}

print(lloyd["name"])
print(alice["homework"])
print(tyler["quizzes"])

students = [lloyd, alice, tyler] #no quotes in list students.  I believe the list is variables defining the dictionary.
for student in students:
	print(student["name"])
	print(student["homework"])
	print(student["quizzes"])
	print(student["tests"])

# def average(*numbers):
# 	total = sum(numbers)
# 	print(total)
# average(1,2,3)

# def average(*numbers):
# 	total = sum(numbers)
# 	total = float(total) / len(numbers)
# 	return total
# print(average(1,2,3,4))

#there's no average() function.  It's mean.  Must Import Statistics to use statistics.mean().
def get_average(student):
	homework = ((mean(student["homework"])) * .10) + ((mean(student["quizzes"])) * .30) + ((mean(student["tests"])) * .60)
	return homework
#print("Lloyd's average is" ,get_average(lloyd))

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print(get_letter_grade(80.55))

def get_class_average(students):
	results = []
	for student in students:
		results.append(get_average(student)) #get_average(student) is function at line 30
	return mean(results)
print(get_class_average(students)) #(students) is from the list at line 11
print(get_letter_grade(get_class_average(students)))