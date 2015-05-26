#!/usr/bin/python
# Filename: simplestclass.py

# class Person:
#     pass # An empty block

# p = Person()
# print p

class Person:
    def sayHi(self):
        print 'Hello, how are you?'

p = Person().sayHi()

# This short example can also be written as Person().sayHi()