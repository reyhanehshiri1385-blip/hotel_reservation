def sign_up():
    while True:
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
                default_balance = 500
                file.write(f"{first_name},{last_name},{username},{password},{default_balance}\n")
                print("Your registration was successful!")
                print(f"Welcome {first_name} {last_name}")
                break
        except ValueError:
            print("This username priviously registered!")
def log_in(username,password):
    with open("users_info.txt","r") as file:
            for line in file:
                info = line.strip().split(",")
                if info[2]==username and info[3]==password:
                    print("Your login was successful!")
                    print(f"welcome {info[0]} {info[1]}")
                    return True
            print("Wrong username or password!")
            return False