(:II. Retrieve the SID values of students who have 
enrolled in CSc226 as well as CSc227.:)

let $courses := doc("Gradebook.xml")/gradebook/grade/courses/course[cno = "CSc226" or cno="CSc227"]

for $student in doc("Gradebook.xml")/gradebook/grade/students/student
let $enrolled_in := doc("Gradebook.xml")/gradebook/grade/enrolls/enroll[sid=$student/sid and secno = $courses/secno]
where count($courses) = $count($enrolled_in)
return <students>{$student/sid}</students>