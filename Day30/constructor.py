'''
class Flipkart:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        print(f"Hello {self.name}, Welcome to the flipkart")



david = Flipkart('david',7893329751)
'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)


    def display(self):
        print(self.username,self.__password,self._posts)


pavani = Instagram('pavani','pavani@123')
pavani.display()
print(pavani.username)
print(pavani.getpassword())
print(pavani.accesspost)

pavani.username = 'sai'
pavani.setpassword("sai@123")
pavani.accesspost = "sunrise.png"
pavani.accesspost = "beach.png"
pavani.accesspost = "forest.png"