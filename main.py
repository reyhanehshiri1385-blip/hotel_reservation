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
        print("user login...")
        user_username = input("please enter your username:")
        password = input("please enter your password:")
        if log_in(user_username,password) :
            while True:
                print("enter 1 : see list of rooms")
                print("enter 2 : search the room according to your request")
                print("enter 3 : book a room")
                print("enter 4 : see the list of your reservations")
                print("enter 5 : see the list of your Active reservations")
                print("enter 6 : cancel your reservation")
                print("enter 7 : increasing your balance")
                print("_"*40)
                choice = input("your choice:")
                if choice=="1":
                    print("you can see list of rooms!")
                    rooms.show_rooms()
                    print("_"*40)
                elif choice=="2":
                    while True:
                        search_base = input("you want to search base on (price range) or (facilities):")
                        if search_base=="price range":
                            rooms.search_rooms_price()
                        elif search_base=="facilities":
                            rooms.search_rooms_facilities()
                        else:
                            print("just write (price range) or (facilities)")
                elif choice=="3":
                    check_in = input("please enter your check in date (YYYY_mm_dd):")
                    check_out = input("please enter your check out date (YYYY_mm_dd):")
                    print("you can see list of available rooms during this dates:")
                    print("_"*40)
                    rooms.showroom_basedate(check_in,check_out)
                    room_id= int(input("please enter your room number that you want:"))
                    print("_"*40)
                    capacity= int(input("please enter the number of guests that you have:"))
                    print("_"*40)
                    username= input("please enter your username:")
                    print("_"*40)
                    calculation = rooms.calculate_reserve(room_id,check_in,check_out,capacity)
                    while True:
                        print("enter 1 if you want to pay the cost")
                        print("enter 2 if you want to cancel")
                        choice = input("enter:")
                        if choice=="1":
                            if rooms.payment(username,calculation):
                                rooms.final_reserve(username,room_id,check_in,check_out,capacity,calculation)
                                break
                            else:
                                print("payment wasn't successful!")
                                break                            
                        elif choice=="2":
                            break
                        else:
                            print("wrong number")
                elif choice=="4":
                    rooms.list_reservations(user_username)
                elif choice=="5":
                    rooms.filter_list_reservations(user_username)
                elif choice=="6":
                    pass
                elif choice=="7":
                    rooms.increasing_balance(user_username)
                else:
                    print("wrong input!")
        break
    elif choice=="3":
        break
    else:
        print("wrong number!")
