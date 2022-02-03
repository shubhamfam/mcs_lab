(:VII. Retrieve the names of customers 
who have placed exactly two orders.:)

let $customers := doc("Mailorder.xml")/mailorder/customers/customer

for $customer in $customers
let $orders_placed := doc("Mailorder.xml")/mailorder/orders/order[cno = $customer/cno]
where count($orders_placed) = 2
return <li>{string($customer/cname)}</li>