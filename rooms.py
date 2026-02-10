from abc import ABC,abstractmethod
# we have an abstract class Room and child classes that they are the type of rooms 
class Room(ABC):
    # a room has some atributes like: number , facilities , capacity and... that putting in a cunstuctor!
    def __init__(self,room_id,base_price,facilities,capacity,available,status,average_rate):
        self.room_id = room_id
        self.base_price = base_price
        self.facilities = facilities
        self.capacity = capacity
        self.available = available
        self.status = status
        self.average_rate = average_rate
    # every room should have this method but with different performance 
    # when we call this method for each room we have polymorphism
    @abstractmethod
    def calculate_price(self,num_night):
        pass
class Single_Room(Room):
    # this type of room has 20 dollars for services besides base price
    def calculate_price(self, num_night):
        # if number of nights can be more than 7 , user gets discount: without paying the cost for service
        if num_night >= 7:
            calculation = (self.base_price)*(num_night)
            print("_"*80)
            print(f"""tatal cost: {calculation} \n
                  you got discount! \n
                  you do not need to pay 20 dollars for services besides base price""")
            print("_"*80)
            return calculation
        else:
            calculation = (self.base_price)*(num_night)+20
            print("_"*80)
            print(f"""tatal cost: {calculation} \n
                    20 dollars for services besides base price""")
            print("_"*80)
            return calculation
class Double_Room(Room):
    # this type of room has 30 dollars for services besides base price
    def calculate_price(self,num_night):
        # if number of nights can be more than 7 , user gets discount: without paying the cost for service
        if num_night >= 7:
            calculation = (self.base_price)*(num_night)
            print("_"*80)
            print(f"""tatal cost: {calculation} \n
                  you got discount! \n
                  you do not need to pay 30 dollars for services besides base price""")
            print("_"*80)
            return calculation
        else:
            calculation = (self.base_price)*(num_night)+30
            print("_"*80)
            print(f"""tatal cost: {calculation} \n
                    30 dollars for services besides base price""")  
            print("_"*80)
            return calculation     
class Suite_Room(Room):
    # this type of room has 10 dollars for services besides base price
    def calculate_price(self,num_night):
        # if number of nights can be more than 7 , user gets discount: without paying the cost for service
        if num_night >= 7:
            calculation = (self.base_price)*(num_night)
            print("_"*80)
            print(f"""tatal cost: {calculation} \n
                  you got discount! \n
                  you do not need to pay 10 dollars for services besides base price""")
            print("_"*80)
            return calculation
        else:
            calculation = (self.base_price)*(num_night)+10
            print("_"*80)
            print(f"""tatal cost: {calculation} \n
                    10 dollars for services besides base price""")
            print("_"*80)
            return calculation
import json
# this program read data for each room of the file (rooms_info.json)
# for each type of room we have class and can make an object for each room
with open("rooms_info.json","r") as file:
    # list_rooms is a list that has all of the objects
    list_rooms = []
    file = json.load(file)
    for line in file:
        if line["type"]== "single":
            single_room = Single_Room(line["room_id"],line["base_price"],line["facilities"],line["capacity"],line["available"],line["status"],line["average_rate"])
            if line["available"]=="True":
                list_rooms.append(single_room)         
        elif line["type"]== "double":
            double_room = Double_Room(line["room_id"],line["base_price"],line["facilities"],line["capacity"],line["available"],line["status"],line["average_rate"])
            if line["available"]=="True":
                list_rooms.append(double_room)
        elif line["type"]== "suite":
            suite_room = Suite_Room(line["room_id"],line["base_price"],line["facilities"],line["capacity"],line["available"],line["status"],line["average_rate"])
            if line["available"]=="True":
                list_rooms.append(suite_room)
def show_rooms():
    # iterating list_rooms to show each room to the users with all of attributes 
    for room in list_rooms:
        if type(room)==Single_Room:
            print("_"*80)
            print(f"a single room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
        if type(room)==Double_Room:
            print("_"*80)
            print(f"a double room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
        if type(room)==Suite_Room:
            print("_"*80)
            print(f"a suite room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n") 
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)   
def search_rooms_price():
    # user can choose low and high price and see the rooms that have price between this range!
    while True:
        # exception handling...
        try:
            print("_"*80)
            low_price = input("enter type of price range,first low price limit: (for example 50 dollars)")
            low_price_float = float(low_price)
            print("_"*80)
            high_price = input("then high price limit: (for example 100 dollars)")
            high_price_float = float(high_price)
            print("_"*80)
            break
        except ValueError:
            print("_"*80)
            print("invalid input! enter again!")
            print("_"*80)           
    list_choice = []
    # finding rooms that have the price between the requested range! 
    for room in list_rooms:
        if room.base_price>= float(low_price) and room.base_price<= float(high_price):
            list_choice.append(room)
    print("_"*80)        
    print("this result is based on your choice:")
    print("_"*80)
    if list_choice==[]:
        print("_"*80)
        print("sorry we couldn't find any result!")
        print("_"*80)
    for room in list_choice:
        if type(room)==Single_Room:
            print("_"*80)
            print(f"a single room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
        if type(room)==Double_Room:
            print("_"*80)
            print(f"a double room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
        if type(room)==Suite_Room:
            print("_"*80)
            print(f"a suite room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
    return list_choice 
def search_rooms_facilities():
    # exception handling...
    while True:  
        try:      
            print("_"*80)
            facilities_choice = input("enter facilities that you want: (choice between: tv,fridge,wifi)")
            print("_"*80)
            facil_choice_list = facilities_choice.split(",")
            break
        except ValueError:
            print("_"*80)
            print("please enter valid input! with (,) enter again!")
            print("_"*80)
    if facilities_choice=="tv":
        facil_choice_list = ["tv"]
    elif facilities_choice=="fridge":
        facil_choice_list = ["fridge"]
    elif facilities_choice=="wifi":
        facil_choice_list = ["wifi"]
    list_choice = []
    # check for finding the facilities that user wants
    for room in list_rooms:
        if room.facilities == facil_choice_list:
            list_choice.append(room)
    print("_"*80)        
    print("this result is based on your choice:")
    print("_"*80)
    if list_choice==[]:
        print("_"*80)
        print("sorry we couldn't find any result!")
        print("_"*80)
    for room in list_choice:
        if type(room)==Single_Room:
            print("_"*80)
            print(f"a single room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
        if type(room)==Double_Room:
            print("_"*80)
            print(f"a double room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
        if type(room)==Suite_Room:
            print("_"*80)
            print(f"a suite room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80) 
    return list_choice
from datetime import datetime
def calculate_reserve(num_room,check_in,check_out,num_people):
    existing_in=datetime.strptime(check_in,"%Y_%m_%d")
    existing_out=datetime.strptime(check_out,"%Y_%m_%d")
    # first we calculate the nights's difference between check in date and check out date 
    # based on number of nights we calculate the cost of reserve
    for room in list_rooms:
        if room.room_id == num_room and room.capacity == num_people:
            if room.status == "canceled":
                num_night = (existing_out-existing_in).days
                # polymorphism
                calculation=room.calculate_price(num_night) 
                print("_"*80)
                return calculation
            elif room.status == "completed":
                num_night = (existing_out-existing_in).days
                # polymorphism
                calculation=room.calculate_price(num_night) 
                print("_"*80)      
                return calculation           
            elif room.status == "active":
                num_night = (existing_out-existing_in).days
                # polymorphism
                calculation=room.calculate_price(num_night) 
                print("_"*80)
                return calculation
    print("_"*80)
    print("we do not have this room!,enter correct number for room you wanted!")
    print("_"*80)
    return None
def showroom_basedate(check_in,check_out):
    rooms=[]
    check_in=datetime.strptime(check_in,"%Y_%m_%d")
    check_out=datetime.strptime(check_out,"%Y_%m_%d")
    for room in list_rooms:
        if room.status=="completed":
            rooms.append(room)
        elif room.status=="canceled":
            rooms.append(room)
        # if the room has an active status, we check if the room reservation was not in the time period selected by the user, 
        # we will display this room in the search results.
        elif room.status=="active":
            with open("reserve_info.json") as file:
                data = json.load(file)
                is_available= True
                for line in data:
                    if line["room_id"]==room.room_id:
                        exsisting_in=datetime.strptime(line["check_in"],"%Y_%m_%d")
                        exsisting_out=datetime.strptime(line["check_out"],"%Y_%m_%d")
                        if not(check_in >= exsisting_out or check_out <= exsisting_in):
                            is_available = False
                            break
                if is_available:
                    rooms.append(room)               
    for room in rooms:
        if type(room)==Single_Room:
            print("_"*80)
            print(f"a single room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
        if type(room)==Double_Room:
            print("_"*80)
            print(f"a double room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n")
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
        if type(room)==Suite_Room:
            print("_"*80)
            print(f"a suite room with this information:\n")
            print(f"room id:{room.room_id} |,base price:{room.base_price}\n\n facilities:{room.facilities} |,capacity:{room.capacity}\n") 
            print(f"status:{room.status}\n")
            print(f"Average rating:{room.average_rate} (of 5)")
            print("_"*80)
def payment(username,calculation):
    print("in pay...")
    # opening the file for storing users's data and updating balance for user after paying the cost of reservation. 
    with open("users_info.txt","r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            info = line.strip().split(",") 
            if info[2]==username:
                if calculation<= float(info[4]):
                    subtraction = float(info[4])-calculation
                    info[4]=f"{subtraction}"
                    lines[i]= ",".join(info)+"\n"
                    print("_"*80)
                    print("your payment was successful!")
                    print(f"now your new balance is {info[4]}")
                    print("_"*80)
                    can_reserve = True 
                    break
                # if the cost of reservation is more than user's balance , payment will not be successful and user can not reserve the room.
                else:
                    print("_"*80)
                    print("Wrong! your balance is not enough!")
                    print("_"*80)
                    can_reserve = False
                    break
        with open("users_info.txt","w") as file:
            file.writelines(lines)
        return can_reserve
def final_reserve(username,room_num,check_in,check_out,people_num,calculation):
    # storing data and change status for room that has reserved!
    with open("rooms_info.json","r") as file:
        data = json.load(file)
        for info in data:
            if info["room_id"]== room_num:
                info["status"] = "active"
    with open("rooms_info.json","w") as file:
        json.dump(data,file,indent=4)
    # when user do not close the app after reserve, information in the file(rooms_info.json) has updated but in
    # the room's objects has not updated yet!
    # so we should update it earlier in list_rooms (oop)
    for room in list_rooms:
        if room.room_id== room_num:
            room.status = "active"
    # storing data for reserving , in file(reserve_info.json)
    with open("reserve_info.json","r") as file:
        data = json.load(file)
        info_new_reserve={"username":username,"room_id":room_num,"check_in":check_in,"check_out":check_out,
                          "capacity":people_num,"total_price":calculation,"status":"active","ask_comment":"No" }
        data.append(info_new_reserve)
    with open("reserve_info.json","w") as file:
        json.dump(data,file,indent=4)
    print("_"*80)
    print("your reservation was SUCCESSFUl!\n")
    print("you can see the information for your reservation...")
    print(f"\n Username:{username}\n\n Room_id:{room_num}\n\n check_in date:{check_in}\n\n check_out date:{check_out}\n\n Capacity:{people_num}\n\n Total_price:{calculation}\n\n status:active\n")
    print("_"*80)
def list_reservations(username):
    # searching in a file for storing data of reservations
    # all of the reservations for that username should display!
    with open("reserve_info.json","r") as file:
        data = json.load(file)
        user_found = "No"
        for info in data:
            if info["username"]==username:
                user_found = "Yes"
                print("_"*80)
                print(f"\n Room_id:{info["room_id"]}\n\n check_in date:{info["check_in"]}\n\n check_out date:{info["check_out"]}\n\n Capacity:{info["capacity"]}\n\n Total_price:{info["total_price"]}\n\n Status:{info["status"]}\n")
                print("_"*80)
        if user_found == "No":
            print("_"*80)
            print("No reservation yet!")
            print("_"*80)
def filter_list_reservations(username):
    # searching in a file for storing data of reservations
    with open("reserve_info.json","r") as file:
        data = json.load(file)
        user_found = "No"
        for info in data:
            # just displaying all of the active reserves for that username!
            if info["username"]==username and info["status"]=="active":
                user_found = "Yes"
                print("_"*80)
                print(f"\n Room_id:{info["room_id"]}\n\n check_in date:{info["check_in"]}\n\n check_out date:{info["check_out"]}\n\n Capacity:{info["capacity"]}\n\n Total_price:{info["total_price"]}\n\n Status:{info["status"]}\n")
                print("_"*80)
        if user_found == "No":
            print("_"*80)
            print("No active reservation yet!")
            print("_"*80)
def increasing_balance(username):
    while True:
        # exception handling...
        try:
            print("_"*80)
            amount = input("How many dollars do you want to increase?")
            print("_"*80,"\n")
            amount_float = float(amount)
            if amount_float <0:
                raise ValueError
            break
        except ValueError:
            print("_"*80)
            print("wrong input! enter again!")
            print("_"*80)
    # the amount that user enters , is added to his\her balance
    print("while proccessing your account...")   
    with open("users_info.txt","r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            info = line.strip().split(",") 
            if info[2]==username:
                old_balance= float(info[4])
                new_balance =float(info[4])+float(amount)
                info[4]= str(new_balance)
                lines[i]= ",".join(info)+"\n"
                print("_"*80)
                print("increasing your balance was successful!\n")
                print(f"you had {old_balance}\nnow your new balance is {float(info[4])}")
                print("_"*80)
                break
        with open("users_info.txt","w") as file:
            file.writelines(lines)
def cancel_reservation(username,room_id,check_in,check_out):
    check_in_ob = datetime.strptime(check_in,"%Y_%m_%d")
    with open("reserve_info.json","r") as file:
        data = json.load(file)
        reserve_found="No"
        for info in data:
            if info["username"]==username and info["room_id"]==room_id and info["check_in"]==check_in and info["check_out"]==check_out:
                reserve_found="Yes"
                info["status"]="canceled"
                total_price=info["total_price"]
                with open("reserve_info.json","w") as file:
                    json.dump(data,file,indent=4)
                # check the status of that room if it has not any active reserve changing the status to canceled in rooms_info.json!
                with open("reserve_info.json","r") as file:
                    data = json.load(file)
                    any_active_reserve= "No"
                    for info in data:
                        if info["room_id"]==room_id:
                            if info["status"]=="active":
                                any_active_reserve="Yes"
                    # not any active reserve
                    if any_active_reserve=="No":
                        with open("rooms_info.json","r") as file:
                            data = json.load(file)
                            for info in data:
                                if info["room_id"]== room_id:
                                    info["status"] = "canceled"
                            with open("rooms_info.json","w") as file:
                                json.dump(data,file,indent=4)
                        # change the status in object of rooms
                        for room in list_rooms:
                            if room.room_id== room_id:
                                room.status = "canceled"
                    # this room has active reserve
                    if any_active_reserve=="Yes":
                        with open("rooms_info.json","r") as file:
                            data = json.load(file)
                            for info in data:
                                if info["room_id"]== room_id:
                                    info["status"] = "active"
                            with open("rooms_info.json","w") as file:
                                json.dump(data,file,indent=4)
                        # change the status in object of rooms
                        for room in list_rooms:
                            if room.room_id== room_id:
                                room.status = "active"       
                print("_"*80)              
                print("your reservation was canceled")
                print("_"*80)
                date_now = datetime.now()
                # 48 hours means 2 days 
                hour_diff = ((check_in_ob-date_now).total_seconds())/3600
                # opening file related to users account
                print("_"*80)
                print("in returning the cost of reservation...\n")
                with open("users_info.txt","r") as file:
                    lines = file.readlines()
                    for i,line in enumerate(lines):
                        info = line.strip().split(",") 
                        if info[2]==username:
                            # if more than 48 hours to check in date, whole of cost returns
                            if hour_diff > 48 :
                                old_balance = info[4]
                                new_balance = float(info[4])+total_price
                                info[4]= str(new_balance)
                                lines[i]= ",".join(info)+"\n"
                                print("_"*80)
                                print("returning was successful!\ntotal cost was returned!")
                                print(f"you had {float(old_balance)} dollars \n now your new balance is {info[4]}")
                                print("_"*80)
                                break
                            # if less than 48 hours, just 50 percent of cost returns
                            else:
                                old_balance = info[4]
                                new_balance = float(info[4])+((total_price)*0.5)
                                info[4]= str(new_balance)
                                lines[i]= ",".join(info)+"\n"
                                print("_"*80)
                                print("returning was successful!\n 50 percent of cost was returned!")
                                print(f"you had {float(old_balance)} dollars \n now your new balance is {info[4]}")
                                print("_"*80)
                                break
                    with open("users_info.txt","w") as file:
                        file.writelines(lines)
        if reserve_found=="No":
            print("_"*80)
            print("sorry! reserve wasn't found!")
            print("_"*80)
def update_average_rates(room_id):
    # every time user's rate is registered, average of rates for that room updates.  
    with open("comment_point_users.json","r") as file:
        rates = []
        data = json.load(file)
        for info in data:
            if info["room_id"]==room_id:
                rates.append(info["rate"])
    average_rate = sum(rates)/len(rates)
    with open("rooms_info.json","r") as file:
        data = json.load(file)
        for info in data:
            if info["room_id"]== room_id:
                info["average_rate"] = average_rate
    with open("rooms_info.json","w") as file:
        json.dump(data,file,indent=4)