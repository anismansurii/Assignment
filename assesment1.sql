create database assesment_sql_tops;


use assesment_sql_tops;

create table workers(
	wid int primary key ,
    wfname varchar(20) not null ,
    wlname varchar(20)   ,
    wsalary float(8,2) ,
    wJoining datetime  ,
    wdept int 
);

alter table workers modify column wsalary float(8);
alter table workers modify column wdept varchar(10);


insert into workers values (1, "Monika" , "Arora",  100000 , "2014-02-20 09:00:00" , "HR") ;
INSERT INTO workers VALUES (2, "Niharika", "Verma", 80000, "2014-06-11 09:00:00", "Admin");
INSERT INTO workers VALUES (3, "Vishal", "Singhal", 300000, "2014-02-20 09:00:00", "HR");
INSERT INTO workers VALUES (4, "Amitabh", "Singh", 500000, "2014-02-20 09:00:00", "Admin");
INSERT INTO workers VALUES (5, "Vivek", "Bhati", 500000, "2014-06-11 09:00:00", "Admin");
INSERT INTO workers VALUES (6, "Vipul", "Diwan", 200000, "2014-06-11 09:00:00", "Account");
INSERT INTO workers VALUES (7, "Satish", "Kumar", 75000, "2014-01-20 09:00:00", "Account");
INSERT INTO workers VALUES (8, "Geetika", "Chauhan", 90000, "2014-04-11 09:00:00", "Admin");

-- 1 . Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME 
-- Ascending and DEPARTMENT Descending.  asc is default
select * from workers order by wfname asc;
select * from workers order by wdept ;

-- 2 Write an SQL query to print details for Workers with the first names      
-- from the Worker table. 
select * from workers where wfname = "Vipul" or wfname = "satish"; 

-- 3 Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and 
-- contains six alphabets.
select * from workers where wfname like ("_____h");

-- 4 Write an SQL query to print details of the Workers whose SALARY lies between 1 and 5 lakh
select * from workers where wsalary between 100000 and 500000;

-- 5. Write an SQL query to fetch duplicate records having matching data in some fields of a table. 
select * from workers having wjoining in (select distinct  wjoining  from workers) ;

-- 6 Write an SQL query to show the top 6 records of a table. 
 select * from workers limit 6;
 
 
--  7. Write an SQL query to fetch the departments that have less than five people in them. 
select wdept , count(*)  count from workers group by wdept having count <5 ;

-- 8. Write an SQL query to show all departments along with the number of people in there. 
select wdept , count(*)  count from workers group by wdept ;

-- 9 .  Write an SQL query to print the name of employees having the highest salary in each department. 
select wfname , wdept from workers where wsalary in (select max(wsalary) from workers group by wdept);