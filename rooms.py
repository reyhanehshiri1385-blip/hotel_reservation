from abc import ABC,abstractmethod
from random import choice
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

class Double_Room(Room):
    def calculate_price(self, num_night):
        calculation = (self.base_price)*(num_night)+30
        print(f"""tatal cost: {calculation}
                  30 dollars for services besides base price""")       
class Suite_Room(Room):
    def calculate_price(self, num_night):
        calculation = (self.base_price)*(num_night)+10
        print(f"""tatal cost: {calculation}
                  10 dollars for services besides base price""")
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
def reservation1(username,num_room,check_in,check_out,num_people):
    existing_in=datetime.strptime(check_in,"%Y_%m_%d")
    existing_out=datetime.strptime(check_out,"%Y_%m_%d")
    for room in list_rooms:
        if room.room_id == num_room and room.capacity == num_people:
            if room.status == "canceled":
                num_night = (existing_out-existing_in).days
                room.calculate_price(num_night) 
                print("_"*40)
            elif room.status == "completed":
                num_night = (existing_out-existing_in).days
                room.calculate_price(num_night) 
                print("_"*40)                                   
            elif room.status == "active":
                num_night = (existing_out-existing_in).days
                room.calculate_price(num_night) 
                print("_"*40)
        else:
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
            file = open("reserve_info.json")
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
    #############################
    
            
            