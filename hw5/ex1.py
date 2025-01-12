class Book:
    title = None
    author = None
    year = None
    def get_info(self):
        print(self.title,'\n', self.author, '\n', self.year, sep='')

new_book = Book()
new_book.title = '400 days'
new_book.author = 'Mike Jordan'
new_book.year = 2004
new_book.get_info()