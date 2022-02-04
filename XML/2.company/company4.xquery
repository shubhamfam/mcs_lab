(:d. Retrieve the names of managers 
who have at least one dependent.:)

let $managers := doc("company.xml")/companyDB/employees/employee[@manages]

for $manager in $managers
where count($manager/dependents/dependent) >= 1
return <li>
        {concat($manager/fname, " ", $manager/lname)}
       </li>
