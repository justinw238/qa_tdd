from app.distance import Distance
from app.verifyemail import VerifyEmail


def doDistance(choice):
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

        if choice == '3':
            result = doDistance(choice)
        if choice == '4':
            checkEmail()
        if choice == '0':
            return

        choice = -1


if __name__ == '__main__':
    main()