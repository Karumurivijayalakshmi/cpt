#classmethod:not the instances,class bound
'''class class(1st arg)
@classmethod'''

'''class student:
    def __init__(s, name,marks):
        s.name=name
        s.marks=marks
    def display(self):
        print(f"Student name:{s.name}")
        print(f"Student marks:{s.marks}")
name=str(input("Enter the name:"))
marks=int(input("Enter the marks:"))
s=student(name,marks)
s.display()'''

'''class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod
    def input(cls):
        name=str(input("Enter the name:"))
        marks=int(input("Enter the marks:"))
        return cls (name,marks)
    def display(self):
        print(f"Student name:{self.name}")
        print(f"Student marks:{self.marks}")
s= student.input()
s.display()'''


'''code to illustrate a product with its price by normal istances 
  and claculate the products tax rate by 10% in a class method and print
  the total amount to be paid....'''


'''class product:
    tax_rate=0.18
    def __int__(self,name,price):
        self.name=name
        self.price=price
    def finalprice(self):
        total=self.price *(1+product.tax_rate)
        print(f"Final price of {self.name} is Rs.{total:.2f}")
    @classmethod
    def settax(cls,rate):
        cls.tax_rate=rate/100
name=str(input("Enter the product name:"))
price=float(input("Enter the base price:"))
rate=int(input("Enter tax_rate in %:"))
product.settax(rate)
item=product(name,price)
item.finalprice()'''

'''class Product:
    tax_rate = 0.18

    def __init__(self, name, price):  # Fixed constructor name
        self.name = name
        self.price = price

    def finalprice(self):
        total = self.price * (1 + Product.tax_rate)
        print(f"Final price of {self.name} is Rs.{total:.2f}")

    @classmethod
    def settax(cls, rate):
        cls.tax_rate = rate / 100


# Taking user input
name = input("Enter the product name: ")
price = float(input("Enter the base price: "))
rate = int(input("Enter tax_rate in %: "))

# Setting tax rate and creating object
Product.settax(rate)
item = Product(name, price)
item.finalprice()'''


'''basic math operations using @classmethod'''

'''class calculator:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    @classmethod
    def input(cls):
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        return cls(a,b)
    def add(self):
        return self.a+self.b
c=calculator.input()
print("Addition result:",c.add())'''


'''class calculator:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    @classmethod
    def input(cls):
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        return cls(a,b)
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
c=calculator.input()
print("Subtract result:",c.sub())
print("Addition result:",c.add())
print("Multiplies result:",c.mul())'''


#static method @staticmethod

'''class Student:
    gender='Female'
    def __inti__(s,name):
        s.name=name
    def dispaly(s):
        print(f"name:{s.name}")
    @classmethod
    def getname(cls):
        return cls.gender
    
    @staticmethod
    def resident(type_of_resident):
        if type_of_resident.lower()=='Indian':
            return "the person is Indian"
        else:
            return "non_resident Indian"
        
name=input("Enter your name:")
s=Student(name)
s.display()
print("Student gender:",Student.getname())'''


'''class Student:
    gender = 'Female'

    def __init__(s, name):  # Fixed constructor name
        s.name = name

    def display(s):  # Fixed spelling of method
        print(f"name: {s.name}")

    @classmethod
    def getname(cls):
        return cls.gender

    @staticmethod
    def resident(type_of_resident):
        if type_of_resident.lower() == 'indian':
            return "The person is Indian"
        else:
            return "Non-resident Indian"


# User input
name = input("Enter your name: ")
type=input("Enter resident or Non-resident:")
s = Student(name)
s.display()
print("Student gender:", Student.getname())
print(s.resident(type))'''


'''class op:
    @staticmethod
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
x=int(input("Enter a value:"))
y=int(input("Enter a value:"))
print("sum:",op.add(x,y))
print("subtract:",op.sub(x,y))
print("multiplicate:",op.mul(x,y))
print("division:",op.div(x,y))'''


'''class op:
    @staticmethod
    def operate(a,b):
        print("Add:",a+b)
        print("Sub:", a-b)
x=int(input("Enter a value:"))
y=int(input("Enter a value:"))
op.operate(x,y)'''


class calc:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def add(s):
        return s.a+s.b
    @classmethod
    def input(cls):
        a=int(input("Enter number:"))
        b=int(input("Enter number"))
        return cls(a,b)
    @staticmethod
    def mul(x,y):
        return x*y
c=calc.input()
print("Addition-instance",c.add())
x=int(input("Enter number for mul:"))
y=int(input("Enter another number:"))
print("Mul-static",c.mul(x,y))

