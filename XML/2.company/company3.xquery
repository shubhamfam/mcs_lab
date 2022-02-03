(:c. Retrieve the names of all employees who have two or more dependents.:)

let $employees := doc("company.xml")/companyDB/employees/employee

for $emp in $employees
where count($emp/dependents/dependent) >= 2
return <employee>{concat($emp/fname," ", $emp/lname)}</employee>