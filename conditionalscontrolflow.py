def clinic():
    print("You've just entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print("Of course this is the Argument Room, I've told you that already!")
    else:
        print("You didn't pick left or right! Try again.")
        clinic()

clinic()

def using_control_once():
    if 800 > 700:
        return "Success #1"

def using_control_again():
    if "Raymond" == "Raymond": #reminder use : to define conditionals
        return "Success #2"

print(using_control_once()) #reminder calling a function requires ()
print(using_control_again())

answer = "\'Tis but a scratch!"
answerfrench = "No moiseur"

def black_knight():
    if answer == "\'Tis but a scratch!":
        print("yes")
        #return #don't need return?!?
    else:
        print("no")
        #return #don't need return?!?

black_knight()

def french_soldier():
    if answerfrench == "Yes moiseur":
        return True
    else:
        return False

print(french_soldier()) #prints False because french_soldier function didn't match answerfrench

def greater_less_equal_5(answer):
    #if statements below return values in various syntax
    if answer > 5:
        print(100)
    elif answer < 5:
        return -1
    else:
        return "Zero"

#call function greater_less_equal_5 with answer variable
print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))

def the_flying_circus():
    if 800 > 500 or 1000 > 900:
        return True
    elif "jack" != "richard":
        return False
    else:
        return ("Good success")

print(the_flying_circus()) #reminder calling a function requires ()