(:e. Retrieve the names of employees who work on 
all projects controlled by department “5”.:)

let $employees := doc("company.xml")/companyDB/employees/employee[@worksFor="5"]

for $employee in $employees
return <li>{concat($employee/fname, " ", $employee/lname)}</li>