import time
from datetime import datetime, timedelta


class Book:
    def __init__(self, no, title, author, amount):
        self.no = no
        self.title = title
        self.author = author
        self.existing = amount  # 现存量
        self.stock = amount  # 库存量


class Reader:

    def __init__(self, borrow_id):
        self.borrow_id = borrow_id


def buy_book(book, book_dict, amount):
    if book.no in book_dict:
        book_dict[book.no].stock += amount
    else:
        book.existing = amount
        book.stock = amount
        book_dict[book.no] = book


def back_book(book, reader, borrow_dict):
    book.existing += 1
    list1 = borrow_dict[reader.borrow_id]
    index = 0
    for i in range(len(list1)):
        if book.no == list1[i][0].no:
            index = i
            break
    del list1[index]


def borrow_book(book, reader, borrow_dict):
    if book.existing > 0:
        book.existing -= 1
        if reader.borrow_id in borrow_dict:
            borrow_dict[reader.borrow_id].append([book, datetime.now() + timedelta(days=1)])  # 允许借1天
        else:
            borrow_dict[reader.borrow_id] = [[book, datetime.now() + timedelta(days=1)]]


if __name__ == '__main__':
    book1 = Book(no="1", title="数据结构", author="张三", amount=100)
    book_dict = {book1.no: book1}
    borrow_dict = {}
