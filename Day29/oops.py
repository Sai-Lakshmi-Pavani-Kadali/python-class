'''
class Flipkart:
    products={'shirts':1000,'handbag':2000,'pants':3000}
    discount=30

    @classmethod
    def display(cls):
        print(cls.products)
    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name},Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going-on,grab the products...")
david=Flipkart()
david.userinfo('david',9978456102,'Hyd')
david.displaydiscount()
david.display()
jack=Flipkart()
jack.userinfo('jack',8899774411,'chennai')
jack.displaydiscount()
jack.display()
alex=Flipkart()
alex.userinfo('alex',8877552101,'guntur')
alex.displaydiscount()
alex.display()
'''
'''
class Flipkart:
    products={'shirts':1000,'handbag':2000,'pants':3000}
    discount=30

    @classmethod
    def display(cls):
        print(cls.products)
    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name},Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going-on,grab the products...")
david=Flipkart()
david.userinfo('david',9978456102,'Hyd')
david.displaydiscount()
david.display()
print(david.products)
print(david.name)

Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)

#using object -> ins,cls,sta,clsatt,insatt
#using class  -> cls,sta,clsatt
'''
class user:
    def __init__(self,name,email,phonenumber,password):
        self.name=name
        self.email=email
        self.phonenumber=phonenumber
        self.password=password

    def register(self):
        if self.name == "":
            print("Registraction is failed:Name is required")
        elif self.email == "":
            print("Registraction is failed:Email is required")
        elif self.phonenumber == "":
            print("Registraction is failed: phonenumber is reqired")
        elif self.password == "":
            print("Registraction is failed:passwors")

