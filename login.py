class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def display(self):
        # Pure virtual method (abstract) in base class
        raise NotImplementedError("Subclass must implement abstract method")

class UserDetails(User):
    def __init__(self, username, password, fname, lname, email, mobile, location):
        super().__init__(username, password)
        self.fname = fname
        self.lname = lname
        self.email = email
        self.mobile = mobile
        self.location = location
    
    def display(self):
        print(f"{self.username:15}{self.fname:15}{self.lname:15}{self.email:30}{self.mobile:15}{self.location:20}")
    
    def toCSV(self):
        return f"{self.username},{self.password},{self.fname},{self.lname},{self.email},{self.mobile},{self.location}"

def signup():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    email = input("Enter Email: ")
    mobile = input("Enter Mobile: ")
    location = input("Enter Location: ")

    user = UserDetails(username, password, fname, lname, email, mobile, location)
    
    try:
        with open("users.txt", "a") as outfile:
            outfile.write(user.toCSV() + "\n")
        print("Signup successful!")
    except IOError:
        print("Error opening file for writing.")

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    try:
        with open("users.txt", "r") as infile:
            for line in infile:
                parts = line.strip().split(',')
                if len(parts) >= 2 and parts[0] == username and parts[1] == password:
                    print("Login successful!")
                    return True
    except IOError:
        print("Error opening file for reading.")
    
    print("Invalid username or password.")
    return False

def displayAllUsers():
    try:
        with open("users.txt", "r") as infile:
            print(f"{'Username':15}{'First Name':15}{'Last Name':15}{'Email':30}{'Mobile':15}{'Location':20}")
            print("-" * 110)
            for line in infile:
                parts = line.strip().split(',')
                if len(parts) == 7:
                    user = UserDetails(*parts)
                    user.display()
    except IOError:
        print("Error opening file for reading.")

def main():
    while True:
        print("\n1. Signup\n2. Login\n3. Display All Users (Admin)\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            displayAllUsers()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()