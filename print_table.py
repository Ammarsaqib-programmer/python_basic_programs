def main():
    num = int(input("Enter the number for the table: "))
    start = int(input("Enter the starting multiplier: "))
    end = int(input("Enter the ending multiplier: "))

    for i in range(start, end + 1):
        print(f"{num} x {i} = {num * i}")

if __name__ == "__main__":
    main()
