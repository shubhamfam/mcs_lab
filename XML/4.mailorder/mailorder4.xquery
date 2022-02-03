(:IV. Retrieve the names of customers who have ordered parts only 
from employees living in the city of Wichita.:)

let $doc :=  doc("Mailorder.xml")/mailorder
let $zip := $doc/zipcodes/zipcode[city = "Wichita"]/zip
let $emps := $doc/employees/employee[zip = $zip]
let $orders := $doc/orders/order[eno = $emps/eno]
let $customers := $doc/customers/customer[cno = $orders/cno]

return <customers>{$customers/cname}</customers>
