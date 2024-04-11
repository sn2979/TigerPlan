#!/usr/bin/env python

#-----------------------------------------------------------------------
# course.py
#modeled after Book.py
#-----------------------------------------------------------------------

class Course:

    def __init__(self, num, title, courseid):
        self._author = num
        self._title = title
        self._price = courseid

    def get_author(self):
        return self._author

    def get_title(self):
        return self._title

    def get_price(self):
        return self._price

    def to_tuple(self):
        return (self._author, self._title, self._price)

#-----------------------------------------------------------------------

def _test():
    '''
    book = Book('Kernighan', 'The Practice of Programming', 40.74)
    print(book.get_author())
    print(book.get_title())
    print(book.get_price())
    print(book.to_tuple())
    '''
    

if __name__ == '__main__':
    _test()
