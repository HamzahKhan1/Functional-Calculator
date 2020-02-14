#functional_calculator

#define your functions
def addition(x,y):
    outcome = x+y
    print(str(x) + "+" + str(y) + "=" + str(outcome))

def subtraction(x,y):
    outcome = x-y
    print(str(x) + "-" + str(y) + "=" + str(outcome))

def multiplication(x,y):
    outcome = x*y
    print(str(x) + "x" + str(y) + "=" + str(outcome))

def division(x,y):
    outcome = x/y
    print(str(x) + "/" + str(y) + "=" + str(outcome))

#offer the user the option to run again after completing
go_again = "y"

#everything from here to the end should be in a while loop that checks if the user wants to play again
while str(go_again) == "y":
    userChoice = int(input("What kind of calculation would you like to perform?\n[1]Addition\n[2]Subtraction\n[3]Multiplication\n[4]Division\nEnter Choice: "))
    print("-----------------------")
    if(userChoice == 1):
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))
        addition(firstNumber, secondNumber)
    elif(userChoice == 2):
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))
        subtraction(firstNumber, secondNumber)
    elif(userChoice == 3):
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))
        multiplication(firstNumber, secondNumber)
    elif(userChoice == 4):
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))
        division(firstNumber, secondNumber)
    else:
        print("Not a specified option")

    go_again = input("Should we go again? (y)es or (no) >> ")

print("Thank you for playing!")
    



