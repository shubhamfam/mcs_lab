(:I. Retrieve the names of students enrolled in the ‘Automata’ 
class in the term of Fall 1996.:)

let $cno := doc("Gradebook.xml")/gradebook/grade/catalogs/catalog[ctitle="Automata"]/cno

let $course := doc("Gradebook.xml")/gradebook/grade/courses/course[cno=$cno]

let $enrolls := doc("Gradebook.xml")/gradebook/grade/enrolls/enroll[term = "f96" and secno=$course/secno]

let $students := doc("Gradebook.xml")/gradebook/grade/students/student[sid=$enrolls/sid]

for $student in $students
return <student>
        {concat($student/fname, " ",$student/lname)}
       </student>
