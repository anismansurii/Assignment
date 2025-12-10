-- For this assignment, you will finish building the contact management database for MarketCo 
create database MarketCo;
use MarketCo;

-- Question 1 . Statement to create table 

create table Company (
		CompanyID int primary key ,
        CompanyName varchar(45) not null ,
        Street varchar(45) not null ,
        City varchar(45) not null ,
        State varchar(20) not null ,
        Zip varchar(6) not null 
);

create table Contact (
		ContactID int primary key ,
        CompanyID int not null ,
        FirstName varchar(45) not null ,
        LastName varchar(45) not null ,  
        Street varchar(45) not null ,
        City varchar(45) not null ,
        State varchar(20) not null ,
        Zip varchar(6) not null ,     
        IsMain boolean ,
        Email varchar(45) not null ,
        Phone varchar(12) unique ,
        foreign key(CompanyID) references Company(CompanyID)
);

-- Q 2 Statement to create the Employee table  

create table Employee(
		EmployeeID int primary key , 
        FirstName varchar(45) not null ,
        LastName varchar(45) not null ,  
        Salary decimal(10 , 2),
        HireDate date not null ,
        JobTitle varchar(25) not null ,
        Email varchar(45) not null ,
        Phone varchar(12) unique
);

-- Q 3 Statement to create the ContactEmployee table 

CREATE TABLE ContactEmployee (
    ContactEmployeeID INT NOT NULL PRIMARY KEY,
    ContactID INT NOT NULL,
    EmployeeID INT NOT NULL,
    ContactDate DATE,
    Description VARCHAR(100),
    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Q 4 . ) In the Employee table, the statement that changes Dhruv’s phone number to 2155558800 

set sql_safe_updates = 0;
update employee set Phone='2155558800' where EmployeeID = 1;

-- Q 5 .In the Company table, the statement that changes the name of “Amazon” to “Amazon web services” . 

update company set companyname='AWS' where companyname = "Amazon";

/* Q 6 .  In ContactEmployee table, the statement that removes Dhruv Kothari’s (Employee) contact 
event with Anis Mansuri (contact) (one statement). 
HINT: Use the primary key of the ContactEmployee table to specify the correct record to remove*/ 

delete from contactemployee where 
contactID = (select contactID from contact where FirstName = "Anis"and LastName = "Mansuri") and 
EmployeeID = (select EmployeeID from employee where FirstName = "Dhruv" and LastName = "Kothari");

-- or we can directly give the contactID = 1 and EmployeeID = 1

/* Q 7 Write the SQL SELECT query that displays the names of the employees that 
have contacted sbi bank (one statement). Run the SQL SELECT query in 
MySQL Workbench. Copy the results below as well. */

-- connect employee and contactemp to get contactID
create view EmployeeContactRes as
select e.FirstName , e.EmployeeID , ce.ContactID , ce.ContactDate 
from employee e join contactemployee ce 
on e.EmployeeID = ce.EmployeeID; 

-- connect contact to company to get company name
create view contactcompany as
select ecr.FirstName as EmpName , ecr.EmployeeID , ecr.ContactDate , c.ContactID , c.FirstName as ContactName , c.CompanyID 
from contact c join EmployeeContactRes ecr 
on c.ContactId = ecr.ContactID;

-- Final Answer getting people who contacted sbibank as particular company from result
select cc.EmpName , cc.EmployeeID , cc.ContactDate , cc.ContactID , cc.ContactName , co.CompanyID , co.CompanyName
from contactcompany cc join company co
on cc.CompanyID = co.CompanyID where CompanyName = "SBI Bank";
