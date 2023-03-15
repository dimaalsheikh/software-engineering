# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def encode(password):
    encoded = ""
    for i in password:
        digit = int(i) + 3
        encoded += str(digit)
    return encoded


def main():
    encoded = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Quit")
        print()

        menu_selection = int(input("Please enter an option: "))
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("The encoded password is " + encoded)

        elif menu_selection == 2:
            break


if __name__ == "__main__":
    main()
