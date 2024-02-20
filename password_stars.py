"""
CP1404 - prac_2
Get a password using minimum length and display asterisks
"""
def get_password():
    password = input("Enter your password: ")
    return password

def print_password_asterisks(password):
    print('*' * len(password))

def main():
    password = get_password()
    print_password_asterisks(password)


main()