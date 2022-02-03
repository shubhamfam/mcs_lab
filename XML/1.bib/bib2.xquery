(:ii. Find all books authored by "Raghu Ramakrishnan".:)

for $x in doc("bib.xml")/bib/book
where $x/author/first = 'Raghu' and $x/author/last = 'Ramakrishnan'
return <books>{$x}</books>
