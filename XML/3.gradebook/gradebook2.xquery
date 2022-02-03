(:II. Retrieve the SID values of students who have 
enrolled in CSc226 as well as CSc227.:)

let $courses := doc("Gradebook.xml")/gradebook/grade/courses/course[cno = "CSc226" or cno="CSc227"]

let $enrolls := doc("Gradebook.xml")/gradebook/grade/enrolls/enroll[secno=$courses/secno]


return <students>{distinct-values($enrolls/sid)}</students>