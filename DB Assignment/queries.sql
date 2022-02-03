/*
A) Write an SQL query to print all Worker details from the Worker table order 
by FIRST_NAME Ascending and DEPARTMENT Descending. 
B) Write an SQL query to print details of the Workers who are also Managers. 
C) Write an SQL query to determine the 5th highest salary without using TOP or 
limit method. 
D) Write an SQL query to fetch intersecting records of two tables. 
E) Write an SQL query to show all departments along with the number of 
people in there. 
*/

select * from worker order by first_name asc,department desc;

select * from worker, title where worker.worker_id = title.worker_ref_id and worker_title = "Manager";

select * from(
select first_name, salary, dense_rank() 
over(order by salary desc)r from worker) 
where r=5;

select worker_id from worker intersect select worker_ref_id from bonus;
select bonus_date from bonus intersect select affected_from from title;

select department,count(*) from worker group by department;