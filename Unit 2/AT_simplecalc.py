user_equation = input("Enter an eqution: ")
num_1 = user_equation[0]
operator = user_equation[1]
num_2 = user_equation[2]
if operator == "+":
    print ("The result is " + str(int(num_1) + int(num_2)))
elif operator == "*":
    print ("The result is " + str(int(num_1) * int(num_2)))
elif operator == "/":
    print ("The result is " + str(int(num_1) / int(num_2)))
elif operator == "-":
    print ("The result is " + str(int(num_1) - int(num_2)))
else:
    print ("The result is " + str(int(num_1) % int(num_2)))





#print ("The result is ____")  
#Addition +
#Subtraction -
#Multiplication *
#Division /
#Modulo %