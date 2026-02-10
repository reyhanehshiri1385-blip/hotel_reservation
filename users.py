def sign_up():
    # first user should register and enter username and password besides first name and last name
    while True:
        print("_"*80)
        print("new user registration...")
        first_name = input("please enter your first name:")
        last_name = input("please enter your last name:")
        username = input("please enter your username:")
        password = input("please enter your password:")
        print("_"*80)
        # storing this data in a file that is espeacially for users
        try:
            with open("users_info.txt","r") as file:
                for line in file:
                    info = line.strip().split(",")
                    # username should be unique
                    if info[2]==username:
                        raise ValueError
            with open("users_info.txt","a") as file:
                # each user has a default balance
                default_balance = 500
                file.write(f"{first_name},{last_name},{username},{password},{default_balance}\n")
                print("_"*80)
                print("Your registration was successful!")
                print("_"*80,"\n")
                print("#"*80)
                print(f"Welcome {first_name} {last_name} to this hotel!")
                print("#"*80)
                break
        except ValueError:
            print("_"*80)
            print("This username priviously registered!")
            print("_"*80)
def log_in(username,password):
    # each user for entering to the program should enter correct username and password
    with open("users_info.txt","r") as file:
            for line in file:
                info = line.strip().split(",")
                if info[2]==username and info[3]==password:
                    print("_"*80)
                    print("Your login was successful!")
                    print("_"*80,"\n")
                    print("#"*80)
                    print(f"welcome {info[0]} {info[1]}")
                    print("#"*80)
                    return True
            print("_"*80)    
            print("Wrong username or password!")
            print("_"*80)
            return False