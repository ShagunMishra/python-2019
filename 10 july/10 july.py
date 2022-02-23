Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
b1=True
>>> print(b1)
True
>>> b1
True
>>> type(b1
     )
<class 'bool'>
>>> id(b1)
140734902597968
>>> b1=b2=b3=b4=True
>>> b2=False
>>> c1=3+3j
>>> print(c1)
(3+3j)
>>> type(c1)
<class 'complex'>
>>> id(c1)
2752409311600
>>> q1[10,20,30]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    q1[10,20,30]
NameError: name 'q1' is not defined
>>> q1=[10,20,30]
>>> b1=bytes(q1)
>>> type(b1)
<class 'bytes'>
>>> b1[0]
10
>>> b1
b'\n\x14\x1e'
>>> b1[0]=20
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b1[0]=20
TypeError: 'bytes' object does not support item assignment
>>> b1=[10,20,30]
>>> b2=bytearray(b1)
>>> type(b2)
<class 'bytearray'>
>>> b2[0]=20
>>> print(b2[0])
20
>>> b2[1]
20
>>> r1=range(1,11)
>>> r1[0]
1
>>> r1[6]
7
>>> for i in r1:
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> r2=range(0,100,10)
>>> r2
range(0, 100, 10)
>>> print(r2)
range(0, 100, 10)
>>> for i in r2:
	print(i)

	
0
10
20
30
40
50
60
70
80
90
>>> a=100
>>> b=200
>>> a+b
300
>>> a=b=None
>>> print(a)
None
>>> print(b)
None
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> a=10+1.5j
>>> b=30+2.5j
>>> c=a+b
>>> print(c)
(40+4j)
>>> s=5
>>> a="hello"
>>> print(a)
hello
>>> print(s)
5
>>> s="hi"
>>> s
'hi'
>>> s='hello'
>>> s
'hello'
>>> s="a"
>>> type(s)
<class 'str'>
>>> a=10#comment
>>> b=10""" hell
"""
SyntaxError: invalid syntax
>>> 
============================= RESTART: E:/asw.py =============================
>>> 
============================= RESTART: E:/asw.py =============================
10
>>> x,y,z="Örange","Mango","Banana"
>>> print(z)
Banana
>>> x="Awesom"
>>> print("Python is"+x)
Python isAwesom
>>> print("Python is "+x)
Python is Awesom
>>> print("Python is very", x)
Python is very Awesom
>>> x="Python is "
>>> y="Awesom"
>>> z=x
>>> z=x+y
>>> print(z)
Python is Awesom
>>> x=5
>>> y="HELLO"
>>> z=x+y
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    z=x+y
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> tata="Nylon"
>>> 
============================= RESTART: E:/sha.py =============================
Enter the nameshagu
>>> 
============================= RESTART: E:/sha.py =============================
Enter the namevaransi
Welcome
Hi
Hi jhghb
>>> 
============================= RESTART: E:/sha.py =============================
Enter the namejhiuguib
Hi jhghb
>>> 
========================== RESTART: E:/even odd.py ==========================
Enter the Number: 6
Number is Even
>>> 
========================== RESTART: E:/even odd.py ==========================
Enter the Number: 7
hellooooo
>>> 
========================== RESTART: E:/even odd.py ==========================
Enter the Number: 8
Number is Even
hellooooo
>>> 
========================== RESTART: E:/even odd.py ==========================
Enter the Number: 9
Number is odd
hellooooo
>>> 
============================= RESTART: E:/odd.py =============================
Enter the number: 5
Number is odd
>>> 
============================= RESTART: E:/odd.py =============================
Enter the number: 4
>>> 
============================ RESTART: E:/test.py ============================
Enter the number: 5
The number is positive.
>>> 
============================ RESTART: E:/test.py ============================
Enter the number: 0
The number is zero.
>>> 
============================ RESTART: E:/test.py ============================
Enter the number: -2
The number is negative.
>>> 
============================ RESTART: E:/gret.py ============================
Enter the 1st number:3
Enter the 2nd number:5
Enter the 3rd number:8
8
>>> 
============================ RESTART: E:/gret.py ============================
Enter the 1st number:4
Enter the 2nd number:9
Enter the 3rd number:6
Greater number is:  9
>>> 
============================ RESTART: E:/gret.py ============================
Enter the 1st number:3
Enter the 2nd number:6
Enter the 3rd number:7
Greater number is:  7
>>> 
============================ RESTART: E:/gret.py ============================
Enter the 1st number:2
Enter the 2nd number:3
Enter the 3rd number:7
Greater number is:  7
>>> 
