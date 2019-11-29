def main():
    password = get_password()
    password_check(password)

def get_password():
    secret = input("Please enter your password")
    return secret

def password_check(secret):
    valid = False
    while not valid:
        if len(secret) <6:
            secret = input("Please enter your password")
            valid = False
        else:
            valid = True
            for char in range (0, len(secret)):
                print("*", end =' ')

main()