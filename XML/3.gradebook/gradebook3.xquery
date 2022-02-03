(:III. Retrieve the SID values of students who have
enrolled in CSc226 or CSc227.:)

let $courses := doc("Gradebook.xml")/gradebook/grade/courses/course[cno = "CSc226" or cno="CSc227"]

let $enrolls := doc("Gradebook.xml")/gradebook/grade/enrolls/enroll[secno=$courses/secno]


return <sids>{distinct-values($enrolls/sid)}</sids>