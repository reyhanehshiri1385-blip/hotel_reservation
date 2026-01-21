from users import sign_up,log_in
import rooms
while True:
    print("enter 1 if: registration")
    print("enter 2 if: login")
    print("enter 3 if: exit")
    choice = input("your choice:")
    if choice=="1":
        sign_up()
        break
    elif choice=="2":
        if log_in() :
            while True:
                print("enter 1 if: you want to see list of rooms")
                print("enter 2 if: you want to search the room according to your request")
                choice = input("your choice:")
                if choice=="1":
                    print("you can see list of available rooms!")
                    rooms.show_rooms()
                    break
                elif choice=="2":
                    while True:
                        search_base = input("you want to search base on (price range) or (facilities):")
                        if search_base=="price range":
                            rooms.search_rooms_price()
                            break
                        elif search_base=="facilities":
                            rooms.search_rooms_facilities()
                            break
                        else:
                            print("just write (price range) or (facilities)")
                else:
                    print("wrong number")
        break
    elif choice=="3":
        break
    else:
        print("wrong number!")
