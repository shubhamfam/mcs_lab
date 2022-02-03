(:V. Retrieve the names of customers who have 
ordered all parts costing less than 20.00uits.:)
let $doc := doc("Mailorder.xml")/mailorder

let $cheap_parts := $doc/parts/part[price < 20.00]

let $orderdets := $doc/odetails/odetail[pno = $cheap_parts/pno]

for $orderdet in $orderdets,
    $order in $doc/orders/order[ono = $orderdet/ono],
    $cust in $doc/customers/customer[cno = $order/cno]
where count(distinct-values($cheap_parts)) = count(distinct-values($orderdet/pno))
return <li>{string($cust/cname)}</li>
