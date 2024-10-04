class Book:
 def __init__(self, title, author):
   self.title = title
   self.author = author
 def __eq__(self, other):
   return self.title == other.title and self.author == other.author
book1 = Book('Python Programming', 'John Doe')
book2 = "Python Programming"
print(book1 == book2)