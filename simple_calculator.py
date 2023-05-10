#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add( a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def devide(a,b):
    return a/b
        
        

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if choice == '+':
        num1 = int(input('Enter first number: '))
        print(num1)
        num2 = int(input('Enter second number: '))
        print(num2)
        result = add(num1,num2)
        print(float(num1),"+",float(num2),"=",float(result))
        return True
    elif choice == '-':
        minus(num1,num2)
        return True
    elif choice == '*':
        multiply(num1,num2)
        return True
    elif choice == '/':
        devide(num1,num2)
        return True
    if choice == '#':
        return -1
    else:
        return  False

    


        
#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    
  
  

  # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
  
    if(select_op(choice) == -1):
        print("Done. Terminating")
        exit()
    # else:
    #     select_op(choice)
        
        
    
    
    
      
          
