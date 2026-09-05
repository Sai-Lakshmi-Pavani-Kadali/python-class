Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=92.25
int(b)
92
complex(b)
(92.25+0j)
str(b)
'92.25'
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
True
True
c=3+4j
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(3+4j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s='codegnan'
int(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
10:'codegnan'
SyntaxError: illegal target for annotation
10:'codegnan'
SyntaxError: illegal target for annotation
10: 'codegnan'
SyntaxError: illegal target for annotation
float(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
string
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    string
NameError: name 'string' is not defined. Did you forget to import 'string'?
s='codegnan'
int(s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
{'a', 'e', 'c', 'n', 'd', 'o', 'g'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
l=[1,2,3,4,5,"abcd"]
int(l)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
"[1, 2, 3, 4, 5, 'abcd']"
tuple(l)
(1, 2, 3, 4, 5, 'abcd')
set(l)
{1, 2, 3, 4, 5, 'abcd'}
dict(l)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4,5,6,"aceg")
int(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(t)
"(1, 2, 3, 4, 5, 6, 'aceg')"
list(t)
[1, 2, 3, 4, 5, 6, 'aceg']
set(t)
{1, 2, 3, 4, 5, 6, 'aceg'}
dict(t)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
d={1,2,3,4("abcd")}
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    d={1,2,3,4("abcd")}
TypeError: 'int' object is not callable
d={1,2,3,4,("abcd")}
int(d)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(d)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'set'
complex(d)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'set'
str(d)
"{1, 2, 3, 4, 'abcd'}"
tuple(d)
(1, 2, 3, 4, 'abcd')
list(d)
[1, 2, 3, 4, 'abcd']
dict(d)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dict(d)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
set(d)
{1, 2, 3, 4, 'abcd'}
bool(d)
True
r={'Name':'john','Batch':63,'Course':'PFS'}
int(r)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    int(r)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(r)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    float(r)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(r)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    complex(r)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(r)
"{'Name': 'john', 'Batch': 63, 'Course': 'PFS'}"
>>> list(r)
['Name', 'Batch', 'Course']
>>> tuple(r)
('Name', 'Batch', 'Course')
>>> set(r)
{'Name', 'Course', 'Batch'}
>>> bool(r)
True
>>> q=True
>>> int(q)
1
>>> float(q)
1.0
>>> complex(q)
(1+0j)
>>> str(q)
'True'
>>> tuple(q)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    tuple(q)
TypeError: 'bool' object is not iterable
>>> list(q)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list(q)
TypeError: 'bool' object is not iterable
>>> set(q)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    set(q)
TypeError: 'bool' object is not iterable
>>> dict(q)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    dict(q)
TypeError: 'bool' object is not iterable
