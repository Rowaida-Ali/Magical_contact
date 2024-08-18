class Magical_content:
    def __init__(self,name,email,phone_number):
        self.__name=name
        self.__email=email
        self.__phone_number=phone_number
    def get_name(self):
        return self.__name    
    def get_email(self):
        return self.__email
    def get_phone(self):
        return self.__phone_number 
    def describe(self):
        return self.__name,self.__email,self.__phone_number
content1=Magical_content("Harry","harry_123@gmail.com",44012345)  
update1=input("update your email") 
update2=int(input("update your phone number ")) 
content1.__email=update1
content1.__phone_number=update2
print(content1.describe()) 
print(f"Email after being updated : { content1.__email} ") 
print(f"Phone number after being updated: { content1.__phone_number} ") 

class WizardorWitch(Magical_content):
    def __init__(self,name,email,phone_number,wand,house):
        super().__init__(name,email,phone_number)
        self.wand=wand
        self.house=house
        self.wand={
                "core":"phornix feather",
                "wood":"holly",
                "length":11
            }    
        h=input("enter house name ")
        if h=="Gryffindor" .lower() or h=="Hufflepuff".lower() or h=="Ravenclaw".lower() or h=="Slytherin" .lower():
            self.house=h
        else:
            print("error")    
    def get_wand(self):
        return self.wand  
    def get_house(self):
        return self.house  
    def describe(self):
        return self.wand ,self.house         
wand1=WizardorWitch(wand="wand",house="house",name="harry",email="harry_123@gmail.com",phone_number=44012345) 
print(wand1.describe())


class MagicalCreature(Magical_content):
    def __init__(self,name,email,phone_number,speices,is_tame):
        super().__init__(name,email,phone_number)
        self.__speices=speices
        self.__is_tame=is_tame
    def get_speices(self):
        return self.__speices
    def get_tame(self):
        return self.__is_tame
    def describe(self):
        return self.__is_tame , self.__speices   
creature=MagicalCreature(speices="Hippogriff",is_tame=True,name="harry",email="harry_123@gmail.com",phone_number=44012345)
print(creature.describe())        
name=input("")
class Magicalcontentbook:
    def __init__(self):
       self.contacts=[]
    def add(self,contact):
        self.contacts.append(contact)
    def search(self,name):
        for content in self.contacts:
            if content1.get_name() ==name:
              print(content.describe())
            else:
              print("not found") 
contact=Magicalcontentbook()  
contact1=Magical_content("Harry","harry_123@gmail.com",44012345)
contact.add(content1) 
contact.search(name)




