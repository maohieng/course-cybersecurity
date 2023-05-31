
-- create
CREATE TABLE Employees  
(  
EmployeeID int primary key,
FirstName varchar(255),  
LastName varchar(255),  
Email varchar(255),  
Dept varchar(50),
Country varchar(255),  
City varchar(255)  
);

-- insert
INSERT INTO Employees VALUES (1, 'Clark', 'Cle', 'clark.cle@company.com', 'sale','Cambodia', 'Phnom Penh');
-- INSERT INTO EMPLOYEE VALUES (2, 'Dave', 'Accounting', 5000, 'Cambodia', 'Phnom Penh');
-- INSERT INTO EMPLOYEE VALUES (3, 'Ava', 'Sales', 5000, 'Cambodia', 'Phnom Penh');

-- fetch 
-- SELECT * FROM Employees WHERE dept = 'sale';

-- alter
ALTER TABLE Employees ADD COLUMN Gender varchar(10);

-- update
UPDATE Employees SET Gender = 'female' WHERE EmployeeID = 1;

-- rename column
ALTER TABLE Employees RENAME COLUMN Dept TO DeptID;

-- delete existing data in DeptID before change the column type
UPDATE Employees SET DeptID = null;

-- MODIFY column type
ALTER TABLE Employees MODIFY COLUMN DeptID int;

-- introduce new table 
CREATE TABLE Depts 
(
DeptID int primary key,
Name varchar(50) not null
);

INSERT INTO Depts VALUES (1, 'Sale');

-- add contraint foreign key
ALTER TABLE Employees ADD CONSTRAINT FkDeptID foreign key (DeptID) references Depts(DeptID);

-- add department id for Employees
UPDATE Employees SET DeptID = 1 WHERE EmployeeID = 1;


-- fetch all
SELECT * FROM Employees AS E left outer join Depts as D on E.DeptID = D.DeptID;

-- ORDERS TABLE
-- CREATE TABLE Orders 
-- (
-- OrderID integer not null auto_increment,
-- OrderVal integer not null,
-- EmployeeID integer not null,
-- primary key (OrderID),
-- foreign key(EmployeeID) references Employees(EmployeeID)
-- );

-- SELECT * FROM Orders;



