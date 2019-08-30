import json
import datetime

SERVICES_FILENAME = "/Users/student/code/dog_spa_practice/dog_spa/services.json"
TRANSACTIONS_FILENAME = "/Users/student/code/dog_spa_practice/dog_spa/transactions.txt"

now = datetime.datetime.now()


def get_services():
    print("These are the services we offer:")
    with open(SERVICES_FILENAME) as options:
        services = json.load(options)
        for key in services:
            items = services[key].items()
            for item in items:
                dots = 18 - len(item[0])
                print(f"        {item[0]}{'.' * dots}${item[1]['price']}0")
    print("Which service would you like to order today?")
    print()


def choose_services():
    while True:
        choice = input(">>> ")
        if choice == "bath":
            print(f"{choice} such a good choice!")
            print("Your total is: $25.00")
            print("Thank you have a nice day!")
            with open(TRANSACTIONS_FILENAME, "a") as myfile:
                myfile.write(f"\n{now}, {choice}, 25.0")
            break
        elif choice == "massage":
            print(f"{choice} such a good choice!")
            print("Your total is: $10.00")
            print("Thank you have a nice day!")
            with open(TRANSACTIONS_FILENAME, "a") as myfile:
                myfile.write(f"\n{now}, {choice}, 10.0")
            break
        elif choice == "walk":
            print(f"{choice} such a good choice!")
            print("Your total is: $15.00")
            print("Thank you have a nice day!")
            with open(TRANSACTIONS_FILENAME, "a") as myfile:
                myfile.write(f"\n{now}, {choice}, 15.0")
            break
        elif choice == "play":
            print(f"{choice} such a good choice!")
            print("Your total is: $20.00")
            print("Thank you have a nice day!")
            with open(TRANSACTIONS_FILENAME, "a") as myfile:
                myfile.write(f"\n{now}, {choice}, 20.0")
            break
        else:
            print(f"{choice} is an invalid option!")
            pass


def print_welcome_message():
    print(
        """
                         .--~~,__
            :-....,-------`~~'._.'
            `-,,,  ,_      ;'~U'
            _,-' ,'`-__; '--.
            (_/'~~      ''''(;
 WELCOME TO LUXURY DOG SERVICES!
    """
    )


def dog_spa():
    print_welcome_message()
    get_services()
    choose_services()


if __name__ == "__main__":
    dog_spa()
