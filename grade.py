def main():
    per = int(input("Enter the percentage: "))

    if per >= 80:
        print("A Grade")
    elif 70 <= per < 80:
        print("B Grade")
    elif 60 <= per < 70:
        print("C Grade")
    else:
        print("Fail or D Grade")

if __name__ == "__main__":
    main()
