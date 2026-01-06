def sign_up():
    print("new user registration...")
    first_name = input("please enter your first name:")
    last_name = input("please enter your last name:")
    username = input("please enter your username:")
    password = input("please enter your password:")
    try:
        with open("users_info.txt","r") as file:
            for line in file:
                info = line.strip().split(",")
                if info[2]==username:
                    raise ValueError
        with open("users_info.txt","a") as file:
            file.write(f"{first_name},{last_name},{username},{password}\n")
            print("Your registration was successful!")
    except ValueError:
        print("This username priviously registered!")
def log_in():
    print("user login...")
    username = input("please enter your username:")
    password = input("please enter your password:")
    with open("users_info.txt","r") as file:
            for line in file:
                info = line.strip().split(",")
                if  info[2]==username and info[3]==password:
                    print("Your login was successful!")
                    print(f"welcome {info[0]} {info[1]}")
                    return True
                else:
                    print("Wrong username or password!")
                    return False
while True:
    print("enter 1 if: registration")
    print("enter 2 if: login")
    print("enter 3 if: exit")
    choice = input("your choice:")
    if choice=="1":
        sign_up()
        break
    elif choice=="2":
        log_in()
        break
    elif choice=="3":
        break
    else:
        print("wrong number!")
