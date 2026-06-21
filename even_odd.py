try:
    num = int(input("Enter a number: "))

    if num == 0:
        print("Zero")
    elif num % 2 == 0:
        print("Even")
    else:
        print("Odd")

except ValueError:
    print("Please enter a valid number.")
