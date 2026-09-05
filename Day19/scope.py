'''
def display(n):
    n=n+10
    print('Inside:',n)

n=10
display(n)
print('Outside:',n)
'''
'''
def display():

    print('Inside:',n)

n=10
display()
print('Outside:',n)
'''
'''
def display(n):
    global n
    n=n+10
    print('Inside:',n)

n=10
display(n)
print('Outside:',n)
'''
'''
def display():
    n=n+10
    print('Inside:',n)

display()
print('Outside:',n)
'''
'''
def display():
    global n
    n='PFS'
    print("updated course:",n)
n='JFS'
display()
print("final course:",n)
'''
'''
def display():
    n='PFS'
    def update():
        nonlocal n
        n='PFS'
        print("updated course:",n)
    update()
    print("final course:",n)
display()
'''
l=[1,2,3,4,5]
max=20
sum = 10
print(sum)

