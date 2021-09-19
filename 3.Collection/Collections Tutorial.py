#Create a dictionary where they keys are books, and the values are their authors.
books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}

print(books)

print(books["The Handmaiden's Tale"]) #We can query the author of any book


#However if we try to query what books have been written by an author, we get the following error.

#print(books["Margaret Atwood"])
#KeyError: 'Margaret Atwood'
#This is because "Margaret Atwood" is a value not a key.
#Recall we cannot query a dictionary using a value.





