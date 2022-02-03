(:II. Retrieve the names and cities of employees who have 
taken orders for parts costing more than 50.00 units:)

let $doc := doc("Mailorder.xml")/mailorder

for $odetail in $doc//odetails/odetail,
    $part in $doc//parts/part[pno = $odetail/pno],
    $order in $doc//orders/order[ono = $odetail/ono],
    $emp in $doc/employees/employee[eno = $order/eno],
    $zip in $doc//zipcodes/zipcode[zip = $emp/zip]
where $part/price > 50.00
return <emp>{$emp/ename}{$zip/city}</emp>
