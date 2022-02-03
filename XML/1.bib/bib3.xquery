(:iii. Find number of books with 3 or more than 3 authors.:)

let $books := doc("bib.xml")/bib/book[count(author) >= 3]

return <p>{"No. of books with atleast 3 authors: " , count($books)}</p>


