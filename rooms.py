from abc import ABC,abstractmethod
class Room(ABC):
    def __init__(self,room_id,base_price,facilities,capacity,available):
        self.__room_id = room_id
        self.__base_price = base_price
        self.__facilities = facilities
        self.__capacity = capacity
        self.__available = available
    @abstractmethod
    def calculate_price(self,num_night):
        pass
class Single_Room(Room):
    def calculate_price(self, num_night):
        pass
class Double_Room(Room):
    def calculate_price(self, num_night):
        pass
class Suite_Room(Room):
    def calculate_price(self, num_night):
        pass
import json
with open("rooms_info.json","r") as file:
    list_rooms = []
    file = json.load(file)
    for line in file:
        if line["type"]== "single":
            single_room = Single_Room(line["room_id"],line["base_price"],line["facilities"],line["capacity"],line["available"])
            if line["available"]=="True":
                list_rooms.append(single_room)         
        elif line["type"]== "double":
            double_room = Double_Room(line["room_id"],line["base_price"],line["facilities"],line["capacity"],line["available"])
            if line["available"]=="True":
                list_rooms.append(double_room)
        elif line["type"]== "suite":
            suite_room = Suite_Room(line["room_id"],line["base_price"],line["facilities"],line["capacity"],line["available"])
            if line["available"]=="True":
                list_rooms.append(suite_room)
def show_rooms():
    for room in list_rooms:
        if type(room)==Single_Room:
            print(f"a single room with this information:")
            print(f"base price:{room._Room__base_price} ,facilities:{room._Room__facilities} ,capacity:{room._Room__capacity}")
            print("_"*40)
        if type(room)==Double_Room:
            print(f"a double room with this information:")
            print(f"base price:{room._Room__base_price} ,facilities:{room._Room__facilities} ,capacity:{room._Room__capacity}")
            print("_"*40)
        if type(room)==Suite_Room:
            print(f"a suite room with this information:")
            print(f"base price:{room._Room__base_price} ,facilities:{room._Room__facilities} ,capacity:{room._Room__capacity}")   
            print("_"*40)   
def search_rooms_price():
    low_price = input("enter type of price range,first low price limit: (for example 50 dollars)")
    high_price = input("then high price limit: (for example 100 dollars)")
    list_choice = []
    for room in list_rooms:
        if room._Room__base_price>= float(low_price) and room._Room__base_price<= float(high_price):
            list_choice.append(room)
    print("this result is based on your choice:")
    for room in list_choice:
        if type(room)==Single_Room:
            print(f"a single room with this information:")
            print(f"base price:{room._Room__base_price} ,facilities:{room._Room__facilities} ,capacity:{room._Room__capacity}")
            print("_"*40)
        if type(room)==Double_Room:
            print(f"a double room with this information:")
            print(f"base price:{room._Room__base_price} ,facilities:{room._Room__facilities} ,capacity:{room._Room__capacity}")
            print("_"*40)
        if type(room)==Suite_Room:
            print(f"a suite room with this information:")
            print(f"base price:{room._Room__base_price} ,facilities:{room._Room__facilities} ,capacity:{room._Room__capacity}")   
            print("_"*40) 
def search_rooms_facilities():
    facilities_choice = input("enter facilities that you want: (choice between: tv,fridge,wifi)")
    facil_choice_list = facilities_choice.split(",")
    list_choice = []
    for room in list_rooms:
        if room._Room__facilities == facil_choice_list:
            list_choice.append(room)
    print("this result is based on your choice:")
    for room in list_choice:
        if type(room)==Single_Room:
            print(f"a single room with this information:")
            print(f"base price:{room._Room__base_price} ,facilities:{room._Room__facilities} ,capacity:{room._Room__capacity}")
            print("_"*40)
        if type(room)==Double_Room:
            print(f"a double room with this information:")
            print(f"base price:{room._Room__base_price} ,facilities:{room._Room__facilities} ,capacity:{room._Room__capacity}")
            print("_"*40)
        if type(room)==Suite_Room:
            print(f"a suite room with this information:")
            print(f"base price:{room._Room__base_price} ,facilities:{room._Room__facilities} ,capacity:{room._Room__capacity}")   
            print("_"*40) 
