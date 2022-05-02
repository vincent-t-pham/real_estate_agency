import sqlite3

conn = sqlite3.connect('agency.db')

c = conn.cursor()


c.execute("""
CREATE TABLE IF NOT EXISTS `Owner`(
	Username		VARCHAR(25) NOT NULL,
	Name			VARCHAR(25) NOT NULL,
	Birthday		date,
	Email			VARCHAR(25) NOT NULL,
    Phone_number	VARCHAR(10) NOT NULL,
	primary key (Username)
    	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS `Client` (
	Username		VARCHAR(25) NOT NULL,
	Name			VARCHAR(25) NOT NULL,
	Birthday		date,
	Email			VARCHAR(25) NOT NULL,
    Phone_number	VARCHAR(10) NOT NULL,
	primary key (Username)
	);
        
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Agent(
	Agent_id		VARCHAR(25) NOT NULL,
	Name			VARCHAR(25) NOT NULL,
    Email   		VARCHAR(25) NOT NULL,
    Phone_number	VARCHAR(10) NOT NULL,
	Number_of_clients	integer not null,
	Number_of_properties	integer not null,
	primary key (Agent_id)
	);
        
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Property (
	Property_id			CHAR(10) NOT NULL,
	Listed_date			DATE NOT NULL,
	Square_foot			INTEGER NOT NULL,
	Lot_size			INTEGER NOT NULL,
	Number_of_baths		INTEGER NOT NULL,
    Number_of_beds		INTEGER NOT NULL,
	street_address		VARCHAR(100) NOT NULL,
	city				VARCHAR(100) NOT NULL,
    state				VARCHAR(100) NOT NULL,
    zipcode				INTEGER NOT NULL,
	Property_type		VARCHAR(20) NOT NULL,
	Agent_id			VARCHAR(25) NOT NULL,
	Open_house_date		DATE,
	Owner_username		VARCHAR(25) NOT NULL,
    availability     	INTEGER,
	PRIMARY KEY (Property_id),
	FOREIGN KEY (Owner_username) REFERENCES `Owner`(Username) on delete cascade,
	FOREIGN KEY (Agent_id) REFERENCES Agent(Agent_id) on delete cascade
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Contract (
	Contract_id 					CHAR(10) NOT NULL,
	`Type`							VARCHAR(10) NOT NULL,
    Price_rent 						INTEGER NOT NULL,
	Purchase_date					DATE,
	Lease_start_date				DATE,
	Client_username					VARCHAR(25) NOT NULL,
	Owner_username					VARCHAR(25) NOT NULL,
	Property_id						CHAR(10) NOT NULL,
	Agent_id						VARCHAR(25) NOT NULL,
	PRIMARY KEY (Contract_id),
	FOREIGN KEY (Client_username) 	REFERENCES `Client`(username) on delete cascade,
	FOREIGN KEY (Owner_username)  	REFERENCES `Owner`(username) on delete cascade,
	FOREIGN KEY (Property_id)	  	REFERENCES Property(Property_id) on delete cascade,
	FOREIGN KEY (Agent_id)		  	REFERENCES Agent(Agent_id) on delete cascade
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Maintenance_Record (
	Username					VARCHAR(25) NOT NULL,
	Record_id					CHAR(10) NOT NULL,
	`Date`						DATE,
	Maintenance_item			VARCHAR(50) NOT NULL,
	PRIMARY KEY (Username, Record_id),
	FOREIGN KEY (Username)  	REFERENCES Landlord(Landlord_username) on delete cascade
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Seller (
	Seller_username					VARCHAR(25) NOT NULL,
	PRIMARY KEY (Seller_username),
	FOREIGN KEY (Seller_username) 	REFERENCES `Owner`(username) on delete cascade
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Landlord (
	Landlord_username				VARCHAR(25) NOT NULL,
	PRIMARY KEY (Landlord_username),
	FOREIGN KEY (Landlord_username) REFERENCES `Owner`(username) on delete cascade
	);
        """)


c.execute("""
CREATE TABLE IF NOT EXISTS Sale_Property (
	Sale_property_id     			CHAR(10) NOT NULL,
	Listing_price       			INTEGER NOT NULL,
	PRIMARY KEY (sale_property_id),
	FOREIGN KEY (Sale_property_id) 	REFERENCES Property(Property_id) on delete cascade
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Rental_Property(
	Rental_property_id    				CHAR(10) NOT NULL,
	Monthly_rent        				INTEGER NOT NULL,
	PRIMARY KEY (rental_property_id),
	FOREIGN KEY (Rental_property_id)    REFERENCES Property(Property_id) on delete cascade
	);
        """)


c.execute("""
CREATE TABLE IF NOT EXISTS Rents(
	Renter_username    				VARCHAR(25) NOT NULL,
	Rental_property_id    			CHAR(10) NOT NULL,
	PRIMARY KEY (Renter_username, Rental_property_id) ,
	FOREIGN KEY (Rental_property_id)  REFERENCES  Rental_Property(Rental_Property_id) on delete cascade,
	FOREIGN KEY (Renter_username)   REFERENCES `client`(username) on delete cascade
	);
        """)


c.execute("""
CREATE TABLE IF NOT EXISTS Buys(
     Buyer_username     					VARCHAR(25) NOT NULL,
    Sale_property_id   					CHAR(10) NOT NULL,
    PRIMARY KEY (Buyer_username, Sale_property_id),
    FOREIGN KEY (Sale_Property_id) 		REFERENCES Sale_Property(Sale_Property_id) on delete cascade,
	FOREIGN KEY (Buyer_username) 		REFERENCES `client`(username) on delete cascade
);
            """)

c.execute("""
CREATE TABLE IF NOT EXISTS Receives_offer(
     Client_Username     			VARCHAR(25) NOT NULL,
    Agent_id        				VARCHAR(25) NOT NULL,
    Offer_price    					INTEGER NOT NULL,
    PRIMARY KEY (Client_username, Agent_id),
    FOREIGN KEY (Agent_id) 			REFERENCES Agent(Agent_id) on delete cascade,
    FOREIGN KEY (Client_Username) 	REFERENCES `Client`(Username) on delete cascade
);
            """)


c.execute("""
CREATE TABLE IF NOT EXISTS Agent_works_with_client(
    Client_username    				VARCHAR(25) NOT NULL,
    Agent_id           				VARCHAR(25) NOT NULL,
    PRIMARY KEY (Client_username, Agent_id),
	FOREIGN KEY (Agent_id) 			REFERENCES Agent(Agent_id) on delete cascade,
	FOREIGN KEY (Client_username)   REFERENCES `Client`(username) on delete cascade
);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Agent_works_with_owner(
    Owner_username    			 VARCHAR(25) NOT NULL,
    Agent_id        			 VARCHAR(25) NOT NULL,
    PRIMARY KEY (Owner_username, Agent_id),
	FOREIGN KEY (Agent_id) 		 REFERENCES Agent(Agent_id) on delete cascade,
    FOREIGN KEY (Owner_username) REFERENCES `Owner`(username) on delete cascade
);""")

# add to Owner
c.execute("Insert into `Owner` values('jimmy23', 'Jimmy W', '1980-04-03', 'jimmyw@gmail.com', '5690230')")
c.execute("Insert into `Owner` values('walter07', 'Walter S', '1990-06-03', 'walter_s@gmail.com', '5698210')")
c.execute("Insert into `Owner` values('aaron98', 'Aaron P', '1976-04-23', 'aaron98@gmail.com', '5690780')")
c.execute("Insert into `Owner` values('hina87', 'Hina S', '1998-06-14', 'hinas_87@gmail.com', '5654870')")
# add to client
c.execute("Insert into `Client` values('anikha69', 'Anikha S', '1997-06-03', 'anikha_s@gmail.com', '5690230', 'renter')")
c.execute("Insert into `Client` values('christineio', 'Christine Polly', '1987-06-19', 'jimmyw@gmail.com', '5687640', 'buyer')")
c.execute("Insert into `Client` values('stephenstrange', 'Stephen S', '1976-04-09', 'stephen_s@gmail.com', '56919087','buyer')")
c.execute("Insert into `Client` values('tony_s', 'Tony S', '1988-12-08', 'tonystark@gmail.com', '56182938', 'renter')")
# add to Property
c.execute("Insert into Property values('2266578381', '2021-08-06', 1300, 4500, 3,4, '123 Peachtree', 'San Jose', 'CA', 95192, 'rental', '0986289', '2021-09-08', 'jimmy23', TRUE)")
c.execute("Insert into Property values('2283729010', '2021-09-05', 1100, 3400, 2,2, '123 Avalon', 'Santa Clara', 'CA', 95145, 'sale', '0989589', '2021-09-10', 'walter07', TRUE)")
c.execute("Insert into Property values('2289972029', '2021-09-16', 1800, 5000, 4,4, '1100 Morrison', 'San Jose', 'CA', 95126, 'sale', '0975482', '2021-09-18', 'aaron98', TRUE)")
c.execute("Insert into Property values('2218271949', '2021-09-21', 800, 3000, 2,1, '383 Stockton', 'Santa Clara', 'CA', 95148, 'rent', '0985820', '2021-09-24', 'hina87', TRUE)")
# add to agent
c.execute("Insert into Agent values('0986289', 'Jesse Pinkman', 'jesse_pinkman@gmail.com', '56452613', 4, 4)")
c.execute("Insert into Agent values('0989589', 'Anakin Skywalker', 'anakinsky@gmail.com', '56371613', 2, 2)")
c.execute("Insert into Agent values('0975482', 'Paul Rudd', 'paul_rudd@gmail.com', '56472013', 2, 3)")
c.execute("Insert into Agent values('0985820', 'Anthony Edward', 'edward_tony@gmail.com', '56452719', 3, 3)")
# add to contract
c.execute("Insert into Contract values('1572672817', 'rental', 1500, NULL, '2021-09-15', 'anikha69', 'jimmy23', '2266578381', '0986289')")
c.execute("Insert into Contract values('1289172901', 'sale', 150000, '2021-09-10', NULL, 'christineio', 'walter07', '2283729010', '0989589')")
c.execute("Insert into Contract values('1278172379', 'sale', 140000, '2021-09-22', NULL, 'Stephenstrange', 'aaron98', '2289972029', '0975482')")
c.execute("Insert into Contract values('1402838161', 'rental', 1200, NULL, '2021-09-28', 'Tony_s', 'hina87', '2218271949', '0985820')")
# add to Landlord
c.execute("Insert into Landlord values('jimmy23')")
c.execute("Insert into Landlord values('hina87')")
# add to Maintenance_Record
c.execute("Insert into Maintenance_Record values('jimmy23', '8720128481', '2021-09-22', 'Pipe')")
c.execute("Insert into Maintenance_Record values('hina87', '8728912832', '2021-09-28', 'Dishwasher')")
c.execute("Insert into Maintenance_Record values('jimmy23', '8725162263', '2021-09-30', 'Sink')")
# add to Seller
c.execute("Insert into Seller values('walter07')")
c.execute("Insert into Seller values('aaron98')")
# add to Sale_Property
c.execute("Insert into Sale_Property values('2283729010', 150000)")
c.execute("Insert into Sale_Property values('2289972029', 140000)")
# add to Rental_Property
c.execute("Insert into Rental_Property values('2266578381', 1500)")
c.execute("Insert into Rental_Property values('2218271949', 1200)")
# add to Rents
c.execute("Insert into Rents values('anikha69', '2266578381')")
c.execute("Insert into Rents values('Tony_s', '2218271949')")
# add to Buys
c.execute("Insert into Buys values('christineio', '2283729010')")
c.execute("Insert into Buys values('stephenstrange', '2289972029')")
# add to Receives_offer
c.execute("Insert into Receives_offer values('anikha69', '0986289',  1400)")
c.execute("Insert into Receives_offer values('tony_s', '0985820', 1300)")
# add to Agent_works_with_client
c.execute("Insert into Agent_works_with_client values('anikha69', '0986289')")
c.execute("Insert into Agent_works_with_client values('tony_s', '0985820')")
# add to Agent_works_with_owner
c.execute("Insert into Agent_works_with_owner values('walter07', '0975482')")
c.execute("Insert into Agent_works_with_owner values('aaron98', '0985820')")
