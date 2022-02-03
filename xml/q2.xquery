for $x in doc("books.xml")/bookstore/book
where $x/price>30
order by $x/string(title)
return $x/string(title)