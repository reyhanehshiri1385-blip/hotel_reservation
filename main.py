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
                if any_active_reserve=="No":
                    with open("rooms_info.json","r") as file:
                            data1 = json.load(file)
                            for info_room in data1:
                                if info_room["room_id"]== num_room_completed:
                                    info_room["status"] = "completed"
                            with open("rooms_info.json","w") as file:
                                json.dump(data1,file,indent=4)
            elif info["ask_comment"]=="No" :
                user_name = info["username"]
                num_room_no_comment = info["room_id"]
                username_room[user_name]=num_room_no_comment
        with open("reserve_info.json","w") as file:
                    json.dump(data,file,indent=4)  
        return username_room   
username_room = update_completed_reservations()
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
                                print("_"*40)
                                print("REMINDER!")
                                print(f" 24 hours left to your check in date! \n your room id: {room_num}")
                                print("_"*40)
            auto_reminder(user_username)
            # now the user has successful log in so we should check if user has completed room today ask for her/his opinion!
            for username,room in username_room.items():
                if username == user_username:
                    print(" your reservation was completed!\n Do you have an opinion a bout the room you had reserved?\n " \
                    f"the room id was {room}\n")
                    while True:
                        print("enter 1 if: Yes")
                        print("enter 2 if: NO")
                        choice = input("your choice:")
                        if choice=="1":
                            print("_"*40)
                            opinion= input("enter your opinion and comment a bout the room:")
                            while True:
                                point = input("enter one number between 1(*) to 5(*****) to the room performance:")
                                try:
                                    point = int(point)
                                    if int(point)>5 or int(point)<1:
                                        raise ValueError("invalid input! enter again!")
                                    valid_input = "Yes"
                                    break
                                except ValueError:
                                    print("invalid input! enter again!")
                            if valid_input=="Yes":
                                with open("reserve_info.json","r") as file:
                                    data = json.load(file)
                                    for info in data:
                                        if info["username"]==user_username and info["room_id"]==room and info["ask_comment"]=="No":
                                            info["ask_comment"]="Yes"
                                with open("reserve_info.json","w") as file:
                                    json.dump(data,file,indent=4)  
                                print("_"*40)
                                print("your opinion was registered! thank you")
                                print("_"*40)
                                # comment and opinion registration!
                                with open("comment_point_users.json","r") as file:
                                    data = json.load(file)
                                    new_comment = {"username":user_username,"room_id":room,"comment":opinion,"rate":point}
                                    data.append(new_comment)
                                with open("comment_point_users.json","w") as file:
                                    json.dump(data,file,indent=4)
                            break                           
                        elif choice=="2":
                            with open("reserve_info.json","r") as file:
                                    data = json.load(file)
                                    for info in data:
                                        if info["username"]==user_username and info["room_id"]==room and info["ask_comment"]=="No":
                                            info["ask_comment"]="Yes"
                            with open("reserve_info.json","w") as file:
                                json.dump(data,file,indent=4)  
                            break
                        else:
                            print("wrong input! enter again!")
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
                    calculation = rooms.calculate_reserve(room_id,check_in,check_out,capacity)
                    while calculation:
                        print("enter 1 if you want to pay the cost")
                        print("enter 2 if you want to cancel")
                        choice = input("enter:")
                        if choice=="1":
                            if rooms.payment(user_username,calculation):
                                rooms.final_reserve(user_username,room_id,check_in,check_out,capacity,calculation)
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
                        while True:
                            try:
                                print("_"*40)
                                room_id_user= int(input("enter your room id that you want to cancel:"))
                                print("_"*40)
                                check_in_date = input("enter your check in date (YYYY_mm_dd):")
                                check_in_date1 = datetime.strptime(check_in_date,"%Y_%m_%d") 
                                print("_"*40)
                                check_out_date = input("enter your check out data (YYYY_mm_dd):")
                                check_out_date1 = datetime.strptime(check_out_date,"%Y_%m_%d")
                                print("_"*40)
                                break
                            except ValueError:
                                print("invalid input!enter again!")
                        rooms.cancel_reservation(user_username,room_id_user,check_in_date,check_out_date)
                elif choice=="7":
                    rooms.increasing_balance(user_username)
                else:
                    print("wrong input!")
        break
    elif choice=="3":
        break
    else:
        print("wrong number!")