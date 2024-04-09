class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return (f'Title: {self.title} \nAuthor: {self.author}, \nPages: {self.pages}')

    def __add__(self, other):
        self.other = other
        return self.other

book1 = Book('Python crash Course', 'Monty Python', 800)
book2 = Book('JavaScript for begginers', 'Steve Jobs', 820)
book3 = Book('JavaScript for begginers', 'Steve Jobs', 890)
print(book1)
vysledek = book1.pages + book2.pages + book3.pages
nazev = book1.title + book2.title + book3.title
print(f'vysledek je: {vysledek}')
print(nazev)

