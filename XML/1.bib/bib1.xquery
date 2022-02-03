
(:i. Find books that have "Temporal" in their titles.:)

for $x in doc("bib.xml")/bib/book
where contains($x/title, 'Temporal') = true()
return <books>{$x}</books>





