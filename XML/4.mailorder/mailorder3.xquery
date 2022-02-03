(:III. Retrieve the pairs of customer number values of 
customers who live in the same zip code:)

let $customers := doc("Mailorder.xml")/mailorder/customers/customer

for $zip in distinct-values($customers/zip)
return <zip code="{$zip}">{
         for $cust in $customers
         where $zip = $cust/zip
         order by $zip
         return $cust/cno
       }</zip>


