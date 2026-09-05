Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=input()
asdf
x
'asdf'
name=input()
pavani
name=input("enter the name:")
enter the name:pavani
name
'pavani'
age=input("Enter the age")
Enter the age22
age
'22'
age=input("enter the age:")
enter the age:21
age
'21'
type(age)
<class 'str'>
price=input("Enter the price:")
Enter the price:99.99
price
'99.99'
price=float(input("Enter the price: "))
Enter the price: 99.99
price
99.99
names=input("Enter the names: ")
Enter the names: pavani codegnan pfs
names
'pavani codegnan pfs'
names.split()
['pavani', 'codegnan', 'pfs']
names=input("Enter the names: ").split()
Enter the names: pavani codegnan pfs
names
['pavani', 'codegnan', 'pfs']
names=input("Enter the names: ").split()
Enter the names: 12345
names
['12345']
map(int,names)
<map object at 0x000001FDE88A5A00>
list(map(int,names))
[12345]
values=list(map(int,input().split()))
123456765378
values
[123456765378]
[1.0, 2.0, 3454.0, 5463.23]
[1.0, 2.0, 3454.0, 5463.23]
names=tuple(input("Enter the names: ").split())
Enter the names: fghj fdghj fgh
names
('fghj', 'fdghj', 'fgh')
values=tuple(map(int,input().split()))
1234
values
(1234,)
values=tuple(map(float,input().split()))
567 5678 567
values
(567.0, 5678.0, 567.0)
names=set(input().split())
ytuio true tyu
names
{'true', 'ytuio', 'tyu'}
values=set(map(int,input().split()))
1234
values
{1234}
a,b=[1,2]
a
1
b
2
a,b=(1,2)
a
1
b
2
email,password=input("Enter the email and password: ").split()
Enter the email and password: pavani@gmail.com 12334
email
'pavani@gmail.com'
password
'12334'
a,b,c=list(map(int,input().split()))
123
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 1)
1 2 3
SyntaxError: invalid syntax
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
name,marks=input().split()
pavani 29
name
'pavani'
marks
'29'
int(marks)
29
e=eval(input())
1
e
1
e=eval(input())
1234.13
e
1234.13
e=eval(input())
"satwika"
SyntaxError: multiple statements found while compiling a single statement
>>> e=eval(input())
[1,2,3,4,4,5]
>>> e
[1, 2, 3, 4, 4, 5]
>>> e=eval(input())
[1,12.4,"str",[1,2,3]]
>>> e
[1, 12.4, 'str', [1, 2, 3]]
>>> e=eval(input())
(1,2,4,3)
... >>> e
>>> e
(1, 2, 4, 3)
>>> e=eval(input())
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    >>> e
    ^^
SyntaxError: invalid syntax
>>> e=eval(input())
[1,2,3,4,5]
>>> e
[1, 2, 3, 4, 5]
>>> e=eval(input())
{1,2,3,4,5}
>>> e=eval(input())
{1:1,2:2,3:3}
>>> e
{1: 1, 2: 2, 3: 3}
>>> e=eval(input())
True
>>> e
True
>>> e=eval(input())
2+3*4+5*8
>>> e
54
