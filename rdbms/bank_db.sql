 (2) Bank Database 
 Consider the following database of Bank. A bank maintains the customer details, account details  
 and loan details . It has the Branch information also. Following are the tables : 
 
 1 Account(acc_no int, acc_type char(10), balance float(8,2)) 
 2. Loan(loan_no int, loan_amt double(9,2) , no_of_years int) 
 3. Branch(branch_no int, branch_name char(20), branch_city varchar(20)) 
 4 .Customer(cust_no int , cust_name char(20), cust_street char(15), cust_city varchar(20)) 
 The relationships are as follows. :- 
 Customer-Account : 1-M 
 Customer- Loan : 1-M 
 Branch-Loan : 1-M 
 Branch-Account : 1:M 
 Constraints : 
 1. branch_name is not null.
 
create table Branch (
    branch_no int PRIMARY KEY auto_increment,
    branch_name varchar(20) not null,
    branch_city varchar(20) not null
);

create table Customer (
    cust_no int PRIMARY KEY auto_increment,
    cust_name varchar(20),
    cust_street varchar(15),
    cust_city varchar(20)
);

create table Account (
    acc_no int PRIMARY KEY auto_increment,
    acc_type varchar(10) not null,
    balance double(8, 2) not null,
    cust_no int,
    branch_no int,
    FOREIGN KEY(cust_no) REFERENCES Customer(cust_no) ON DELETE CASCADE,
    FOREIGN KEY(branch_no) REFERENCES Branch(branch_no) ON DELETE CASCADE,
    constraint check(acc_type in ('savings', 'current', 'salary')),
    UNIQUE(acc_no, cust_no, branch_no)
);

create table Loan (
    loan_no int PRIMARY KEY auto_increment,
    loan_amt float(9, 2) not null,
    no_of_years int not null,
    cust_no int,
    branch_no int,
    FOREIGN KEY(cust_no) REFERENCES Customer(cust_no) ON DELETE CASCADE,
    FOREIGN KEY(branch_no) REFERENCES Branch(branch_no) ON DELETE CASCADE,
    UNIQUE(cust_no, branch_no, loan_no)
);

INSERT INTO
    Branch(branch_name, branch_city)
VALUES
    ("CIDCO", "Pune"),
    ("Sadashiv Peth", "Pune"),
    ("SBI Kalasagar", "Pimpri"),
    ("SBI Vadgaon", "Pune"),
    ("Nagar", "Ahmednagar");

INSERT INTO
    Customer(cust_name, cust_street, cust_city)
VALUES
    ("Shubham", "Miami Rd.", "Pune"),
    ("Wallabh", "JM St.", "Pune"),
    ("Yash", "LM Joshi Rd.", "Pune"),
    ("Saurabh", "Hadaps Rd", "Pune"),
    ("Kalyani", "Sinhagad Rd.", "Pune");

INSERT INTO
    Account(acc_type, balance, cust_no, branch_no)
VALUES
    ("savings", 999999.99, 1, 4),
    ("current", 600000, 2, 1),
    ("salary", 450000, 3, 2),
    ("savings", 355550, 4, 3),
    ("savings", 100000, 5, 4),
    ("salary", 705000, 5, 1),
    ("current", 80000, 4, 5),
    ("current", 50000, 1, 5);

INSERT INTO
    Loan(cust_no, branch_no, loan_amt, no_of_years)
VALUES
    (1, 4, 8000000, 5),
    (2, 1, 1000000, 3),
    (3, 2, 20000, 1),
    (4, 3, 4000000, 7),
    (5, 4, 550000, 4),
    (2, 3, 500000, 2),
    (1, 5, 20000, 1),
    (4, 5, 50000, 1);


 select * from Branch;
 +-----------+---------------+-------------+
 | branch_no | branch_name   | branch_city |
 +-----------+---------------+-------------+
 |         1 | CIDCO         | Pune        |
 |         2 | Sadashiv Peth | Pune        |
 |         3 | SBI Kalasagar | Pimpri      |
 |         4 | SBI Vadgaon   | Pune        |
 |         5 | Nagar         | Ahmednagar  |
 +-----------+---------------+-------------+
 
 
 select * from Customer;
 +---------+-----------+--------------+-----------+
 | cust_no | cust_name | cust_street  | cust_city |
 +---------+-----------+--------------+-----------+
 |       1 | Shubham   | Miami Rd.    | Pune      |
 |       2 | Wallabh   | JM St.       | Pune      |
 |       3 | Yash      | LM Joshi Rd. | Pune      |
 |       4 | Saurabh   | Hadaps Rd    | Pune      |
 |       5 | Kalyani   | Sinhagad Rd. | Pune      |
 +---------+-----------+--------------+-----------+
 
 select * from Account;
 +--------+----------+------------+---------+-----------+
 | acc_no | acc_type | balance    | cust_no | branch_no |
 +--------+----------+------------+---------+-----------+
 |      1 | savings  | 1000000.00 |       1 |         4 |
 |      2 | current  |  600000.00 |       2 |         1 |
 |      3 | salary   |  450000.00 |       3 |         2 |
 |      4 | savings  |  355550.00 |       4 |         3 |
 |      5 | savings  |  100000.00 |       5 |         4 |
 |      6 | salary   |  705000.00 |       5 |         1 |
 |      7 | current  |   80000.00 |       4 |         5 |
 |      8 | current  |   50000.00 |       1 |         5 |
 +--------+----------+------------+---------+-----------+
 
 
 select * from Loan;
 +---------+------------+-------------+---------+-----------+
 | loan_no | loan_amt   | no_of_years | cust_no | branch_no |
 +---------+------------+-------------+---------+-----------+
 |       2 | 1000000.00 |           3 |       2 |         1 |
 |       3 |   20000.00 |           1 |       3 |         2 |
 |       4 | 4000000.00 |           7 |       4 |         3 |
 |       6 |  500000.00 |           2 |       2 |         3 |
 |       7 |   20000.00 |           1 |       1 |         5 |
 |       8 |   50000.00 |           1 |       4 |         5 |
 +---------+------------+-------------+---------+-----------+
 
 

 (a) Queries: 
 1. Find out customer name having loan amt >10000 
 
select
    distinct cust_name as "people having loan > 10000"
from
    Customer c,
    Loan l
where
    loan_amt > 10000
    and c.cust_no = l.cust_no;


 +----------------------------+
 | people having loan > 10000 |
 +----------------------------+
 | Wallabh                    |
 | Yash                       |
 | Saurabh                    |
 | Shubham                    |
 +----------------------------+
 

2. Select customers having account but not loan. 

select
    distinct c.cust_no,
    c.cust_name
from
    Customer c,
    Account a
where
    c.cust_no = a.cust_no
    and a.cust_no not in(select cust_no from Loan);


 +---------+-----------+
 | cust_no | cust_name |
 +---------+-----------+
 |       5 | Kalyani   |
 +---------+-----------+
 
 

3. Select customers having account as well as loan. 

select distinct c.cust_no, c.cust_name
from Customer c, Account a, Loan l
where c.cust_no = a.cust_no and a.cust_no = l.cust_no;


 +---------+-----------+
 | cust_no | cust_name |
 +---------+-----------+
 |       1 | Shubham   |
 |       2 | Wallabh   |
 |       3 | Yash      |
 |       4 | Saurabh   |
 +---------+-----------+
 

4. Find out customer names having loan at ‘Pimpri’ branch.

select cust_name
from Customer c, Account a, Branch b
where
    c.cust_no = a.cust_no
    and a.branch_no = b.branch_no
    and branch_city = "Pimpri";


 +-----------+
 | cust_name |
 +-----------+
 | Saurabh   |
 +-----------+
 


5. Find out customer names having Saving account. 

select cust_name from Customer c, Account a
where c.cust_no = a.cust_no and acc_type = "savings";

 +-----------+
 | cust_name |
 +-----------+
 | Shubham   |
 | Saurabh   |
 | Kalyani   |
 +-----------+


6. Find out the total of all the loan amount at Nagar Branch.

select
    sum(loan_amt) as "total loan at Nagar Branch"
from
    Loan l,
    Branch b
where
    b.branch_no = l.branch_no
    and branch_name = "Nagar";

 +----------------------------+
 | total loan at Nagar Branch |
 +----------------------------+
 |                   70000.00 |
 +----------------------------+
 

7. List the names of customers who have taken loan from the branch in the same city they live. 
select cust_name
from Customer c, Branch b, Loan l
where c.cust_no = l.cust_no and c.cust_city = b.branch_city and b.branch_no = l.branch_no;


 +-----------+
 | cust_name |
 +-----------+
 | Wallabh   |
 | Yash      |
 +-----------+
 

(b) Stored Procedures: 

 a) Write a procedure to transfer amount of 1000 Rs. from account_no 1 to account_no 2*/
Delimiter // 
Create procedure transferAmount() 
Begin
    update
        Account
    set
        balance = (
            case
                when acc_no = 1 then (balance - 1000)
                when acc_no = 2 then (balance + 1000)
            end
        )
    where
        acc_no in (1, 2);
End //


select acc_no, balance from Account where acc_no in(1, 2);

 +--------+------------+
 | acc_no | balance    |
 +--------+------------+
 |      1 | 1000000.00 |
 |      2 |  600000.00 |
 +--------+------------+
 
 call transferAmount();
 Query OK, 2 rows affected (0.23 sec)
 
 mysql> select acc_no, balance from Account where acc_no in(1,2);
 +--------+-----------+
 | acc_no | balance   |
 +--------+-----------+
 |      1 | 999000.00 |
 |      2 | 601000.00 |
 +--------+-----------+

b) Write a procedure withdrawal for the following 
 1. Accept balance amount and acc_no for withdrawal as input parameters. 
 2. Check if input amount is less than actual balance of accounts. 
 3. If input amount is less ,give the message “withdrawal allowed from account” otherwise give the  
 message “withdrawal not allowed from account”. Update the balance field. 
 
Delimiter // 
Create procedure withdrawAmount(in amount float(9, 2), in ac int) 
Begin 
    declare bal float(9, 2);
    select balance into bal from Account where acc_no = ac;

    IF amount <= bal THEN
        select 'withdrawal allowed from account' as status;

        update Account set balance = balance - amount where acc_no = ac;
    ELSE
        select 'withdrawal not allowed from account';
    END IF;
End //

select acc_no, balance from Account where acc_no = 1;
 +--------+-----------+
 | acc_no | balance   |
 +--------+-----------+
 |      1 | 998000.00 |
 +--------+-----------+

call withdrawAmount(1000, 1);

 +---------------------------------+
 | status                          |
 +---------------------------------+
 | withdrawal allowed from account |
 +---------------------------------+
select acc_no, balance from Account where acc_no = 1;
 +--------+-----------+
 | acc_no | balance   |
 +--------+-----------+
 |      1 | 997000.00 |
 +--------+-----------+
 

(c) Stored Functions: 
 
 a) Write a function that returns the total loan amount of a particular branch. 
 ( Accept branch name as input parameter.) 

delimiter $$ 
create function totalLoanAtBranch(b_name varchar(20)) returns float 
deterministic 
begin 
    declare total_loan_amt float(9, 2);
    select sum(loan_amt) into total_loan_amt
    from Loan l, Branch b
    where b.branch_no = l.branch_no and branch_name = b_name;

    return total_loan_amt;
end $$

select totalLoanAtBranch("SBI Kalasagar");

 +------------------------------------+
 | totalLoanAtBranch("SBI Kalasagar") |
 +------------------------------------+
 |                            4500000 |
 +------------------------------------+
 

 b) Write a function to count the no. of customers of particular branch. 
 (Accept branch name as input parameter).
 
delimiter $$ 
create function countCustomers(b_name varchar(20)) returns int 
deterministic 
begin 
    declare number_of_customers int;
    select count(*) into number_of_customers
    from Account a, Branch b
    where a.branch_no = b.branch_no and branch_name = b_name;

    return number_of_customers;
end $$


select countCustomers("CIDCO");

 +-------------------------+
 | countCustomers("CIDCO") |
 +-------------------------+
 |                       2 |
 +-------------------------+
 

(d) Cursors: 
 
 a) Write a procedure using cursor to display the customers having loan 
 amounts between 40000 and 50000 from branch name 'CIDCO'..

delimiter $$ 
DROP PROCEDURE IF EXISTS displayCustomer;
CREATE PROCEDURE displayCustomer() 
BEGIN 
    declare cno int; declare lno int; declare amt float(9,2);declare cname varchar(30);declare bname varchar(20);
    declare cur cursor for
    select c.cust_no, cust_name, loan_no, loan_amt, branch_name
        from Customer c,Loan l, Branch b where l.branch_no = b.branch_no and c.cust_no = l.cust_no;

    open cur;
    loop fetch cur into cno, cname, lno, amt, bname;
        if bname = 'CIDCO' and 40000 < amt and amt < 50000 then 
            select cno, cname, lno, amt;
        end if;
    end loop;
    close cur;
END $$ 

call displayCustomer();


+------+---------+------+----------+
| cno  | cname   | lno  | amt      |
+------+---------+------+----------+
|    1 | Shubham |    9 | 43000.00 |
+------+---------+------+----------+
1 row in set (0.00 sec)

+------+---------+------+----------+
| cno  | cname   | lno  | amt      |
+------+---------+------+----------+
|    5 | Kalyani |   10 | 45000.00 |
+------+---------+------+----------+
1 row in set (0.00 sec)



 b) Write a procedure using cursor add an interest of 3% to the balance of all  
 accounts having balance > 5000.
 
DROP PROCEDURE IF EXISTS addInterest;
delimiter $$
CREATE PROCEDURE addInterest() BEGIN 
declare bal float(8,2);
declare ac int;
declare cur cursor for select acc_no, balance from Account;
open cur;
loop fetch cur into ac, bal;
    if bal > 5000 then
        update Account set balance = balance + balance * 0.03 where acc_no = ac;
        select concat("added interest", ac);
    end if;
end loop;
close cur;
END $$

select * from Account where balance > 5000;

+--------+----------+------------+---------+-----------+
| acc_no | acc_type | balance    | cust_no | branch_no |
+--------+----------+------------+---------+-----------+
|      1 | savings  | 1089448.75 |       1 |         4 |
|      2 | current  |  619030.00 |       2 |         1 |
|      3 | salary   |  463500.00 |       3 |         2 |
|      4 | savings  |  366216.50 |       4 |         3 |
|      5 | savings  |  103000.00 |       5 |         4 |
|      6 | salary   |  726150.00 |       5 |         1 |
|      7 | current  |   82400.00 |       4 |         5 |
|      8 | current  |   51500.00 |       1 |         5 |
+--------+----------+------------+---------+-----------+

call addInterest();
select * from Account where balance > 5000;

+--------+----------+------------+---------+-----------+
| acc_no | acc_type | balance    | cust_no | branch_no |
+--------+----------+------------+---------+-----------+
|      1 | savings  | 1122132.25 |       1 |         4 |
|      2 | current  |  637600.88 |       2 |         1 |
|      3 | salary   |  477405.00 |       3 |         2 |
|      4 | savings  |  377203.00 |       4 |         3 |
|      5 | savings  |  106090.00 |       5 |         4 |
|      6 | salary   |  747934.50 |       5 |         1 |
|      7 | current  |   84872.00 |       4 |         5 |
|      8 | current  |   53045.00 |       1 |         5 |
+--------+----------+------------+---------+-----------+




(e) Triggers:  

a) Write a trigger which will execute when account_no is less than 0 . Display the 
 appropriate message. */
DROP TRIGGER IF EXISTS check_acc_no;

DELIMITER $$

    CREATE TRIGGER check_acc_no BEFORE INSERT ON `Account`
    FOR EACH ROW BEGIN
      IF (NEW.acc_no < 0) THEN
        signal sqlstate '45000' set message_text = 'accpunt number cant be less than 0';
      END IF;
    END$$

DELIMITER ;

insert into Account values(-1,"savings", 5000, 3, 5);

ERROR 1644 (45000): accpunt number cant be less than 0




b) Write a trigger which will execute when loan_amount is updated. Do not allow to update. Display  
the message that ' loan amount once given cannot be updated.'


DROP TRIGGER IF EXISTS loan_amt_update;

DELIMITER $$

    CREATE TRIGGER loan_amt_update BEFORE UPDATE ON `Loan`
    FOR EACH ROW BEGIN
      IF NEW.loan_amt IS NOT NULL THEN
        signal sqlstate '45000' set message_text = 'you cant update loan amount';
      END IF;
    END$$

DELIMITER ;

update Loan set loan_amt = 0 where cust_no = 1;

ERROR 1644 (45000): you cant update loan amount


(f) Views: 
 
 a) Create a view which contains all the customer details along with the details of all accounts of that  
 customer.

create or replace view customer_accounts_view as
select c.cust_no, cust_name, acc_no, acc_type, balance, branch_name, cust_city
    from Customer c, Account a, Branch b
    where c.cust_no = a.cust_no and a.branch_no = b.branch_no;

select * from customer_accounts_view;

 +---------+-----------+--------+----------+-----------+---------------+-----------+
 | cust_no | cust_name | acc_no | acc_type | balance   | branch_name   | cust_city |
 +---------+-----------+--------+----------+-----------+---------------+-----------+
 |       1 | Shubham   |      1 | savings  | 997000.00 | SBI Vadgaon   | Pune      |
 |       1 | Shubham   |      8 | current  |  50000.00 | Nagar         | Pune      |
 |       2 | Wallabh   |      2 | current  | 601000.00 | CIDCO         | Pune      |
 |       3 | Yash      |      3 | salary   | 450000.00 | Sadashiv Peth | Pune      |
 |       4 | Saurabh   |      4 | savings  | 355550.00 | SBI Kalasagar | Pune      |
 |       4 | Saurabh   |      7 | current  |  80000.00 | Nagar         | Pune      |
 |       5 | Kalyani   |      5 | savings  | 100000.00 | SBI Vadgaon   | Pune      |
 |       5 | Kalyani   |      6 | salary   | 705000.00 | CIDCO         | Pune      |
 +---------+-----------+--------+----------+-----------+---------------+-----------+
 


b) Create a view which contains details of all loans from the ‘sadashiv peth’ branch. 
 
create or replace view sadashiv_peth_loans as
select c.cust_no, cust_name, loan_no, loan_amt, no_of_years
from Branch b, Loan l, Customer c
where branch_name = "Sadashiv Peth" and b.branch_no = l.branch_no and c.cust_no = l.cust_no;

select * from sadashiv_peth_loans;

 +---------+-----------+---------+----------+-------------+
 | cust_no | cust_name | loan_no | loan_amt | no_of_years |
 +---------+-----------+---------+----------+-------------+
 |       3 | Yash      |       3 | 20000.00 |           1 |
 +---------+-----------+---------+----------+-------------+
 