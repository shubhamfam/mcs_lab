(:b. For every project located in “Stafford”,
retrieve the project number, the controlling
Department number, and the department’s manager’s 
last name, address, and birth date.:)

let $projects := doc("company.xml")/companyDB/projects/project[plocation="Stafford"]

for $project in $projects
let $department := doc("company.xml")/companyDB/departments/department[@dno = $project/@controllingDepartment]
let $manager := doc("company.xml")/companyDB/employees/employee[@ssn = $department/manager/@mssn]
return  <project>
            <pnumber>{$project/@pnumber}</pnumber>
            <controllingDept>{$project/@controllingDepartment}</controllingDept>
            <manager>
                {$manager/lname}
                {$manager/address}
                {$manager/dob}
            </manager>
        </project>