import csv
from faker import Faker
from random import randint, choice, uniform
from datetime import timedelta
# Initialize Faker
fake = Faker()
from datetime import datetime, timedelta


# Define the number of rows to generate
num_rows = [3600,4000,56,1400,3,0,42,20,0,12883,0,0,200091]

# Define possible values for certain fields
manufacturers = ['TugCo', 'HeavyTugs', 'SkyTugs','J&JTugCo','UngerTugging','TugAHawk','GuTaTuG']
locations = ['LAX', 'JFK', 'ORD', 'ATL', 'DFW', 'TLV', 'SFO','LON','CDG','WAW','EWR','AUH','IAH','SEA']
terminals = ["A","B","C","D"]
fuel_types = ['JetA', 'JetB', 'Avgas']
directions = ["EW","NS","NESW","NWSE"]
weights = [50000,100000,250000,300000,450000,700000,1000000]
trucks =[]
plane_tugs = []
airplanes_list = []
takeoffs = []
jet_bridges = []
tuggings = []
airplane_model_list = []
refueling = []
truck_loads = []
runway_list = []
airplanes = [
    "Boeing 747",
    "Airbus A320",
    "Embraer E190",
    "Bombardier CRJ900",
    "Boeing 787",
    "Airbus A380",
    "Bombardier Q400",
    "Boeing 737",
    "Airbus A350",
    "Embraer E175",
    "Boeing 777",
    "Airbus A330",
    "Bombardier CRJ700",
    "Embraer E195",
    "Boeing 757",
    "Airbus A319",
    "Bombardier CRJ200",
    "Boeing 767",
    "Airbus A321",
    "Embraer E170"
]
plane_fuel_map = {
    "Boeing 747": ("Avgas", 970000),  # Weight in pounds
    "Airbus A320": ("JetA", 162000),  # Weight in pounds
    "Embraer E190": ("JetB", 115000),  # Weight in pounds
    "Bombardier CRJ900": ("Avgas", 84000),  # Weight in pounds
    "Boeing 787": ("JetA", 502000),  # Weight in pounds
    "Airbus A380": ("JetB", 610000),  # Weight in pounds
    "Bombardier Q400": ("JetA", 64600),  # Weight in pounds
    "Boeing 737": ("Avgas", 174200),  # Weight in pounds
    "Airbus A350": ("JetB", 555000),  # Weight in pounds
    "Embraer E175": ("JetA", 81800),  # Weight in pounds
    "Boeing 777": ("Avgas", 656000),  # Weight in pounds
    "Airbus A330": ("JetB", 507000),  # Weight in pounds
    "Bombardier CRJ700": ("JetA", 75000),  # Weight in pounds
    "Embraer E195": ("Avgas", 97000),  # Weight in pounds
    "Boeing 757": ("JetB", 255000),  # Weight in pounds
    "Airbus A319": ("Avgas", 166000),  # Weight in pounds
    "Bombardier CRJ200": ("JetB", 49500),  # Weight in pounds
    "Boeing 767": ("JetA", 395000),  # Weight in pounds
    "Airbus A321": ("Avgas", 206000),  # Weight in pounds
    "Embraer E170": ("JetA", 48500)  # Weight in pounds
}

# Function to write CSV files
def write_csv(table_name, header, data):
    filename = f"{table_name}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

# Generate data
def generate_airplane_tug(index):
    return [fake.license_plate(), choice(weights), randint(1, 15), choice(manufacturers), choice(locations)]

def generate_fueling_truck():
    return [fake.license_plate(), randint(200, 800), randint(1, 20), fake.date_this_decade().strftime("%Y-%m-%d"), choice(locations)]

def generate_runway(index):
    return [index%4, randint(1000, 2000), randint(200000, 500000), directions[randint(0, 3)], locations[int(index/4)]]

def generate_gate(index):
    gate_num = index%100
    local_location = locations[int(index/100)]
    jet_bridges.append(generate_jet_bridge(index, gate_num, local_location))
    return [gate_num, local_location]

def generate_fuel_type(index):
    return [fuel_types[index], round(uniform(1.5, 5.0), 2)]

def generate_jet_bridge(index, gate_num, local_location):
    return [index, randint(1, 30), randint(5000, 15000), gate_num,local_location]

def generate_fuel_stock():
    location = locations[int(index/3)]
    return [randint(10000, 100000), locations[int(index/3)], fuel_types[index%3]]

def generate_airplane_type(index):
    return [airplanes[index], randint(50, 500), randint(200, 1000), randint(1000, 15000), randint(5, 30), plane_fuel_map[airplanes[index]][0],plane_fuel_map[airplanes[index]][1] ]#added in weight

def generate_truck_load(truck, plane):
    truck_loads.append([randint(5000, 20000), fake.date_this_year().strftime("%Y-%m-%d"), truck[0], truck[4], plane_fuel_map[plane[4]][0]])

def generate_airplane(index):
    manufacture_date = fake.date_this_decade() - timedelta(days=randint(365*5, 365*20))  # Random manufacture date within the last 5 to 20 years
    # Add random years (0-2) and random months (3-10) to the manufacture date to get the in-service date
    in_service_date = manufacture_date + timedelta(days=randint(0, 365*2))
    return [index, manufacture_date.strftime("%Y-%m-%d"), in_service_date.strftime("%Y-%m-%d"), 1, choice(airplanes)]

def generate_refueling(date, plane, runway):
    date = fake.date_this_decade()
    trucks_local = [truck for truck in trucks if truck[4] == runway[4]]
    truck = trucks_local[randint(0, len(trucks_local) - 1)]
    generate_truck_load(truck, plane)
    refueling.append([date.strftime("%Y-%m-%d"), randint(5000, 20000), truck[0], plane[0]])


def generate_tugs(location,date, plane):
    canHold = False #ensure the tug can hold the plane's weight
    local_tugs = [tug for tug in plane_tugs if location == tug[4]]
    while canHold == False:
        tug = local_tugs[randint(0,len(local_tugs)-1)]
        if tug[1] > plane_fuel_map[plane[4]][1]:
            canHold = True
    gate = [gate[3] for gate in jet_bridges if gate[4] == location]
    return [date.strftime("%Y-%m-%d"), randint(0, 5000), tug[0], plane[0],gate[randint(0,len(gate) -1)]]

def generate_landing_takeoff():
        plane = airplanes_list[randint(0,len(airplanes_list)-1)]
        runway = runway_list[randint(0,len(runway_list)-1)]
        date = fake.date_this_year()
        date2 = date +  timedelta(days=randint(0, 3))
        tuggings.append(generate_tugs(runway[4],date, plane))
        generate_refueling(date, plane, runway)
        takeoffs.append([date.strftime("%Y-%m-%d"), 0, plane[0], runway[4], runway[0]])
        takeoffs.append([date2.strftime("%Y-%m-%d"), 1,plane[0], runway[4], runway[0]])

# Define headers for each table
headers = {
    "AirplaneTug": ["LicenseNumber", "WeightCapacity", "YearsInUse", "Manufacturer", "Location"],
    "FuelingTruck": ["LicensePlate", "Horsepower", "YearsInUse", "LastMaintained", "Location"],
    "Runway": ["Number","Length", "WeightCapacity", "Orientation", "Location"],
    "Gate": ["GateNumber", "Location"],
    "FuelType": ["TypeOfFuel", "Price"],
    "JetBridge": ["SerialNumber", "YearsInUse", "WeightLimit", "GateNumber","Location"],
    "FuelStock": ["LitersInStock", "Location", "TypeOfFuel"],
    "AirplaneType": ["MakeAndModel", "Capacity", "MaxSpeed", "Range", "LifeTime", "TypeOfFuel","Weight"],
    "TruckLoad": ["LitersOfFuel", "Date", "LicensePlate", "Location","TypeOfFuel"],
    "Airplane": ["SerialNumber", "DateManufactored", "DateAcquired", "In_Service", "MakeAndModel"],
    "Refueling": ["Date", "Amount_of_Fuel_Delivered", "LicensePlate", "SerialNumber"],
    "Tugs": ["Date", "FuelRemainingAfterTug", "LicenseNumber", "SerialNumber", "Gate"],
    "Landings_Takeoff" : ["Date", "LT","Plane","Location","Runway"]
}

i = 0
# Generate and write data for each table
for table_name, header in headers.items():
    data = []
    index = 0
    for _ in range(num_rows[i]):
        if table_name == "Runway":
            runway = generate_runway(index)
            runway_list.append(runway)
            data.append(runway)
        elif table_name == "AirplaneTug":
            plane_tug = generate_airplane_tug(index)
            plane_tugs.append(plane_tug)
            data.append(plane_tug)
        elif table_name == "FuelingTruck":
            truck = generate_fueling_truck()
            trucks.append(truck)
            data.append(truck)
        elif table_name == "FuelType":
            data.append(generate_fuel_type(index))
        elif table_name == "Gate":
            data.append(generate_gate(index))
        elif table_name == "JetBridge":#dependent on Gate
            data.append(generate_jet_bridge(index))
        elif table_name == "FuelStock":# dependant on fueltype
            data.append(generate_fuel_stock())
        elif table_name == "AirplaneType":
            airplane_model = generate_airplane_type(index)
            airplane_model_list.append(airplane_model)
            data.append(airplane_model)
        elif table_name == "TruckLoad": #dependent on fuel stock and fuel truck
            data.append(generate_truck_load())
        elif table_name == "Airplane":# depenent on airplane type
            airplane = generate_airplane(index)
            airplanes_list.append(airplane)
            data.append(airplane)
        elif table_name == "Tugs":#dependent on airplanes and airplanetug
            data.append(generate_tugs())
        elif table_name == "Landings_Takeoff":
            generate_landing_takeoff()
        index+=1
    print(header)
    i += 1

    write_csv(table_name, header, data)
write_csv("Refueling", headers["Refueling"], refueling)
write_csv("TruckLoad", headers["TruckLoad"], truck_loads)
write_csv("JetBridge", headers["JetBridge"], jet_bridges)
write_csv("Landings_Takeoff", headers["Landings_Takeoff"], takeoffs)
write_csv("Tugs", headers["Tugs"], tuggings)

print("CSV files have been generated successfully.")
