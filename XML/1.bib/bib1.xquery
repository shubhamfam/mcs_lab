
(:i. Find books that have "Temporal" in their titles.:)

for $x in doc("bib.xml")/bib/book
where contains($x/title, 'Temporal') = true()
return <books>{$x}</books>


(:iii. Find number of books with 3 or more than 3 authors.:)

(:iv. Find all books that have price more than 40 units.:)



