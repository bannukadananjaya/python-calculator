## codes for operations
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def devide(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)

def power(a,b):
    return a**b

def remainder(a,b):
    return a%b

##operation selection function

def select_op(choice):
    if choice == '#' :
        return -1
    
    elif choice == '$' :
        return 0
    elif choice == '+'or'-'or'/'or'*'or'^'or'%' :
        while True:
            num1s=str(input("Enter the first number :"))
            print(num1s)
            if num1s[-1] == '$' :   ## num1s.endswith('$'):
                return 0
            if num1s[-1] == '#' :
                return -1
            
            try:
                num1=float(num1s)
                break
            except Exception :
                print("Not a valid number, plz enter again")
                continue

        while True:
            num2s = str(input("Enter the second number :"))
            print(num2s)
            if num2s[-1] == '$' :
                return 0
            elif num2s[-1] == '#' :
                return -1
            
            try:
                num2 = float(num2s)
                break
            except Exception :
                print("Not a valid number, please enter again")
                continue
    
        if choice == '+':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '-' :
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice == '*' :
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice == '/' :
            print(num1,"/",num2,"=",devide(num1,num2))
        else :
            print("Something went wrong")
    else :
        print("Unrecognized operation")

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
    #program ends here
    print("Done. Terminating")
    exit()

            