num = int(input(" Enter a non-negative number: "))
for x in range (1,num+1):
        if x%3==0 and x%5==0:
            print("fizz buzz")
        elif x%3==0:
            print('fizz')
        elif x%5==0:
            print('buzz')
        else:
            print(x)  
