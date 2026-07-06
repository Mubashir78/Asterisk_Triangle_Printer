def print_triangle() -> None:
    print("Hello. This script prints out a triangle based on asterisk symbol multiplied times your number.\n")
    print("Please type a number below to print out a triangle. Remember to not enter a number too large, otherwise the triangle might not fit your screen and may look unusual.")

    while True:
        try:
            num = int(input("\nEnter a number: "))
            if num <= 0:
                print("Please enter a number greater than 0.")
                continue

            count = 1
            while count <= num:
                print("*" * count)
                count += 1

            input("Press Enter to exit...")
            break

        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    print_triangle()
