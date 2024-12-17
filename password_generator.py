import string
import random
from csv import writer


def passgen():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    platform = input("Enter the platform for the password: ")
    pass_len = int(input("Enter the length of the password: "))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)

    password = "".join(s[:pass_len])
    print(f"Generated password: {password}")

    passdata = [platform, password]
    file_name = 'pass.csv'

    try:
        with open(file_name, 'x') as f:
            writedata = writer(f)
            writedata.writerow(["Platform", "Password"])
    except FileExistsError:
        pass

    # Append the password data
    with open(file_name, 'a') as f:  # 'a' mode to append data
        writedata = writer(f)
        writedata.writerow(passdata)


passgen()
