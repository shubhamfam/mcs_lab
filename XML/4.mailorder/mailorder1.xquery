(:I. Retrieve the names of parts that cost less than 20.00units.:)

let $cheap_parts := doc("Mailorder.xml")/mailorder/parts/part[price < 20.00]

return <cheap_parts>
            {$cheap_parts/pname} 
       </cheap_parts>