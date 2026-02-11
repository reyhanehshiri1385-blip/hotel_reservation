from email.errors import InvalidDateDefect
from users import sign_up,log_in
from datetime import datetime
import json
# calling this function before any proccessing, every time this programm runs we should check for reservations's status!
# maybe if the check out date is past we should change the status of reservation to completed.
def update_completed_reservations():
    with open("reserve_info.json","r") as file:
        # create a dictionary can collect user, and collect room that has completed status today 
        # it is the time to ask for user's opinin a bout the room he/she has reserved. 
        username_room=dict()
        data = json.load(file)
        for info in data:
            date_now = datetime.now()
            check_out_date = datetime.strptime(info["check_out"],"%Y_%m_%d")
            if (date_now > check_out_date) and info["status"]=="active" and info["ask_comment"]=="No" :
                info["status"]= "completed"
# the user can give opinion and point!
                user_name = info["username"]
                num_room_completed = info["room_id"]
                username_room[user_name]=num_room_completed
                # also we should check if that room has any active reserve or not!
                # if it has, the status of that room when users see should be active!
                any_active_reserve= "No"
                for info in data:
                    if info["status"]=="active" and info["room_id"]==num_room_completed:
                        any_active_reserve= "Yes"
                        with open("rooms_info.json","r") as file:
                            data1 = json.load(file)
                            for info_room in data1:
                                if info_room["room_id"]== num_room_completed:
                                    info_room["status"] = "active"
                            with open("rooms_info.json","w") as file:
                                json.dump(data1,file,indent=4)
                # if that room has not any active reservation
                # so the status of that room should be completed!
                if any_active_reserve=="No":
                    with open("rooms_info.json","r") as file:
                            data1 = json.load(file)
                            for info_room in data1:
                                if info_room["room_id"]== num_room_completed:
                                    info_room["status"] = "completed"
                            with open("rooms_info.json","w") as file:
                                json.dump(data1,file,indent=4)
            elif info["ask_comment"]=="No" and info["status"]=="completed" :
                user_name = info["username"]
                num_room_no_comment = info["room_id"]
                username_room[user_name]=num_room_no_comment
        with open("reserve_info.json","w") as file:
                    json.dump(data,file,indent=4)  
        return username_room   
username_room = update_completed_reservations()
exit_loop_2 = "No"
while True:
    if exit_loop_2=="Yes":
        break
    # the menu
    print("_"*80,"\n")
    print("enter 1 if: registration")
    print("enter 2 if: login")
    print("enter 3 if: exit")
    print("_"*80)
    choice = input("your choice:")
    print("_"*80)
    if choice=="1":
        sign_up()
        break
    elif choice=="2":
        print("_"*80)
        print("user login...")
        user_username = input("please enter your username:")
        password = input("please enter your password:")
        print("_"*80)
        if log_in(user_username,password) :
            # when user logs in to the program if only 24 hours left the user's check in date,
            # user should notice the alarm!
            def auto_reminder(username):
                with open("reserve_info.json","r") as file:
                    data = json.load(file)
                    for info in data:
                        if info["username"]== username and info["status"]== "active":
                            room_num = info["room_id"]
                            date_now = datetime.now()
                            check_in_date = datetime.strptime(info["check_in"],"%Y_%m_%d")
                            day_diff = (check_in_date - date_now).days
                            if day_diff == 1 :
                                print("_"*80)
                                print("REMINDER!")
                                print(f" 24 hours left to your check in date! \n your room id: {room_num}")
                                print("_"*80)
            # when user has successful login this function is called to check for his\her reservations
            auto_reminder(user_username)
            # now the user has successful log in so we should check if user has completed room today ask for her/his opinion!
            for username,room in username_room.items():
                # first asking the user for opinion's registration!
                if username == user_username:
                    print("_"*80)
                    print("your reservation was completed!\n\n Do you have an opinion a bout the room you had reserved?\n\n " \
                    f"the room id was {room}\n")
                    print("_"*80)
                    while True:
                        print("_"*80)
                        print("enter 1 if: Yes")
                        print("enter 2 if: NO")
                        print("_"*80)
                        choice = input("your choice:")
                        # user can give comment and rate (1 to 5) for the room that he\she had reserved.
                        if choice=="1":
                            print("_"*80)
                            opinion= input("enter your opinion and comment a bout the room:")
                            while True:
                                point = input("enter one number between 1(*) to 5(*****) to the room performance:")
                                print("_"*80)
                                # exception handling
                                try:
                                    point = int(point)
                                    if int(point)>5 or int(point)<1:
                                        raise ValueError("invalid input! enter again!")
                                    valid_input = "Yes"
                                    break
                                except ValueError:
                                    print("_"*80)
                                    print("invalid input! enter again!")
                                    print("_"*80)
                            # if user entered valid input we should store her\his data
                            if valid_input=="Yes":
                                with open("reserve_info.json","r") as file:
                                    data = json.load(file)
                                    for info in data:
                                        if info["username"]==user_username and info["room_id"]==room and info["ask_comment"]=="No":
                                            info["ask_comment"]="Yes"
                                with open("reserve_info.json","w") as file:
                                    json.dump(data,file,indent=4)  
                                print("_"*80)
                                print("your opinion was registered! thank you")
                                print("_"*80)
                                # comment and opinion registration!
                                with open("comment_point_users.json","r") as file:
                                    data = json.load(file)
                                    new_comment = {"username":user_username,"room_id":room,"comment":opinion,"rate":point}
                                    data.append(new_comment)
                                with open("comment_point_users.json","w") as file:
                                    json.dump(data,file,indent=4)
                                # after the user registered her/his opinion, we should update rates's average of that room!
                                def update_average_rates(room_id):
                                    with open("comment_point_users.json","r") as file:
                                        # storing all of the rates a bout the room that user registered her\his opinion
                                        rates = []
                                        data = json.load(file)
                                        for info in data:
                                            if info["room_id"]==room_id:
                                                rates.append(info["rate"])
                                    # average calculation
                                    average_rate = sum(rates)/len(rates)
                                    # storing update average to can show in list of rooms
                                    with open("rooms_info.json","r") as file:
                                        data = json.load(file)
                                        for info in data:
                                            if info["room_id"]== room_id:
                                                info["average_rate"] = average_rate
                                    with open("rooms_info.json","w") as file:
                                        json.dump(data,file,indent=4)
                                update_average_rates(room)
                            break                           
                        elif choice=="2":
                            # user does not want to register her/his opinion, just we should sure that asking for comment one time has happened!
                            with open("reserve_info.json","r") as file:
                                    data = json.load(file)
                                    for info in data:
                                        if info["username"]==user_username and info["room_id"]==room and info["ask_comment"]=="No":
                                            info["ask_comment"]="Yes"
                            with open("reserve_info.json","w") as file:
                                json.dump(data,file,indent=4)  
                            break
                        else:
                            print("_"*80)
                            print("wrong input! enter again!")
                            print("_"*80)
            import rooms
            while True:
                # the new menu after the user had successful log in
                print("_"*80)
                print("enter 1 : see list of rooms")
                print("enter 2 : search the room according to your request")
                print("enter 3 : book a room")
                print("enter 4 : see the list of your reservations")
                print("enter 5 : see the list of your Active reservations")
                print("enter 6 : cancel your reservation")
                print("enter 7 : increasing your balance")
                print("enter 8 : exit")
                print("_"*80)
                choice = input("your choice:")
                if choice=="1":
                    print("_"*80)
                    print("you can see list of rooms!")
                    print("_"*80)
                    rooms.show_rooms()
                    print("_"*80)
                elif choice=="2":
                    # user should enter one of options: price range or facilities
                    while True:
                        print("_"*80)
                        search_base = input("you want to search base on (price range) or (facilities) or (type):")
                        print("_"*80)
                        if search_base=="price range":
                            rooms.search_rooms_price()
                            break
                        elif search_base=="facilities":
                            rooms.search_rooms_facilities()
                            break
                        elif search_base=="type":
                            rooms.search_rooms_type()
                            break
                        else:
                            print("_"*80)
                            print("just write (price range) or (facilities) or (type)")
                            print("_"*80)
                elif choice=="3":
                    while True:
                        try:
                            # user should enter her/his check in and check out date and see list of available rooms during this dates
                            print("_"*80)
                            check_in = input("please enter your check in date (YYYY_mm_dd):")
                            # exception handling...
                            check_in_exc_handl= datetime.strptime(check_in,"%Y_%m_%d")
                            date_now = datetime.now()
                            # if date was past!
                            if check_in_exc_handl<date_now:
                                raise ValueError
                            print("_"*80)
                            check_out = input("please enter your check out date (YYYY_mm_dd):")
                            # exception handling...
                            check_out_exc_handl= datetime.strptime(check_out,"%Y_%m_%d")
                            # if date was past!
                            if check_out_exc_handl<date_now:
                                raise ValueError
                            print("_"*80)
                            print("you can see list of available rooms during this dates:")
                            print("_"*80)
                            break
                        except ValueError:
                            print("_"*80)
                            print("invalid input or invalid date! enter again!")
                            print("_"*80)
                    rooms.showroom_basedate(check_in,check_out)
                        # after user can choose the room that he/she wants
                    while True:
                        # exception handling...
                        try:    
                            print("_"*80)
                            room_id= int(input("please enter your room number that you want:"))
                            print("_"*80)
                            capacity= int(input("please enter the number of guests that you have:"))
                            print("_"*80)
                            break
                        except ValueError:
                            print("_"*80)
                            print("wrong input! enter again!")
                            print("_"*80)
                    # this function calculat the cost of reserve and return it
                    calculation = rooms.calculate_reserve(room_id,check_in,check_out,capacity)
                    while calculation:
                        # user should decide to pay or cancel reserve
                        print("_"*80)
                        print("enter 1 if you want to pay the cost")
                        print("enter 2 if you want to cancel")
                        print("_"*80)
                        choice = input("enter your choice:")
                        if choice=="1":
                            # after successful payment reserve registers and factor stores in a file (reserve_info.json)
                            if rooms.payment(user_username,calculation):
                                rooms.final_reserve(user_username,room_id,check_in,check_out,capacity,calculation)
                                break
                            # if user had not enough balance, payment is not successful and exit
                            else:
                                print("_"*80)
                                print("payment wasn't successful!")
                                print("_"*80)
                                break                            
                        elif choice=="2":
                            break
                        else:
                            print("_"*80)
                            print("wrong input!")
                            print("_"*80)
                elif choice=="4":
                    rooms.list_reservations(user_username)
                elif choice=="5":
                    rooms.filter_list_reservations(user_username)
                elif choice=="6":
                        # when users want to cancel reservations, they should enter the information of reserve
                        while True:
                            # exception handling...
                            try:
                                print("_"*80)
                                room_id_user= int(input("enter your room id that you want to cancel:"))
                                print("_"*80)
                                check_in_date = input("enter your check in date (YYYY_mm_dd):")
                                check_in_date1 = datetime.strptime(check_in_date,"%Y_%m_%d") 
                                print("_"*80)
                                check_out_date = input("enter your check out data (YYYY_mm_dd):")
                                check_out_date1 = datetime.strptime(check_out_date,"%Y_%m_%d")
                                print("_"*80)
                                # if user has cenceled her/his reserve, can not cancel it again!
                                # if user has completed her/his reserve, can not cancel it again!
                                with open("reserve_info.json","r") as file:
                                    data = json.load(file)
                                    for info in data:
                                        if info["room_id"]==room_id_user and info["check_in"]==check_in_date and info["check_out"]==check_out_date and info["username"]==user_username:
                                            if info["status"]=="canceled":
                                                raise ValueError("this room has been canceled before!")
                                            elif info["status"]=="completed":
                                                raise ValueError("this room has been completed before!")
                                break
                            except ValueError:
                                print("_"*80)
                                print("invalid input!enter again!")
                                print("_"*80)
                        rooms.cancel_reservation(user_username,room_id_user,check_in_date,check_out_date)
                elif choice=="7":
                    rooms.increasing_balance(user_username)
                elif choice=="8":
                    exit_loop_2="Yes"
                    break
                else:
                    print("_"*80)
                    print("wrong input!")
                    print("_"*80)
        else:
            break            
    elif choice=="3":
        break
    else:
        print("_"*80)
        print("wrong number!")
        print("_"*80)