(:Retrieve the names of students who have enrolled in all 
courses in the catalog table:)

<ul>{
let $catalogs := doc("Gradebook.xml")/gradebook/grade/catalogs/catalog
let $courses := doc("Gradebook.xml")/gradebook/grade/courses/course[cno=$catalogs/cno]/secno
let $enrolls := doc("Gradebook.xml")/gradebook/grade/enrolls/enroll
let $students := doc("Gradebook.xml")/gradebook/grade/students/student

for $student in $students
let $enrolled_in := $enrolls[sid = $student/sid]/secno
where count($courses) = count($enrolled_in)
return <li>{concat($student/fname, " ", $student/lname)}</li>
}</ul> 