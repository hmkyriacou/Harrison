#Calculator App
#Harrison Kyriacou

#Modules
import random as rand

#Calculate Function
def calculate (eq):
    equ = eq[0].split(' ')
    if (equ[1] == '+'):
        ans = (float(equ[0]) + float(equ[2]))
    elif (equ[1] == '-'):
        ans = (float(equ[0]) - float(equ[2]))
    elif (equ[1] == '*'):
        ans = (float(equ[0]) * float(equ[2]))
    elif (equ[1] == '/'):
        ans = (float(equ[0]) / float(equ[2]))

    return ans

#Random Calculation Function
def randCalc (num):
    for x in range(num):
        oper = rand.randint(1, 4)
        num1 = round(rand.random() * 100, 3)
        num2 = round(rand.random() * 100, 3)
        if (oper == 1):
            ans = num1 + num2
            print('\n' + str(num1) + "+" + str(num2))
        elif (oper == 2):
            ans = num1 - num2
            print('\n' + str(num1) + "-" + str(num2))
        elif (oper == 3):
            ans = num1 * num2
            print('\n' + str(num1) + "*" + str(num2))
        elif (oper == 4):
            ans = num1 / num2
            print('\n' + str(num1) + "/" + str(num2))
        print (str(round(ans, 3)))

#Main
print("\nWelcome to The Calculator App\nBy Harrison Kyriacou")

#Repeat program
userTest = True
while (userTest == True):
#User Decides to input or random equation
    userDec = int(input("\nTo preform a calculation enter '1'\n\nTo preform a random calculation enter '2'\n"))
#User Decison Test
    decTest = False
    while (decTest == False):
        if (userDec != 1 and userDec != 2):
            print("\nPlease only enter a '1' or a '2'")
            decTest = False
            userDec = input("\nTo preform a calculation enter '1'\n\nTo preform a random calculation enter '2'\n")
        else:
            decTest = True

    if (userDec == 2):
        num = int(input("\nEnter how many random equations you would like: "))
        numTest = False
        while (numTest == False):
            if (num > 10):
                num = input("\nPlease no more than 10. Enter number of equations: ")
                numTest = False
            else:
                numTest = True
        randCalc(num)

    if (userDec == 1):
        print("\nEnter any two term equation to calculate.\n\nUse any of the four basic operators (+, -, *, /)")
        print("\nPlease include spaces between each number and the operator.\n")
        equ = [ input("Enter equation you want to calculate: ") ]

#Input control
        equTest = False
        while (equTest != True):
            if (equ[0].find(' ') == -1):
                print ('Please include spaces between all characters\n')
                equTest = False
                equ = [ input("Enter equation you want to calculate: ") ]
            elif (equ[0].find(' ') == equ[0].rfind(' ')):
                print ('Please include spaces between all characters\n')
                equTest = False
                equ = [ input("Enter equation you want to calculate: ") ]
            elif (len(equ[0].split(' ')) > 3):
                print ('Please only use two numbers\n')
                equTest = False
                equ = [ input("Enter equation you want to calculate: ") ]
            else:
                equTest = True

        print(calculate(equ))
    userDec2 = input("\nTo run program again enter 'yes' to end program enter 'end': ")
    userDec2Test = False
    while (userDec2Test == False):
        if (userDec2 != 'yes' and userDec2 != 'end'):
            userDec2Test = False
            userDec2 = input("\nTo run program again enter 'yes' to end program enter 'end': ")
        else:
            userDec2Test = True
    if (userDec2 == 'yes'):
        userTest = True
    if (userDec2 == 'end'):
        userTest = False
