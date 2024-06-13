# Airplane Equipment Database 

## Ephraim Ungar and Eli Hawk

## Project Proposal


Our goal is to represent a database which stores data for the main equipment for an airport, such as airplanes, fueling equimpment, airplane tugs, jetbridge, etc.

Our objective is streamline the management and maintainence of the airport equipment.

### Target Users
The target users of our database are:
  1) Airport managers
  2) Maintainance staff
  3) Logistics coordinaters

### Use cases of our database include: 
1) Inventory management, so that we have accurate information regarding the current state of the inventory.
2) Maintainance scheduling, i.e. information regarding the current state of the equipment
3) Fuel management, data representing the appropriate kinds of fuel for different airplanes as well as information regarding the refueling
4) Runway scheduling, to store information regarding runway scheduling
(5) Tug scheduling

### ERD Entities:
1) Airplane type: Different airplane types have varying specifications and capacities. Tracking these helps in operational planning and maintenance. This entity supports the classification and management of different airplane models.
2) Airplane: Airplanes are central to airport operations. Tracking their serial numbers, manufacturing dates, acquisition dates, and service status is crucial for maintenance and operational planning. This entity allows the system to manage airplane details, schedule maintenance, and monitor their operational status.
3) Runway: Runways are vital infrastructure. Tracking their attributes ensures they can accommodate various aircraft and are maintained properly. This entity aids in runway management, ensuring they meet operational requirements and are available for landings and takeoffs.
4) Jetbridge: Jet bridges facilitate passenger boarding and deboarding. Their maintenance and operational status are critical for efficient gate operations. This entity ensures jet bridges are tracked for maintenance schedules and operational readiness.
5) Gate: Gates are essential for boarding and deboarding passengers. Managing their availability and status is crucial for airport operations. 
6) Fueltype: Different fuel types are used for various aircraft. Managing fuel types ensures appropriate refueling. This entity helps in managing fuel inventory and pricing.
7) Fuelstock: Managing fuel stock is vital for refueling operations. Tracking fuel quantities ensures adequate supply. This entity enables monitoring fuel levels to prevent shortages and optimize fuel orders.
8) Fueling truck: Fueling trucks are critical for refueling airplanes. Their maintenance and operational status directly impact refueling efficiency. This entity helps schedule maintenance and track the availability of fueling trucks.

### Limitations
The current ERD does not cover: 
  1) Management of personnel operating the equipment.
  2) The financial aspects of maintenance and operations.
  3) Handling and tracking incidents or malfunctions of equipment.
  4) Ordering of new parts for broken airplane parts.
  5) Equipment for loading/unloading cargo.
  6) Equipment for loading/unloading food/waste from cabin.

![Airplane_Equipment_DSD](https://github.com/ephmonster/miniProjectDatabase/assets/33190140/c29faafe-1aef-48d3-b853-d13f6e58d4c9)


![DSDImage](https://github.com/ephmonster/miniProjectDatabase/assets/71876859/a612c6c7-3bce-4a00-92fb-aa7b711a1474)

![Screenshot (5)](https://github.com/ephmonster/miniProjectDatabase/assets/71876859/64b1450f-40db-4297-8d74-118eaba3543e)

### Data Generation
#### Amount of Data
  1) Airplane Type:  20 different types of planes with varying manufacturers and Make and Models
  2) Airplane: 12884, each plane is a type of 'Airplane Type'
  3) FuelingTruck: 4000
  4) Airplane tug: 3600
  5) Fuel Stock: 42
  6) Fuel Type: 3
  7) Gates: 1400
  8) JetBridge: 1400
  9) TruckLoads: 200091
  10) LandingsTakeoff: 400182
  11) Refuelings: 200091
  12) Runways: 52

#### Method of Data Generation
*Note:* The python script used to generate the data is on GitHub with the name: airplane_equipment_data_generation.py
1) We created a list of various airports we will simulate airplane and equipment usage.
2) Then, we created the vairous types of critical equipment in significant amounts giving a few hundred Refueling Trucks and Tugs at each airport.
3) Created planes to land and takeoff by airports.
4) Generated 200091 Takeoff and landings, for each time a plane lands at the airport there is a tug that tugs it, a truckload full of fuel, and a refueling that the truck gives to that plane which has date within a few days of the planes landing, and is before its takeoff.
5) The Takeoffs and Landings are randomized, simulating variying capacties of planes taking off and landing at the 14 airports. For each time a plane lands at an airport there is an entry of that plane taking off as well within a few days.
6) Each Takeoff/Landing has a specific runway at the airport associated with it that the plane landed on.
7) For each truckload that is generated with a refueling of the plane it is ensured that the truck is loaded with the proper type of fuel for that plane.
8) Each airport has 100 gates and each gate has a jet bridge to connect it to the plane.

### Backups

#### Data Dump Command

### Queries
#### Regular Queries
1) 
2)  Get all serial numbers of airplanes manufactured by 'Boeing'
3)  Get count of all airplane tugs by manufacturer at an airport
##### Update Queries
1)  Update price for a type of fuel
2)  Update airplane range (e.g. if it got an engine/fueltank upgrade with increased range)
