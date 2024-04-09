class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return (f'Title: {self.title} \nAuthor: {self.author}, \nPages: {self.pages}')

book1 = Book('Python crash Course', 'Monty Python', 800)
book2 = Book('JavaScript for begginers', 'Steve Jobs', 820)
print(book1)
vysledek = book1.author + book2.author
print(vysledek)

