for $x at $i in doc("Gradebook.xml")/gradebook/grade/students/student
return <li>{$i}. {data($x)}</li>





