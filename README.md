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
##### Select Queries
1) Query: SELECT makeandmodel, COUNT(*) FROM airplane GROUP BY makeandmodel;
   * Retrieve the make and model of each airplane.
   * Count how many airplanes exist for each make and model.
   * Group the results by the make and model.
2) Query: SELECT * FROM airplane ORDER BY datemanufactored;
   * Select all columns from the airplane table.
   * Sort the results by the date the airplanes were manufactured, in ascending order.
3) Query: SELECT serialnumber FROM public.airplane WHERE makeandmodel IN (SELECT makeandmodel FROM public.airplanetype WHERE makeandmodel LIKE 'Boeing%');
   * Select the serial number of airplanes.
   * Filter to include only those airplanes whose make and model match any make and model from the airplanetype table starting with 'Boeing'.
4) Query: SELECT a.serialnumber, a.makeandmodel FROM airplane a INNER JOIN airplanetype b ON a.makeandmodel = b.makeandmodel WHERE b.range > 13000;
   * Select the serial number and make and model of airplanes.
   * Perform an inner join between the airplane and airplanetype tables based on matching make and model.
   * Include only those airplanes where the range in the airplanetype table is greater than 13,000.
##### Update Queries
5) Query: UPDATE airplanetype SET range = 10000 WHERE makeandmodel = 'Airbus A319';
   * Update the range value in the airplanetype table.
   * Set the range to 10,000 for all entries where the make and model is 'Airbus A319'.
6) Query: UPDATE fueltype SET price = 5.0 WHERE typeoffuel = 'Avgas';
   * Update the price in the fueltype table.
   * Set the price to 5.0 for the fuel type 'Avgas'.
##### Delete Queries
7) Query: DELETE FROM tugs WHERE date < CURRENT_DATE - INTERVAL '5 months';
   * Delete entries from the tugs table.
   * Remove records where the date is older than 5 months from the current date.
8) Query: DELETE FROM truckload WHERE date < CURRENT_DATE - INTERVAL '5 months';
   * Delete entries from the truckload table.
   * Remove records where the date is older than 5 months from the current date.
#### Parameterized Queries
1) Query: PREPARE get_airplanes_by_date_location (date, text) AS SELECT a.* FROM airplane a JOIN landingtakingoff l ON a.serialnumber = l.serialnumber WHERE l.date = $1 AND l.location = $2;
   * Prepare a statement named get_airplanes_by_date_location that accepts a date and a text string as parameters.
   * Select all columns from the airplane table.
   * Join the airplane table with the landingtakingoff table on the serial number.
   * Filter the results to include only those records where the date matches the provided date parameter and the location matches the provided text parameter.
2) PREPARE get_fueling_trucks_by_fuel (text) AS SELECT f.* FROM fuelingtruck f JOIN truckload t ON f.licenseplate = t.licenseplate WHERE t.typeoffuel = $1 ORDER BY f.lastmaintained;
   * Prepare a statement named get_fueling_trucks_by_fuel that accepts a text string as a parameter.
   * Select all columns from the fuelingtruck table.
   * Join the fuelingtruck table with the truckload table on the license plate.
   * Filter the results to include only those records where the type of fuel matches the provided text parameter.
   * Order the results by the last maintained date of the fueling trucks.
3) Query: PREPARE get_gates_by_event_count (int) AS SELECT g.* FROM gate g WHERE (SELECT COUNT(*) FROM landingtakingoff l WHERE l.gatenumber = g.gatenumber AND l.location = g.location) > $1;
   * Prepare a statement named get_gates_by_event_count that accepts an integer as a parameter.
   * Select all columns from the gate table.
   * Filter the results to include only those gates where the count of events (landings or takeoffs) associated with that gate is greater than the provided integer parameter.
4) Query: PREPARE get_tugs_by_location_count_manufacturer (text) AS SELECT at.manufacturer, COUNT(*) FROM airplanetug at JOIN tugs t ON at.licensenumber = t.licensenumber WHERE t.location = $1 GROUP BY at.manufacturer ORDER BY at.manufacturer;
   * Prepare a statement named get_tugs_by_location_count_manufacturer that accepts a text string as a parameter.
   * Select the manufacturer of airplane tugs and the count of tugs for each manufacturer.
   * Join the airplanetug table with the tugs table on the license number.
   * Filter the results to include only those tugs located at the provided location parameter.
   * Group the results by manufacturer.
   * Order the results by manufacturer.

![image](https://github.com/ephmonster/miniProjectDatabase/assets/33190140/477b32de-e184-4eaf-a519-15b977ac8799)


#### Timing
| Query Number | RunTime No Indexing | Runtime with Indexing | Relevant Index|
|----------|----------|----------|----------|
| 1 | 6.357 | 8.014 | |
| 2 | 7.828 | 7.749 | |
| 3 | 10.075 | 2.511 | idx_plane_makeandmodel | 
| 4 | 4.097 | 4.425 | idx_tug_makeandmodel | 
| 5 | 6.655 | 2.460 | idx_plane_makeandmodel |
| 6 | 0.215 | 0.169 | |
| 7 | 475.743 | 366.276 | |
| 8 | 478.449 | 565.209 | |
