-- managers table
create table managers (
id integer not null,
name varchar(32),
primary key(id)
);

insert into managers values 
(30001, 'Mr. 30001'), 
(30002, 'Mr. 30002'), 
(30003, 'Mr. 30003'), 
(30004, 'Mr. 30004');

-- jobs table
create table jobs (
id integer not null,
title varchar(32) not null,
min_salary float not null,
max_salary float not null,
primary key(id)
);

insert into jobs values
(100, 'Sr. Architect', 60000, 100000),
(200, 'Sr. Software Developer', 60000, 80000),
(300, 'Jr. Software Developer', 40000, 60000);

-- departments table
create table departments (
id integer not null,
name varchar(32) not null,
manager_id integer,
primary key(id),
foreign key(manager_id) references managers(id)
);

insert into departments values
(2, 'Architect Group', 30001),
(5, 'Software Development', 30002),
(7, 'Design Team', 30003),
(8, 'Software', 30004);

-- employees table
create table employees (
id integer not null,
firstname varchar(32),
lastname varchar(32),
ssn varchar(8),
birthdate varchar(10),
sex varchar(8),
address varchar(100),
salary float,
job_id integer,
manager_id integer,
dept_id integer,
primary key(id),
foreign key(job_id) references jobs(id),
foreign key(manager_id) references managers(id),
foreign key(dept_id) references departments(id)
);

insert into employees values 
(),

create table job_histories(
id integer primary key auto_increment,
employee_id integer not null,
job_id integer not null,
dept_id integer not null,
foreign key(employee_id) references employees(id),
foreign key(job_id) references jobs(id),
foreign key(dept_id) references departments(id)
);

