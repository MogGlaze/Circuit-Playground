def main():
    # Ask user for an integer greater than 20
    while True:
        try:
            user_number = int(input("Enter an integer greater than 20: "))

            if user_number > 20:
                break
            else:
                print("Number must be greater than 20.")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    #  count
    count = 0

    # While user is greater than 1
    while user_number > 1:
        user_number = user_number / 2
        count += 1

    # Output result
    print(f"Final value: {user_number}")
    print(f"Loop count: {count}")


main()
