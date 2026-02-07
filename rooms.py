from abc import ABC,abstractmethod
from random import choice
from textwrap import indent
class Room(ABC):
    def __init__(self,room_id,base_price,facilities,capacity,available,status):
        self.room_id = room_id
        self.base_price = base_price
        self.facilities = facilities
        self.capacity = capacity
        self.available = available
        self.status = status
    @abstractmethod
    def calculate_price(self,num_night):
        pass
class Single_Room(Room):
    def calculate_price(self, num_night):
        calculation = (self.base_price)*(num_night)+20
        print(f"""tatal cost: {calculation}
                  20 dollars for services besides base price""")
        return calculation
class Double_Room(Room):
    def calculate_price(self, num_night):
        calculation = (self.base_price)*(num_night)+30
        print(f"""tatal cost: {calculation}
                  30 dollars for services besides base price""")  
        return calculation     
class Suite_Room(Room):
    def calculate_price(self, num_night):
        calculation = (self.base_price)*(num_night)+10
        print(f"""tatal cost: {calculation}
                  10 dollars for services besides base price""")
        return calculation
import json
with open("rooms_info.json","r") as file:
    list_rooms = []
    file = json.load(file)
    for line in file:
        if line["type"]== "single":
            single_room = Single_Room(line["room_id"],line["base_price"],line["facilities"],line["capacity"],line["available"],line["status"])
            if line["available"]=="True":
                list_rooms.append(single_room)         
        elif line["type"]== "double":
            double_room = Double_Room(line["room_id"],line["base_price"],line["facilities"],line["capacity"],line["available"],line["status"])
            if line["available"]=="True":
                list_rooms.append(double_room)
        elif line["type"]== "suite":
            suite_room = Suite_Room(line["room_id"],line["base_price"],line["facilities"],line["capacity"],line["available"],line["status"])
            if line["available"]=="True":
                list_rooms.append(suite_room)
def show_rooms():
    for room in list_rooms:
        if type(room)==Single_Room:
            print(f"a single room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40)
        if type(room)==Double_Room:
            print(f"a double room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40)
        if type(room)==Suite_Room:
            print(f"a suite room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}") 
            print(f"status:{room.status}")
            print("_"*40)   
def search_rooms_price():
    low_price = input("enter type of price range,first low price limit: (for example 50 dollars)")
    high_price = input("then high price limit: (for example 100 dollars)")
    list_choice = []
    for room in list_rooms:
        if room.base_price>= float(low_price) and room.base_price<= float(high_price):
            list_choice.append(room)
    print("this result is based on your choice:")
    if list_choice==[]:
        print("sorry we couldn't find any result!")
    for room in list_choice:
        if type(room)==Single_Room:
            print(f"a single room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40)
        if type(room)==Double_Room:
            print(f"a double room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40)
        if type(room)==Suite_Room:
            print(f"a suite room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40)
    return list_choice 
def search_rooms_facilities():
    facilities_choice = input("enter facilities that you want: (choice between: tv,fridge,wifi)")
    facil_choice_list = facilities_choice.split(",")
    if facilities_choice=="tv":
        facil_choice_list = ["tv"]
    elif facilities_choice=="fridge":
        facil_choice_list = ["fridge"]
    elif facilities_choice=="wifi":
        facil_choice_list = ["wifi"]
    list_choice = []
    for room in list_rooms:
        if room.facilities == facil_choice_list:
            list_choice.append(room)
    print("this result is based on your choice:")
    if list_choice==[]:
        print("sorry we couldn't find any result!")
    for room in list_choice:
        if type(room)==Single_Room:
            print(f"a single room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40)
        if type(room)==Double_Room:
            print(f"a double room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40)
        if type(room)==Suite_Room:
            print(f"a suite room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40) 
    return list_choice
from datetime import datetime
def calculate_reserve(num_room,check_in,check_out,num_people):
    existing_in=datetime.strptime(check_in,"%Y_%m_%d")
    existing_out=datetime.strptime(check_out,"%Y_%m_%d")
    for room in list_rooms:
        if room.room_id == num_room and room.capacity == num_people:
            if room.status == "canceled":
                num_night = (existing_out-existing_in).days
                calculation=room.calculate_price(num_night) 
                print("_"*40)
                return calculation
            elif room.status == "completed":
                num_night = (existing_out-existing_in).days
                calculation=room.calculate_price(num_night) 
                print("_"*40)      
                return calculation           
            elif room.status == "active":
                num_night = (existing_out-existing_in).days
                calculation=room.calculate_price(num_night) 
                print("_"*40)
                return calculation
    print("we do not have this room!,enter correct number for room you wanted!")
def showroom_basedate(check_in,check_out):
    rooms=[]
    check_in=datetime.strptime(check_in,"%Y_%m_%d")
    check_out=datetime.strptime(check_out,"%Y_%m_%d")
    for room in list_rooms:
        if room.status=="completed":
            rooms.append(room)
        elif room.status=="canceled":
            rooms.append(room)
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
            print(f"a single room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40)
        if type(room)==Double_Room:
            print(f"a double room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}")
            print(f"status:{room.status}")
            print("_"*40)
        if type(room)==Suite_Room:
            print(f"a suite room with this information:")
            print(f"room id:{room.room_id} |,base price:{room.base_price} |,facilities:{room.facilities} |,capacity:{room.capacity}") 
            print(f"status:{room.status}")
            print("_"*40)
def payment(username,calculation):
    print("in pay...")
    with open("users_info.txt","r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            info = line.strip().split(",") 
            if info[2]==username:
                if calculation<= int(info[4]):
                    subtraction = int(info[4])-calculation
                    info[4]=f"{subtraction}"
                    lines[i]= ",".join(info)+"\n"
                    print("your payment was successful!")
                    print(f"now your new balance is {int(info[4])}")
                    print("_"*40)
                    can_reserve = True 
                    break
                else:
                    print("Wrong! your balance is not enough!")
                    print("_"*40)
                    can_reserve = False
                    break
        with open("users_info.txt","w") as file:
            file.writelines(lines)
        return can_reserve
def final_reserve(username,room_num,check_in,check_out,people_num,calculation):
    #storing data and change status for room that has reserved!
    with open("rooms_info.json","r") as file:
        data = json.load(file)
        for info in data:
            if info["room_id"]== room_num:
                info["status"] = "active"
    with open("rooms_info.json","w") as file:
        json.dump(data,file,indent=4)
    #storing data for reserving , in file(reserve_info.json)
    with open("reserve_info.json","r") as file:
        data = json.load(file)
        info_new_reserve={"username":username,"room_id":room_num,"check_in":check_in,"check_out":check_out,
                          "capacity":people_num,"total_price":calculation,"status":"active" }
        data.append(info_new_reserve)
    with open("reserve_info.json","w") as file:
        json.dump(data,file,indent=4)
    print("your reservation was SUCCESSFUl!")
    print("you can see the information for your reservation...")
    print(f"\n Username:{username}\n\n Room_id:{room_num}\n\n check_in date:{check_in}\n\n check_out date:{check_out}\n\n Capacity:{people_num}\n\n Total_price:{calculation}\n\n status:active\n")
    print("_"*40)
def list_reservations(username):
    with open("reserve_info.json","r") as file:
        data = json.load(file)
        user_found = "No"
        for info in data:
            if info["username"]==username:
                user_found = "Yes"
                print("_"*40)
                print(f"\n Room_id:{info["room_id"]}\n\n check_in date:{info["check_in"]}\n\n check_out date:{info["check_out"]}\n\n Capacity:{info["capacity"]}\n\n Total_price:{info["total_price"]}\n\n Status:{info["status"]}\n")
                print("_"*40)
        if user_found == "No":
            print("_"*40)
            print("No reservation yet!")
            print("_"*40)
def filter_list_reservations(username):
    with open("reserve_info.json","r") as file:
        data = json.load(file)
        user_found = "No"
        for info in data:
            if info["username"]==username and info["status"]=="active":
                user_found = "Yes"
                print("_"*40)
                print(f"\n Room_id:{info["room_id"]}\n\n check_in date:{info["check_in"]}\n\n check_out date:{info["check_out"]}\n\n Capacity:{info["capacity"]}\n\n Total_price:{info["total_price"]}\n\n Status:{info["status"]}\n")
                print("_"*40)
        if user_found == "No":
            print("_"*40)
            print("No active reservation yet!")
            print("_"*40)
def increasing_balance(username):
    amount = input("How many dollars do you want to increase?")
    print("while proccessing your account...")   
    with open("users_info.txt","r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            info = line.strip().split(",") 
            if info[2]==username:
                old_balance= int(info[4])
                new_balance =int(info[4])+int(amount)
                info[4]= str(new_balance)
                lines[i]= ",".join(info)+"\n"
                print("increasing your balance was successful!")
                print("_"*40)
                print(f"you had {old_balance}\nnow your new balance is {int(info[4])}")
                print("_"*40)
                break
        with open("users_info.txt","w") as file:
            file.writelines(lines)
