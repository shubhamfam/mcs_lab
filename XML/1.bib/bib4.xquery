(:iv. Find all books that have price more than 40 units.:)

for $x in doc("bib.xml")/bib/book
where $x/price > 40
return <li>{$x}</li>