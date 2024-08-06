CREATE TABLE Worker (
    WORKER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FIRST_NAME CHAR(25),
    LAST_NAME CHAR(25),
    SALARY INT(15),
    JOINING_DATE DATETIME,
    DEPARTMENT CHAR(25)
);

INSERT INTO Worker
    (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
        (001, 'Monika', 'Arora', 100000, '14-02-20 09.00.00', 'HR'),
        (002, 'Niharika', 'Verma', 80000, '14-06-11 09.00.00', 'Admin'),
        (003, 'Vishal', 'Singhal', 300000, '14-02-20 09.00.00', 'HR'),
        (004, 'Amitabh', 'Singh', 500000, '14-02-20 09.00.00', 'Admin'),
        (005, 'Vivek', 'Bhati', 500000, '14-06-11 09.00.00', 'Admin'),
        (006, 'Vipul', 'Diwan', 200000, '14-06-11 09.00.00', 'Account'),
        (007, 'Satish', 'Kumar', 75000, '14-01-20 09.00.00', 'Account'),
        (008, 'Geetika', 'Chauhan', 90000, '14-04-11 09.00.00', 'Admin');

CREATE TABLE Bonus (
    WORKER_REF_ID INT,
    BONUS_AMOUNT INT(10),
    BONUS_DATE DATETIME,
    FOREIGN KEY (WORKER_REF_ID)
        REFERENCES Worker(WORKER_ID)
        ON DELETE CASCADE
);

INSERT INTO Bonus
    (WORKER_REF_ID, BONUS_AMOUNT, BONUS_DATE) VALUES
        (001, 5000, '16-02-20'),
        (002, 3000, '16-06-11'),
        (003, 4000, '16-02-20'),
        (001, 4500, '16-02-20'),
        (002, 3500, '16-06-11');
   
CREATE TABLE Title (
    WORKER_REF_ID INT,
    WORKER_TITLE CHAR(25),
    AFFECTED_FROM DATETIME,
    FOREIGN KEY (WORKER_REF_ID)
        REFERENCES Worker(WORKER_ID)
        ON DELETE CASCADE
);

INSERT INTO Title
(WORKER_REF_ID, WORKER_TITLE, AFFECTED_FROM) VALUES
 (001, 'Manager', '2016-02-20 00:00:00'),
 (002, 'Executive', '2016-06-11 00:00:00'),
 (008, 'Executive', '2016-06-11 00:00:00'),
 (005, 'Manager', '2016-06-11 00:00:00'),
 (004, 'Asst. Manager', '2016-06-11 00:00:00'),
 (007, 'Executive', '2016-06-11 00:00:00'),
 (006, 'Lead', '2016-06-11 00:00:00'),
 (003, 'Lead', '2016-06-11 00:00:00');


-- Write a query to display all the first_name  in upper case
select upper(first_name) from worker


-- Write a querty to display unique department from workers table
select distinct(department) from worker

-- Write an SQL query to print the first three characters of FIRST_NAME from Worker table
select substr(first_name,1,3) from worker

-- Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.
select position("a" in first_name) as position, first_name from worker
where first_name = "Amitabh"

-- Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length
select distinct(department), length(department) from worker

-- Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME 
Ascending and DEPARTMENT Descending
select * from worker
order by first_name asc, department desc

-- Write a query to get workers whose name are Vipul and Satish
select * from worker
where first_name in ("Vipul","Satish")


-- Write an SQL query to print details of the Workers whose FIRST_NAME contains 'a'
select first_name from worker
where first_name like "%a%"

-- Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets
select first_name from worker
where first_name like "_____h"

-- Write an SQL query to print details of the Workers whose SALARY lies between 100000 and 500000
select * from worker
where salary between 100000 and 500000

-- Write an SQL query to print details of the Workers who have joined in Feb’2014
select * from worker
where joining_date like "2014-02%"

-- Write an SQL query to fetch the count of employees working in the department ‘Admin’
select department,count(*) from worker
group by department
having department = "admin"

-- Write an SQL query to fetch the no. of workers for each department in the descending order
select department,count(*) as count from worker
group by department
order by count desc

-- Write a query to display workerrs who are managers
select concat(w.first_name," ",w.last_name) as emp_name, t.worker_title from worker w
inner join title t on w.worker_id = t.worker_ref_id
where t.worker_title = "Manager"

-- Write query to find duplicate rows title table
select worker_title,count(*) from title
group by worker_title
having count(*) > 1

-- Write an SQL query to show all workers who got the bonus along with bonus amount
select concat(w.first_name," ",w.last_name), bonus_amount from worker w
inner join bonus b on w.worker_id = b.worker_ref_id 

-- Write a query to find employees in worker table that do not exist in bonus table (ie did not get bonus)
select concat(w.first_name," ",w.last_name), bonus_amount from worker w
left join bonus b on w.worker_id = b.worker_ref_id 
where bonus_amount is null

-- Write a query to find the highest 2 salaries
select distinct(salary) from worker
order by salary desc
limit 2

-- Find 2nd highest without using TOP or LIMIT
select max(salary) from worker
where salary < (select max(salary) from worker)


-- Find people who have the same salary
select * from worker
where salary in(
select salary from worker
group by salary
having count(*) > 1)
   
-- Write a query to fetch 1st 50% records without using Top


-- Write a query to select a department with more than 3 people in worker table
select department, count(*) from worker
group by department
having count(*) > 3

-- Write a query to select 1st and last row of a worker table
(select * from worker
order by worker_id asc
limit 1)
union all
(select * from worker
order by worker_id desc
limit 1)

-- Write a query to select last 5 entries from worker table
select * from worker
order by worker_id desc
limit 5


-- Write a query to select people with highest salary in each group
select department,count(*),max(salary) from worker
group by department

-- Write a query to fetch departments along with the total salaries paid for each of them
select department,count(*),sum(salary) from worker
group by department

-- Write a query to fetch the names of workers who earn the highest salary
select * from worker
where salary in (select max(salary) from worker)
