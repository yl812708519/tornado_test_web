from sqlalchemy.sql import expression

__author__ = 'wangshubin'

a = [1, 2, 3]
b = [4, 5, 6]
c = a+b
# print(c)

class A(object):
    a = 1
    b = 2

arr = (A.a == "a", A.b == 1, "c" >= "a")
for cri in list(arr):
    e = expression._literal_as_text(cri)
    print e
