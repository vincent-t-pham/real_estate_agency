import sqlite3

conn = sqlite3.connect('agency.db')

c = conn.cursor()

#Creates table each table per execute
#Might need a GO at the end?
c.execute("""

CREATE TABLE IF NOT EXISTS Owner(
	Username		char(100) not null,
	Name			char(100) not null,
	Birthday		date,
	Email			char(100) not null,
	primary key (Username)
    	);

        """)

c.execute("""

CREATE TABLE IF NOT EXISTS Client (
	Username		char(100) not null,
	Name			char(100) not null,
	Birthday		date,
	Email			char(100) not null,
	primary key (Username)
	);
        
        """)

c.execute("""

CREATE TABLE IF NOT EXISTS Agent(
	Agent_id		integer not null,
	Name			char(100) not null,
	Number_of_clients	integer not null,
	Number_of_properties	integer not null,
	primary key (Agent_id)
	);
        
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Property (
	Property_id		integer not null,
	Listed_date		date not null,
	Square_foot		integer not null,
	Lot_size		integer not null,
        Number_of_beds          integer not null,
	Number_of_baths		integer not null,
        Property_type           char(100) not null,
        Agent_id                int,
	Open_house_date		date,
	Owner_username		char(100),
        Street_Address          char(100),
        City                    char(100),
        State                   char(100),
        Zip_Code                int,
	primary key (Property_id),
	foreign key (Owner_username) references Owner(Username),
	foreign key (Agent_id) references Agent(Agent_id)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Contract (
	Contract_id 		integer not null,
	Price 			integer not null,
	Type			char(100) not null,
	Purchase_date		date,
	Lease_start_date	date,
	Client_username		char(100) not null,
	Owner_username		char(100) not null,
	Property_id		integer not null,
	Agent_id		integer not null,
	primary key (Contract_id),
	foreign key (Client_username) references Client(username),
	foreign key (Owner_username) references Owner(username),
	foreign key (Property_id) references Property(Property_id),
	foreign key (Agent_id) references Agent(Agent_id)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Maintenance_Record (
	Username		char(100) not null,
	Record_id		char(100) not null,
	Date			date,
	Maintenance_item	char(100) not null,
	primary key (Username, Record_id),
	foreign key (Username) references Owner(Username)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Seller (
	Seller_username		char(100) not null,
	primary key (Seller_username),
	foreign key (Seller_username) references Owner(username) 
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Landlord (
	Landlord_username	char(100) not null,
	primary key (Landlord_username),
	foreign key (Landlord_username) references Owner(username)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Owner_phone_number (
	Username		char(100) not null,
	Phone_number		char(10) not null,
	primary key (Username),
	foreign key (Username) references Owner(username)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Agent_Email (
	Agent_id		integer not null,
	Phone_number		char(10) not null,
	primary key (Agent_id),
	foreign key (Agent_id) references Agent(Agent_id)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Agent_phone_number (
	Agent_id		integer not null,
	Phone_number		char (10) not null,
	primary key(Agent_id, Phone_number),
	foreign key (Agent_id) references Agent(Agent_id)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Sale_Property (
	Sale_property_id     integer not null,
	Listing_price        integer not null,
	Primary key (sale_property_id),
	foreign key (Sale_property_id) references Property(Property_id)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Rental_Property(
	Rental_property_id    integer not null,
	Monthly_rent        integer not null,
	Primary key (rental_property_id),
	foreign key (Rental_property_id) references Property(Property_id)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Renter(
    Renter_Username    char(100) not null,
    Primary Key(Renter_username),
    Foreign key (Renter_username) references Client(Username)
);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Rents(
	Renter_username    char(100) not null,
	Sale_property_id    integer not null,
	Primary Key (Renter_username),
	Foreign Key (Sale_property_id) references  Sale_Property(Sale_Property_id),
	Unique(Sale_property_id),
	Foreign key (Renter_username) references Renter(Renter_username)
	);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Buyer(
    Buyer_username char(100) not null,
    Primary Key(Buyer_username),
	Foreign key (Buyer_username) references Client(Username)
);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Buys(
    Buyer_username    char(100) not null,
    Rental_property_id    integer not null,
    Primary Key (Buyer_username),
    Foreign Key (Rental_Property_id) references Rental_Property(Rental_Property_id),
    Foreign key (Buyer_username) references Buyer(Buyer_username),
    Unique(Rental_property_id)
);
            """)

c.execute("""
CREATE TABLE IF NOT EXISTS Receives_offer(
    Client_Username    char(100) not null,
    Agent_id        integer not null,
    Offer_price    integer not null,
    Primary Key    (Client_username, Agent_id),
    foreign key (Agent_id) references Agent(Agent_id),
    foreign key (Client_Username) references Client(Username)
);
            """)


c.execute("""
CREATE TABLE IF NOT EXISTS Client_phone_no(
    Username    char(100) not null,
    Phone_number     integer not null,
    Primary Key(Username),
	Foreign key (Username) references Client(username)
);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Agent_works_with_client(
    Client_username    char(100) not null,
    Agent_id        integer not null,
    Primary Key (Client_username, Agent_id),
	Foreign key (Agent_id) references Agent(Agent_id)
);
        """)

c.execute("""
CREATE TABLE IF NOT EXISTS Agent_works_with_owner(
    Owner_username    char(100) not null,
    Agent_id        integer not null,
    Primary Key (Owner_username, Agent_id),
	Foreign key (Agent_id) references Agent(Agent_id)
);""")

c.execute("INSERT OR REPLACE INTO Owner VALUES ('Vincent.t.pham', 'Vincent', '2001-01-02', 'vincent.t.pham@sjsu.edu')") 
c.execute("INSERT OR REPLACE INTO Seller VALUES ('test')")

conn.commit()

