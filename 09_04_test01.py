class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print('Title: {}'.format(self.title))
        print('Author: {}'.format(self.author))
        print('Pages: {}'.format(self.pages))

book1 = Book('Python crash Course', 'Monty Python', 800)
book2 = Book('JavaScript for begginers', 'Steve Jobs', 820)
print(book1+book2)

