# Airplane Equipment Database 

## Ephraim Unger and Eli Hawk

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
