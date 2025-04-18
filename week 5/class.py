class Phone:
    def __init__ (self, brand, price):
        self.brand = brand
        self.price = price

phone1 = Phone("Samsung",20000) 
phone2 = Phone("Apple",45000) 

print(phone1.brand)
print(phone2.price)

class Ipad(Phone):
     pass
ipad= Ipad("Samsung",55000)
print (ipad.brand)
print (ipad.price)



