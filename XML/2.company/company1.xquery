(:a. Retrieve the names and addresses of employees
    who work for the “Research” department.:)
    
let $dept := doc("company.xml")/companyDB/departments/department[dname="Research"]

let $employees := doc("company.xml")/companyDB/employees/employee

for $employee in $employees
where contains($dept/employees/@essns, $employee/@ssn) = true()
return  <employee>
            <name>{concat($employee/fname, " ", $employee/lname)}</name>
            {$employee/address}
        </employee>