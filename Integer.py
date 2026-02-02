def main():
    # Ask user for an integer from 0 to 9
    while True:
        try:
            user_num = int(input("Enter an integer from 0 to 9: "))

            if 0 <= user_num <= 9:
                break
            else:
                print("Number must be between 0 and 9.")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Print user input
    print(f"User input is: {user_num}")

    # Loop from 0 to 10
    count = 0
    while count <= 10:
        if user_num == count:
            print(
                f"The User variable is equal to the count variable. "
                f"User = {user_num} Count variable = {count}"
            )
        count += 1


main()


    
