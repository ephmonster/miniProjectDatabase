# Airplane Equipment Database 

## Ephraim Ungar and Eli Hawk

## Project Proposal

## Stage 1
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

### [Data Generation](airplane_equipment_data_generation.py)
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

## Stage 2
### Backups

#### [Data Dump Command](DumpScript)

We backed up our queries and restored the database using INSERT statements and default pg_dump
pg_dump --file "backupSQL.sql" --host "localhost" --port "5432" --username "postgres" --format=c --large-objects --inserts --rows-per-insert "1000" --create --clean --if-exists --verbose "MiniProject"
pg_restore --host "localhost" --port "5432" --username "postgres" --dbname "MiniProject" --clean --if-exists --disable-triggers --verbose "backupSQL.sql
#### [BackupSQL](backupSQL.sql)
#### [BackupSQLlog](backupSQL.log)
pg_dump --file "backupPSQL.sql" --host "localhost" --port "5432" --username "postgres" --format=c --large-objects --verbose "MiniProject" 
pg_restore --host "localhost" --port "5432" --username "postgres" --dbname "MiniProject" --clean --if-exists --disable-triggers --verbose "backupPSQL.sql"
#### [BackupPSQL](backupPSQL.sql)
#### [BackupPSQLlog](backupPSQL.log)

### Queries
#### [Regular Queries](Queries.sql)
##### Select Queries
1) Query: SELECT makeandmodel, COUNT(*) FROM airplane GROUP BY makeandmodel;
   * Retrieve the make and model of each airplane.
   * Count how many airplanes exist for each make and model.
   * Group the results by the make and model.
   * Need: Logistics coordiantor needs to know how many airplanes they have of each type.
2) Query: SELECT * FROM airplane ORDER BY datemanufactored;
   * Select all columns from the airplane table.
   * Sort the results by the date the airplanes were manufactured, in ascending order.
   * Need: Mechanic department can plan for maintance based off of how old a plane is.
3) Query: SELECT serialnumber FROM public.airplane WHERE makeandmodel IN (SELECT makeandmodel FROM public.airplanetype WHERE makeandmodel LIKE 'Boeing%');
   * Select the serial number of airplanes.
   * Filter to include only those airplanes whose make and model match any make and model from the airplanetype table starting with 'Boeing'.
   * Need: Safety inspector can view all Boeing planes after the Boeing recall.
4) Query: SELECT a.serialnumber, a.makeandmodel FROM airplane a INNER JOIN airplanetype b ON a.makeandmodel = b.makeandmodel WHERE b.range > 13000;
   * Select the serial number and make and model of airplanes.
   * Perform an inner join between the airplane and airplanetype tables based on matching make and model.
   * Include only those airplanes where the range in the airplanetype table is greater than 13,000.
   * Need: Flight planner planning long haul flights.
##### Update Queries
5) Query: UPDATE airplanetype SET range = 10000 WHERE makeandmodel = 'Airbus A319';
   * Update the range value in the airplanetype table.
   * Set the range to 10,000 for all entries where the make and model is 'Airbus A319'.
   * Need: Mechanic updating range of plane after parts upgrade.
6) Query: UPDATE fueltype SET price = 5.0 WHERE typeoffuel = 'Avgas';
   * Update the price in the fueltype table.
   * Set the price to 5.0 for the fuel type 'Avgas'.
   * Gasoline aquisition specialist can reset price to accuralty reflect the price 
##### Delete Queries
We did not use Cascading Deletes, we choose queries that specifically would not cause loss of data that represents physical entitites which are zoned in to only delete data from that table.

7) Query: DELETE FROM tugs WHERE date < CURRENT_DATE - INTERVAL '5 months';
   * Delete entries from the tugs table.
   * Remove records where the date is older than 5 months from the current date.
   * Database manager can clean up old data and remove it from storage.
8) Query: DELETE FROM truckload WHERE date < CURRENT_DATE - INTERVAL '5 months';
   * Delete entries from the truckload table.
   * Remove records where the date is older than 5 months from the current date.
   * Database manager can clean up old data and remove it from storage.
#### [Parameterized Queries](ParamQueries.sql)
#### [ParamQuery logs](param_query_log.log)
1) Query: PREPARE get_airplanes_by_date_location (date, text) AS SELECT a.* FROM airplane a JOIN landingtakingoff l ON a.serialnumber = l.serialnumber WHERE l.date = $1 AND l.location = $2;
   * Prepare a statement named get_airplanes_by_date_location that accepts a date and a text string as parameters.
   * Select all columns from the airplane table.
   * Join the airplane table with the landingtakingoff table on the serial number.
   * Filter the results to include only those records where the date matches the provided date parameter and the location matches the provided text parameter.
   * Need: Admin who needs to know all planes that took from a specific airport on a certain date.
2) PREPARE get_fueling_trucks_by_fuelDate (date, text) AS SELECT t.* FROM truckload t WHERE t.date = $1 AND t.typeoffuel = $2;
   * Prepare a statement that accepts a data and a fueltype
   * It selects all truckloads of a certain fuel type on a certain date
   * Need: Truckloads coordinator needs to know all fuel loads taken on a specific date of a specific type of gas.
3) PREPARE get_runways_by_event_count (int) AS SELECT r.* FROM runway r WHERE (SELECT COUNT(*) FROM landingtakingoff l WHERE l.number = r.number AND l.location = r.location) > $1
   * Prepare a statement named get_runways_by_event_count that accepts an integer as a parameter.
   * Gets all runways with more than the parameter given of landings/ takeoffs
   * Need: Maintenance Manager can know when the runway needs to be redone based off the number of takeoff/landings done on the runway.
4) PREPARE get_tugs_by_location_count_manufacturer (text) AS SELECT at.manufacturer, COUNT(*) FROM airplanetug at WHERE at.location = $1 GROUP BY at.manufacturer ORDER BY at.manufacturer;
   * Prepare a statement named get_tugs_by_location_count_manufacturer that accepts a text string as a parameter and retuns all the manufacturer's which have tugs at the given location, with the number of tugs per manufacturer, and is ordered
   * Need: Tug Specialist who needs to know which tugs are at a specific airport.


![image](https://github.com/ephmonster/miniProjectDatabase/assets/33190140/477b32de-e184-4eaf-a519-15b977ac8799)


#### Timing
##### Nonparameterized Query Timing
| Query Number | [RunTime No Indexing](query_log.log) | [Runtime with Indexing](query_log_indexes.log) | Relevant Index|
|----------|----------|----------|----------|
| 1 | 6.357 | 8.014 | |
| 2 | 7.828 | 7.749 | |
| 3 | 10.075 | 2.511 | idx_plane_makeandmodel | 
| 4 | 4.097 | 4.425 | idx_tug_makeandmodel | 
| 5 | 6.655 | 2.460 | idx_plane_makeandmodel |
| 6 | 0.215 | 0.169 | |
| 7 | 475.743 | 35.131  | idx_tugs_date |
| 8 | 478.449 | 235.077 | idx_truckload_date |

##### Parameterized Query Timing
| Query Number | [RunTime No Indexing](query_log.log) | [Runtime with Indexing](query_log_indexes.log) | Relevant Index|
|----------|----------|----------|----------|
| 1 | 334.783 | 10.426 | idx_landingtakingoff_date |
| 2 | 128.580 | 4.395 | idx_truckload_date_typeoffuel |
| 3 | 8651.190 | 128.010 | idx_landingtakingoff_number_location | 
| 4 | 3.947 | 1.755 | idx_tug_makeandmodel |

### [Indexing](Indexes.sql)
Added in indexing for the dates of the flights, makeand model for the airplanes and the manufacturer of the airplane tugs.
1) CREATE INDEX idx_landingtakingoff_date ON public.landingtakingoff (date);
    * Index for the landingtakingoff table based on the date attribute
2) CREATE INDEX idx_plane_makeandmodel ON public.airplane (makeandmodel);
    * Index on the airplane table on the makeandmodel attribute
3) CREATE INDEX idx_tug_makeandmodel ON  public.airplanetug (manufacturer);
    * Index on the tug table on the manufacturer attribute
4) CREATE INDEX idx_truckload_date_typeoffuel ON truckload (date, typeoffuel);
    * Index on the the truckloads by date and type of fuel
5) CREATE INDEX idx_landingtakingoff_number_location ON landingtakingoff (number, location);
    * Index on the landing takeoff by location and runway number
6) CREATE INDEX idx_tugs_date ON tugs (date);
    * Index on the tuggings based off of the date.
7) CREATE INDEX idx_truckload_date ON truckload (date);
    * Index on the truckloads based off of the date.
![image](https://github.com/ephmonster/miniProjectDatabase/assets/33190140/6348251f-52e9-40f4-aa49-d71acfc2a5c1)

#### Constraints
We added the following constraints:
1) A constraint on the speed for an airplane
2) A constraint on the fueltype
3) A constraint on the in service column, requiring a boolean 1 or 0
4) A constrain on the amount of fuel in a fuel stock

Here is the sql for the constraints:
#### [Constraints](Constraints.sql)
We wrote the following queries which violated the constraints:
1) we inserted an airplane with a speed above the max
2) we insert fuel into fueltype which was not one of the allowed types
3) we put a 2, which is not a 0 or 1 into the in service column
4) we inserted more fuel than allowed into the fuel stock
Here is the sql for the violating queries:
#### [Violations](constraint_violations.sql)
Here is the log for the errors for the above queries:
#### [ErrorLogs](constraint_violation_log.log)

## Stage 3

### Additional Queries
#### [Queries](Queries.sql)
1)  Select all trucks at location X which had a refuel on day Y
     * SELECT a.licenseplate
       FROM fuelingtruck a JOIN truckload b
       ON a.licenseplate = b.licenseplate
       WHERE a.location = 'LAX' AND b.date = '2024-04-08

2)  Select all airplanes that are in service and use a given type of fuel
     * SELECT a.serialnumber
       FROM airplane a JOIN airplanetype b
       ON a.makeandmodel = b.makeandmodel
       WHERE a.in_service = 1 AND b.typeoffuel = 'Avgas'

3)  Select all airplanes which had more than 10 takeoffs
     * SELECT a.serialnumber
       FROM airplane a JOIN landingtakingoff b
       ON a.serialnumber = b.serialnumber
       GROUP BY a.serialnumber
       HAVING COUNT(*)>10

#### Timing
Note: The log output was appended to the [Query_Log_File](query_log.log).
| Query Number | [RunTime](query_log.log) | 
|----------|----------|
| 1 | 4.793 |
| 2 | 9.891 |
| 3 | 760.600 |

### [Views](views_queries.sql)
#### Process of choosing views:
We selected views that would provide essential information for specific roles within the airport management team. These views help streamline operations and provide quick access to frequently needed data.

1) View all jetbridges at LAX International Airport
    * User: jetbridge manager at LAX (similar view can be used for a manager at another airport)
    * Need: To manage all jetbridges in the airport
2) View all airbus A319 airplanes
    * User: Engineer specializing in these planes
    * Need: Maintance of these planes
3) View truckloads from a specific day
    * User: Petrolium Manager
    * Need: Track which trucks filled up with a specific type of gas on that day, helps for billing the airlines for gas
4) View runways at LAX
    * User: Air Traffic Control Agent
    * Need: Plan plane landing and takeoffs
#### Explanation of Procedure and Error Messages
##### View Creation and Queries:

Each view is created using CREATE OR REPLACE VIEW with WITH CHECK OPTION to ensure that any inserted or updated data must satisfy the view's WHERE clause.
For each view, a corresponding [SELECT](view_queries.sql) query is provided to fetch specific data from the view.

DML Operations:

[INSERT](view_queries.sql) (View 1): Inserting a new record into lax_bridges. If the inserted record does not satisfy the location = 'LAX' condition, an error will occur due to the WITH CHECK OPTION.
UPDATE (View 2): Updating the in_service status of a specific Airbus A319. If the record to be updated does not exist, no rows will be affected, which can be observed in the execution plan.
[DELETE](view_queries.sql) (View 3): Deleting a specific truckload record. If the record does not exist, no rows will be affected, and the execution plan will show zero rows deleted.
Logging:

The EXPLAIN ANALYZE statement is used to log the execution plan and performance metrics for each query and DML operation. This includes the cost, actual time, and number of rows affected.
Any error messages encountered during the execution of the queries will be captured in the log output. For instance, inserting an invalid record into a view with WITH CHECK OPTION will generate an error message indicating the violation of the view's condition.
This script provides a comprehensive approach to creating views, performing queries, and executing DML operations while logging the execution details for analysis and debugging.

Link to the log file for the view and queries can be found [here](view_query_output_log.log)
### Visualizations:
1) LAX runway Length visualization: Used to plan flight takeoff/landings based on required runway length for a plane
    *  Query: SELECT a.*
       FROM lax_runways a

 ![image](https://github.com/user-attachments/assets/0f95f457-446b-4f0c-a1d5-dd243e742878)


2) Viewing all fueltruck loads from a specific date: Used to understand breakdown of fuel needs and number of fuel loads needed per day
    * Query: SELECT typeoffuel, COUNT(*) AS truckload_count
      FROM truckload_2024_04_28
      GROUP BY typeoffuel;
![fuel_loads_per_day](https://github.com/user-attachments/assets/7fdde0e4-b663-4540-bf44-2c017d86749f)
![image](https://github.com/user-attachments/assets/bfa4c728-2e66-46c6-b40d-aee1803bbc34)


### [Functions](Functions.sql)
#### Process of choosing queries to replace with functions:
We selected complex queries that benefit from encapsulation within functions for better modularity and reusability. These functions can take parameters and return results, making them flexible for various operational needs.
1) Function for airplanes with a range greater than 13000 (Query 4 in stage 2 nonparameterized queries)
    * Test Query: SELECT * FROM airplanes13000()
2) Function for airplanes by date and location (Query 1 in stage 2 parameterized queries)
    * Test Query: select * from airplanes_date_location('2024-05-19', 'TLV')
3) Function for truckloads by fuel type and date (Query 2 in stage 2 parameterized queries)
    * Test Query: SELECT * FROM trucks_fuel_date('2024-04-28', 'JetB')
4) Function to get all runways with more than a given amount of takeoff/landings (Query 2 in stage 2 parameterized queries)
    * Test Query: select * from runway_events(30)
#### Timing
| Query Number | [RunTime](function_log.log) | 
|----------|----------|
| 1 | 51.821 |
| 2 | 4.996 |
| 3 | 1.948 |
| 4 | 63.743 |
### [Triggers](triggers.sql)
1) Output an error message if a user tries to add an airplane with the manufactor date after the date aquired
2) For each truck load of a given type of fuel at an airport subtract that from the total amount of fuel in the fuel stock of that type in the airport
![image](https://github.com/ephmonster/miniProjectDatabase/assets/33190140/f46f7610-a660-4463-83fa-3b8436a363e3)
![image](https://github.com/ephmonster/miniProjectDatabase/assets/33190140/818e6fd0-c74d-4c43-98c8-42758a3d3322)
![image](https://github.com/ephmonster/miniProjectDatabase/assets/33190140/d744f33b-4c02-416a-9364-89c1df321322)
As can be seen in the screenshots above the amount of JetA fuel in TLV went down by 120000 liters after the query was ran twice, once in the image and once just before.


## Stage 4

### Integration
1) First we outlined the DSD and ERD to create a blueprint of how we would merge the 2 databases together
### Foreign ERD
![ERD (1)](https://github.com/user-attachments/assets/5024528a-12d6-4b72-8940-8457b13a1e29)
#### Integrated ERD
![image (3)](https://github.com/user-attachments/assets/0375768b-9c23-452b-81dc-9a0f90f2f460)

#### Integrated DSD
![image (4)](https://github.com/user-attachments/assets/1c25682b-1340-4e65-bc8d-8a76f6fddd00)

2) We created a new database from the datadump backup from our friends database.
3) We created a Forgein Data Wrapper linked to the other database.
<img width="479" alt="role_creation" src="https://github.com/user-attachments/assets/466d1c8c-59f6-4551-9d38-0c9eea1b26b5">

4) We created a mapping to the forgein database
<img width="452" alt="mapping" src="https://github.com/user-attachments/assets/a01c73c8-fbfd-4478-9262-99e43ad0e776">

5) Then imported the forgein schema
To view the commands click [here](integration_forgein_data_wrapper_creation.sql)
6) Then we implemented the necessary changes to blend the 2 databases, outlined here:

Changes: we created a relation between Flight and Airplane called itsPlane. In order to implement this relation we added to the Flight table a column referencing the airplane called:
```sh
ALTER TABLE public.flight
ADD COLUMN serial_number INTEGER;
We populated this column using the following command:
UPDATE public.flight
SET serial_number = FLOOR(RANDOM() * 12883);
```
Additionally, we now have Flight as part of the relation landingtakingoff, where flightid in landingtakingoff references a flightid in the Flight table

Another change we made was to add a table ItsGate which relates a flight to its gates. This is the command we used: 
```sh
CREATE TABLE ItsGate
(
  flightid INT NOT NULL,
  gatenumber INT NOT NULL,
  location VARCHAR NOT NULL,
  PRIMARY KEY (flightid, gatenumber, location)
);
```

We populaled this table using the following command:
```sh
INSERT INTO ItsGate (flightid, gatenumber, location)
SELECT f.flightid, g.gatenumber, g.location
FROM gate g
JOIN 
landingtakingoff l ON g.location = l.location
JOIN flight f ON l.flightID = f.flightid
```
### Integrated Views
#### View 1 - [Boarding Pass] (integrated_views.sql)
Explanation - this view is helpful in representing information for each passenger - it has name, id, ticked id, flight id, flightcode, location and gatenumber
### Boarding Pass View

#### User:
Passenger

#### Need:
To access and verify the details of their flight reservation.

#### Function:
This view provides passengers with a comprehensive summary of their boarding pass information, including flight number, departure and arrival times, seat assignment, and gate information. It also includes crucial details like boarding group and any special instructions or alerts related to the flight. The boarding pass view helps passengers prepare for their journey by consolidating all essential travel information in one place.
```sh
create or replace view boarding_passes AS
select
c.name,
c.customerid,
t.ticketid,
f.flightid,
fc.flightcode,
g.location,
g.gatenumber
FROM
customer c
JOIN ticket t ON t.customerid = c.customerid
JOIN flight f on t.flightid = f.flightid
JOIN flightinfo fc ON f.flightcode = fc.flightcode
JOIN ItsGate g ON g.flightid = f.flightid 
JOIN landingtakingoff l ON l.flightid = f.flightid
WHERE l.lt = 0 AND g.location = l.location
```
##### [Queries](Integrate_View_Queries.sql)

### Query 1

**Summary:**
Retrieves boarding pass details for a specific passenger, including their name, ticket ID, flight information, and gate number.

**Use Case:**
Allows passengers to verify their boarding pass details and ensure that all information related to their flight and gate assignment is correct.

**User:**
Passengers seeking to confirm their flight reservation details.
<img width="618" alt="boardingpass" src="https://github.com/user-attachments/assets/155ad9f8-3c90-4a26-bee3-daa92dccad7c">

---

### Query 2

**Summary:**
Retrieves boarding pass details for all passengers on a specific flight, including their names, ticket IDs, and gate information.

**Use Case:**
Helps in identifying all passengers for a particular flight, which can be useful for flight attendants and gate staff to manage boarding and passenger queries.

**User:**
Flight crew and airport staff needing to review passenger details for a specific flight.

---

### Query 3

**Summary:**
Updates the gate number for all records in the view associated with a specific flight and location.

**Use Case:**
Allows for the modification of gate assignments for a flight, reflecting changes in gate assignments in real-time.

**User:**
Airport operations personnel managing gate assignments and updates.

---

### Query 4

**Summary:**
Inserts a new boarding pass record into the view with specified passenger and flight details.

**Use Case:**
Adds a new boarding pass entry, which may be used for managing ticketing and passenger information. Note that actual insertion typically affects underlying tables.

**User:**
Ticketing and check-in staff adding new boarding pass information into the system.
<img width="598" alt="Boardingpass_Insert_error" src="https://github.com/user-attachments/assets/1de53282-40a2-408c-9d6a-5f074097ebcd">
To combat the above error, we used a workaround detailed below in the Errors section.
##### Timing
| Query Number | [RunTime](Intergated_Views_Queries_Log.log) | 
|----------|----------|
| 1 | 42.352 |
| 2 | 4.974 |
| 3 | 0.547 |
| 4 |  5.153 |
#### View 2
This view combines the airline equipment database with the ticketing database. 
Goal: Leverage client feedback on their flight experience to improve flight quality specifically relating to the airplanes.
We create joins to combine user ratings to the flight they took and which planes were used to better understand client experience for a given flight, as well as gain insite into trends of client ratings based on the plane model they flew (to see whether clients enjoyed flying on newer models better by a significant amount).
##### Users
Data Analysts: To analyze trends in customer satisfaction and operational performance.
Customer Service Teams: To quickly access customer feedback and address issues.
Management: To make informed decisions based on comprehensive data.

```sh
CREATE OR REPLACE VIEW review_airplane_data AS
SELECT
    a.serialnumber,
    f.flightid,
    t.ticketid,
    r.rating
FROM
    airplane a
JOIN
    public.flight f ON f.serial_number = a.serialnumber
JOIN
    public.ticket t ON t.flightid = f.flightid
JOIN
    public.review r ON r.ticketid = t.ticketid;
```

##### [Queries](Integrate_View_Queries.sql)
**Query 1:**

**Summary:**
Calculates the average rating for each airplane make and model, ordered by highest rating.

**Use Case:**
Determine the most highly rated airplane models based on customer reviews.

**User:**
Airline data analysts.

**Query 2:**

**Summary:**
Prepares and executes an update to change the rating of a specific ticket.

**Use Case:**
Modify a customer's review rating for a specific flight ticket.

**User:**
Database administrators.

**Query 3:**

**Summary:**
Calculates the average rating and the number of reviews for each flight, ordered by highest average rating.

**Use Case:**
Identify flights with the best customer satisfaction and the volume of reviews they received.

**User:**
Airline management and data analysts.

**Query 4:**

**Summary:**
Deletes reviews for flights that have only one review to ensure data quality.

**Use Case:**
Clean the review database by removing single-review flights to improve the reliability of aggregated data.

**User:**
Database administrators and data quality managers.
##### Timing
| Query Number | [RunTime](Intergated_Views_Queries_Log.log) | 
|----------|----------|
| 1 | 3892.775 |
| 2 | 7.189 |
| 3 | 2925.043 |
| 4 | 6041.815|

##### Errors
When we tried to use the "With Check Option" we ran into the issue detailed below. Instead we used triggers and functions for validation to automatically update the underlying tables.
<img width="530" alt="checkoptionerror" src="https://github.com/user-attachments/assets/f3befa0b-5240-43ac-a1f0-9856d849da5f">

- **`WITH CHECK OPTION` Limitation**: The `WITH CHECK OPTION` ensures that data modifications made through a view must meet the view's query conditions. In the `review_airplane_data` view, the complex joins and conditions across multiple tables may not be easily enforced by `WITH CHECK OPTION`, leading to issues when trying to apply data constraints or validation.

- **Trigger Implementation**: Due to the limitations of `WITH CHECK OPTION`, triggers were utilized to enforce data integrity. Triggers can handle complex validation requirements and ensure that any data modifications adhere to the view's logic, by executing custom procedures before or after data changes are applied.

- **Function Utilization**: Functions were used within triggers to implement detailed validation checks. These functions allow for more granular control over the validation process, ensuring that the data modifications conform to the view's structure and relationships among the underlying tables, providing a more flexible and reliable solution compared to `WITH CHECK OPTION`.
<img width="384" alt="deleteworkaround trigger" src="https://github.com/user-attachments/assets/c0085d68-4e4f-41b6-ab78-f66a08988e25">

The code for the functions and triggers is available [here](view_triggers_functions.sql)






