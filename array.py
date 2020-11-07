def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif not password.isdigit():
            print("Make sure your password has a number in it")
        elif not password.isupper(): 
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password seems fine")
            break

validate()