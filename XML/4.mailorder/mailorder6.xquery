(:VI. Retrieve the names of customers 
who have not placed a single order.:)

let $customers := doc("Mailorder.xml")/mailorder/customers/customer

let $cust_who_ordered := doc("Mailorder.xml")/mailorder/orders/order/cno

for $customer in $customers
where $customer/cno[not(.= $cust_who_ordered)]
return <li>{string($customer/cname)}</li>
