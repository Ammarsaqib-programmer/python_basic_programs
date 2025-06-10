def main():
    num = int(input("Enter an integer: "))
    original_num = num
    n = len(str(num))  # Number of digits

    result = 0
    temp = num

    # Calculate the sum of nth powers of digits
    while temp != 0:
        remainder = temp % 10
        result += remainder ** n
        temp //= 10

    # Check if it's an Armstrong number
    if result == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is NOT an Armstrong number.")

if __name__ == "__main__":
    main()
