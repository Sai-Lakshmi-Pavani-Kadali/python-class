'''
greater = lambda a,b: a if a>b else b

print(greater(12,13))
print(greater(50,70))
print(greater(40,20))
print(greater(16,26))


wish = lambda name: f'Welcome to the course {name}'

print(wish("sai"))
print(wish("lakshmi"))
print(wish("pavani"))

iseven = lambda n: "Even" if n%2==0 else "odd"

print(iseven(45))
print(iseven(18))
print(iseven(17))


avg = lambda a,b,c: (a+b+c)/3

print(avg(4,5,6))
print(avg(30,26,615))
'''
'''
domain=lambda mail: (mail.split('@')[-1]).split('.')[0]

print(domain('sowmya@codegnan.com'))
print(domain('sowmya@gmail.com'))
print(domain('sowmya@outlook.com'))
print(domain('sowmya@ahoo.com'))
'''
'''
get=lambda price:price+price*0.18


print(get(1000))
print(get(5000))
print(get(8000))
'''
'''
prices=[5678,8765,5467,122,1600,3000]

res = list(map(lambda price : price + price*0.18, prices))

print(res)
'''
'''
names = ['sai','lakshmi','pavani','ammu','divya','vennela']

res = list(map(lambda name: name.title(),names))

print(res)
'''
'''
prices=[5678,8765,5467,122,1600,3000]
res = list(map(lambda price : price - price*0.3, prices))
print(res)
'''
'''
prices=[4567,2345,6789,1314,4740]
res=list(filter(lambda price:price%2!=0,prices))
print(res)
'''
'''
prices=[5678,8765,5467,122,1600,3000]
res = list(map(lambda price : price > price*0.3, prices))
print(res)
'''
'''
names=['jackhong','alexa','davids','tim','virat','akki']
res=list(filter(lambda name:len(name)>5,names))
print(res)
'''
'''
from functools import reduce
l=[5,567,6,24,124,435,462]
res=reduce(lambda sum,i: sum+i,l)
print(res)

names=['jackhong','alexa','davids','tim','virat','akki']
res=reduce(lambda res,i:res+' '+i,names)
print(res)
'''

products = {'sugar':60,
         'salt':50,
         'eggs':90,
         'cooking oil':120,
         'bread':45
         }

print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))

print(dict(sorted(products.items(),key = lambda i:i[1])))
print(dict(sorted(products.items(),key = lambda i:i[1],reverse=True)))
