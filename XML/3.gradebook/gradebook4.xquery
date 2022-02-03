(:IV. Retrieve the names of students who 
have not enrolled in any class.:)

let $students := doc("Gradebook.xml")/gradebook/grade/students/student

let $enrolls := doc("Gradebook.xml")/gradebook/grade/enrolls/enroll/sid

for $student in $students
where $student/sid[not(.= $enrolls)]
return <li>{concat($student/fname, " ", $student/lname)}</li>