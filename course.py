#!/usr/bin/env python

#-----------------------------------------------------------------------
# course.py
#modeled after Book.py
#-----------------------------------------------------------------------

class Course:

    def __init__(self, dept, num, title):
        self._num = num
        self._title = title
        self._dept = dept
    
    def get_dept(self):
        return self._dept

    def get_num(self):
        return self._num

    def get_title(self):
        return self._title

    def to_tuple(self):
        return (self._dept, self._num, self._title)

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
