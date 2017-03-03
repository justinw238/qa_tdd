import os

from app.bmi import BMI
from app.retirement import Retirement
from app.distance import Distance
from app.verifyemail import VerifyEmail


def getBMI():
    bodymass = BMI()
    weight = (input("Please enter your weight in pounds: "))
    height = (input("Please enter your height in inches: "))
    output = float((bodymass.bmi(weight,height)))
    if output < 18.5:
        print("Your BMI category is Underweight and your BMI is: ", "%.1f" % output)
    elif output > 18.5 and output < 25.0:
        print("Your BMI category is Normal Weight and your BMI is: ", "%.1f" % output)
    elif output > 25:
        print("Your BMI category is Overweight and your BMI is: ", "%.1f" % output)


def determineRetirement():
    retire = Retirement()
    age = (input("Enter your age: "))
    salary = (input("Enter your annual salary: "))
    saving = (input("Enter your percentage saved: "))
    goal = (input("Enter your retirement savings goal: "))

    result = retire.retirement(age, salary, saving, goal)

    if (result < 100):
        print("Goal met at " + repr(result) + ".")
    else:
        print("Goal not met.")


def doDistance():
    dist = Distance()
    x1 = input("Enter point X1: ")
    y1 = input("Enter point Y1: ")
    x2 = input("Enter point X2: ")
    y2 = input("Enter point Y2: ")

    result = dist.distance(x1, y1, x2, y2)

    print("Distance is: ", result)
    print("")


def checkEmail():
    verify = VerifyEmail()
    email = input("Enter an email to verify: ")
    if(verify.verifyEmail(email)):
        print(email + " is a valid email address.")
        print("")
    else:
        print(email + " is not a valid email address.")
        print("")
    return

def clean_up():
    input("\nPress Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    choice = -1
    choice_list = ['0', '1', '2', '3', '4']
    while choice != 0:
        while choice not in choice_list:
            print("1: Calculate Body Mass Index")
            print("2: Calculate Retirement")
            print("3: Calculate Distance")
            print("4: Verify Email")
            print("0: Quit")
            choice = input(">> ")
            if choice not in choice_list:
                print("Invalid choice.")


        if choice == '1':
            getBMI()
            clean_up()
        if choice == '2':
            determineRetirement()
            clean_up()
        if choice == '3':
            result = doDistance()
            clean_up()
        if choice == '4':
            checkEmail()
            clean_up()
        if choice == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            return

        choice = -1


if __name__ == '__main__':
    main()
