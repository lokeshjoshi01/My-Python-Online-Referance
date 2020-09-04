"""
this is only for my online referance please don't read.
"""
"""
Founder- guido van rossum
when - december 1989 in netherland
"""
#VARIABES
"""
word - string
number - intiger
decimal - float
"""
# print(type(fliename))

#LIST
"""
number.short - small to big
number.reverce - reverce of list
number.append - join new word in end
number.remove - remove word
number.pop - last value remover
number.insert - insert values
"""

# list = ["lokesh" , "lj" , "joshi" , "joshi"]
# print(list)

"""
for value change
a=temp
b=2
b=temp
print(a,b)
"""

#SETS

# s_form_list = set([1,2,3,4])
# print(s_form_list)

#IF AND ELSE
"""
if
elif
else
"""

# FOR LOOP AND WHILE LOOP
"""
for loop = for item in list
while = while(true)
"""

#BRAKE AND COONTINUE
"""
IF CONDITION WAS NOT STOP THAN USE IN BREAK
ELSE
CONTINUE
"""

# OPERATERS

"""
ARITHMETIC - +*-/ ETC
ASSIGMENT - == =+ =- ETC
COMPERISIOB - I=5 PRINT(I<=5)
LOGIC OPERATORS
MEMBERSHIP OPERATORS
IDENTITY OPERATORS
BITWISE OPERATORS
"""


# SHORT HAND IF-ELSE NOTATION

"""
a = int(input())
b = int(input())

print("you win") if a>b else print("you lose")
"""

#FUNCTION AND DOCSTRING

"""
def function1():
    print("you are looser")
 function1()
 """

#PRINT(FUNCTION2.__DOC__)

#TRY EXCEPT EXCEPTION
"""
print("enter the number")
n1 = input()
print("enter the number")
n2 = input()

try:
    print("add two numbers", int(n1) + int(n2))

except Exception as e:
    print(e)

print("you code succesfully done")
"""

#FOR READ FILE
"""
f = open("lokesh1.txt")
content = f.read()
print(content)
"""
#LINE BY LINE READ
"""
for line in f:
    print(line, end="")
print(f.readline())
f.close()
"""

#APPEND TO BHIND JOINT
"""
f = open("joshi.txt","a")
f.write("i am back")
 f.close()
"""
#READ AND WRITE BOTH
"""
f = open("joshi.txt", "r+")
print(f.read())
f.write("boss")
f.close()
"""
#TELL() AND SEEK()
"""
f = open("joshi.txt")
print(f.tell())

print(f.readline())
f.seek(0)
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())

f.close()
"""

#USING BLOCK TO OPEN FILE
"""
with open("joshi.txt") as f:
    a =f.read()
    print(a)
"""

# GLOBAL AND LOCAL VARIABLE
"""
l =10 #global

def fun1():
     #local
    m=1
    global l
    l = l+10
    print(l,m)
print("i was printed")
fun1()
"""


#LAMBDA OR ONE LINER FUNCTION OR ANOYNOMOS FUNCTION
"""
def add(a,b):
    return a-b
minus = lambda a,b : a - b
print(minus(6,2))
"""

#USING PYTHON EXTERNAL MODUAL AND BUILD IN MODUAL
"""
import random
# random_number = random.randint(0,1)
# print(random_number)
list = ["lokesh" , "lj" , "jl", "joshi"]
choice = random.choice(list)
print(choice)
"""

#F STRING AND STING FORMATING
"""
me = "lj"
a1 = 3
a = f"this is {me} {a1}"
print(a)
"""

#*ARGS OR **KWARGS
"""
def funargs (normal,*args):
    print(args[0])
list = ["lokesh" , "lj" , "jl", "joshi"]
normal = "lokesh joshi"
funargs(normal,*list)
"""

#TIME MODUAL
"""
import time
initial = time.time()

k=0
while (k<45):
    print("lokeshjoshi is programmer")
    k+=1
print("while loop ran in" , time.time()-initial, "second")

initial2 = time.time()
for l in range(45):
    print("lokeshjoshi is programmer")
print("for loop ran in" , time.time()-initial2, "second")
"""
# RECENT TIME FOR
"""
localtime = time.asctime(time.localtime(time.time))
"""
#ENUMERATE FUNCTION
"""
list = ["lokesh", "lj", "jl", "joshi"]
for index, item in enumerate(list):
    if index%2 == 0:
        print(f"lokesh please buy[list]")
"""

# if__name__==__main__
"""
iska use ek function ko dusre function me import krne k liye hota he
"""

# join
"""
list = ["lokesh" , "joshi", "lj"]
a = "and".join(list)
print(a,"other stars")
"""

# MAP , FILTER AND REDUCE
"""
MAP = EK FUNCTION JO PURI LIST ME APPLY KAR DEGA
FILTER = EK ASI LIST JO TRUE RETURN REGA
REDUCE = LIST ME EK DUSRE SE JODNE KA KAM KREGA
"""
# MAP
"""
num = ["1" , "2" , "3" , "4"]
num = list(map(int,num))

num[2] = num[2] + 1
print(num[2])
"""
# FILTER
"""
list1 = [1,2,3,4]
def is_greater_5(num):
    return num>5
gr_than_5 = list(filter(is_greater_5), list1)
print(gr_than_5)
"""

# REDUCE
"""
from functools import reduce

list1 = [1,2,3,4,5]
num = reduce(lambda x,y : x*y,list1)
print(num)
"""

# DECORATORS
# DECORATER KA USE JAB 1 HI JESA KAM 10 FUNCTION K SATH KRNA HO TAB DACORATOR KA USE HOTA HE
"""
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
        return nowexec()
def who_is_lj():
    print("lj is lj")
who_is_lj = dec1("lj is lj")
print(who_is_lj)
"""


# OBJECT ORIENTED PROGRAMMING
"""
CLASSES = TEMPLATE
OBJECT = INSTANCE
DRY = DO NOT REPEAT YOUR SELF"""

# CLASS
"""
class student:
    pass

lokesh = student()
joshi = student()

lokesh.name = "lokesh"
lokesh.std = 12
lokesh.section = 1
lokesh.subject = ["programmer" , "hacker" , "tech"]

print(lokesh.__dict__)
"""

# INSTANCE AND CLASS VARIABLES

"""
class employee:
    no_of_leaves = 8
    pass

lokesh = employee()
joshi = employee()

lokesh.name = "lokesh"
lokesh.salary = 448
lokesh.role = "programmer"

joshi.name = "joshi"
joshi.salary = 489
joshi.role = "hacker"

print(joshi.__dict__)
"""

# SELF AND__INT__()  (CONSTRUCTOR)
"""
class employee:
    no_of_leaves = 8
    pass

def __int__(self,name,salary,role):
    self.name = name
    self.salary =salary
    self.role = role

def print_details(self):
    return f"name is{self.name} , salary is {self.salary} , role is {self.role}"


lokesh = employee("lokesh", 255 , "programmer")
joshi = employee("joshi" , 254 , "hacker")

print(lokesh.print_details)
"""

# CLASS METHOD
# CLASS = JO CLASS ME HOTA HE USE CHANGE KR N K LIYE CLASS KA USE HOTA HE CLASS K UNDR CLASS

"""
def_change_leaves(cla):
            cls_no_of_leaves = newleaves
joshi_change_leaves(4)
"""


# CLASS METHOD AS ALTERNATIVE

"""
def from_str(cls , string):
            return cls(*str.split("-")
lj = employee("lj-255-hacker")
# - KI JGH PE / HO TO STRING KI JGH PE SLASH LIKHNA PDEGA
"""

# STATIC METHOD IN PYTHON

# VACHCHE KAY PRINT KRU HOU ANA MATE
"""
def printgood(str):
        print("this is good" + str)
print(lokesh.printgood("this")
"""

# ABSTRACTION AND ENCAPSULATION
"""
ABSTRACTION = TUKDE ME JODNA , EK EK KRKE
ENCAPSULATION = EMPLITATION KI DETAILS KO HIDE KRNA
"""

# SINGLE INHERITANCE IN PYTHON

# CLASS K UNDER CLASS
"""
class employee:
    no_of_leaves = 8
    pass

def __int__(self,name,salary,role):
    self.name = name
    self.salary =salary
    self.role = role

def print_details(self):
    return f"name is{self.name} , salary is {self.salary} , role is {self.role}"

class programmer(employee):

    def __int__(self, name, salary, role , language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language

    def print_details(self):
        return f"name is{self.name} , salary is {self.salary} , role is {self.role} , language is {self.language}"
lokesh = programmer("lokesh", 255 , "programmer" , [c,cppc,python])
print(lokesh.printprogeammer(self))
"""

# MULTIPLE INHERITANCE
"""
2 CLASS HO AUR TISRE CLASS KO ADD KRE YA TO 2 SE JYADA ADD KRE TO USE MULTIPLE INHERITANCE KHTE HE
NEW CLASS ME KUCH BHI NYA ADD KAR SKTE HE
UPER K SAB CLASS KO BHI ADD KR SKTE HE
CODE SAME TO SAME UPER JESA HI BAS USME NEW CLASS KO ADD KRNA HE
"""

# MULTITIME INHERITANCE
"""
CLASS 1 K GUN CLASS 2 ME HO AUR CLASS 2 K GUN CLASS 3 HO TO USE MULTITIME INHERITANCE KHTE HE
"""
"""
class dad:
    basketball = 3
class son(dad):
    dance = 1
    basketball = 9
    def is_dance(self):
        return f"yes i can king of {self.dance} of times"
class grandson(son):
    dance = 6
    guiter = 1
    def is_dance(selfself):
        return f"yes i can king of {self.dance} of times"
lj = dad()
jl = son()
lokesh = grandson()

print(lokesh.is_dance)
"""

# PUBLIC , PRIVATE AND PROTECTED ACCESS SPECIFIERS
"""
PUBLIC = SAB ACCESS KR SKTE HE
PROTECTED = HMARE PROGRAMM M KHI BHI USE KR SKTE HE DUSRE PROGRAMME KHI BHI USE NHI KR SKTE 
PRIVATE = HMARE ALAVA KOY USE NHI KR SKE GA
PRIVATE KO USE KRNE K LIYE __CLASSNAME__PRIVATE
ISKO NAMEMANGLING BHI KHTE HE"""

# POLYMORPHISM IN PYTHON
"""
ABILITY TO TAKE VARIOUS FORM
2 SAME PROGRAMME KO ALG ALG TRH SE PRINT KREGA"""

# SUPER() AND OVERRIDING IN CLASS
"""
PHELE B ME DUNDHEGA INSTANCE VARIABLE KO USME NA MILE TO A ME JAYEGA AUR PRINT KREGA
INSRANCE VARIABLE MEANS __INIT__(SELF)

EK BAR B ME SE MIL JAYE TO A KO AVERRIDING KREGA JISSE A CODE KAM NHI KREGA

A K CODE KO START KRNA HE TO SUPER() KA USE HOGA 
SUPER()__INIT__() ISSE OVERRIDING CODE BHI RUN HOGA
"""
# DIAMOND SHAPE PROBLEM IN MULTIPLE INHERITANCE

# A == B_AND_C === d

"""
class a:
    def met(self):
    print("this is a")

class b(a):
    def met(self):
    print("this is b")

class c(a):
    def met(self):
    print("this is c")

class d(b,c):
   pass

a=A()
b=B()
c=C()
d=D()

d.met()
"""

# OPERATERS OVERLOADING AND DUNDER METHOD

"""
__ SE START HOTA HE AUR __ SE CLOSE HOTA HE USE BUNDER KHTE HE

OPERATOR OVERLODING K FUNCTION MAPPING OPRETORS ME DEKHNA

DENDER METHOD KA USE MOST OFF OPERATORS KO OVERLODING KRNE ME HOTA HE
"""

# ABSTRACT BASE CLASS AND @ABSTRACTMETHOD

"""
ABCmeta m inheritance function me merhods ko impliment krni hi padti he

form abc import ABCMeta abstactmethod

class shape(ABCMeta):
            @abstractmethod
                def printarea(self):
                return 0 
class rectangle(shape):
                type = "rectangle"
                side = 4
                
                def__init__(self):
                         self.lenth = 6
                         self.breadth = 7
                         
                def printarea(self):
                            return self.lenth * self.breadth
                            
rect1 = ractangle
print(rect1.printarea())

"""

# SETTERS AND PROPERTY DECORATERS

"""
SETTER KA USE KOY BHI TOPIC KO CHANGE KRKE PRINT KRNE K LIYE HOTA HE

SETTER FUNCTION EK BAR LIKHNA PDTA HE

@enail.setter:
        def email(self):
                return f"{self.fname} , {self.lname} .codewithlj"
                
noram function ho tab property decorater ka use hota he

property decorater ka use class method ko change krne k liye hota he

"""


# OBJECT INTROSPECTION

"""
OBJECT KI INFORMATION K LIYE OBJECT INTROSPECTION KA USE HOTA HE JESE KI WO KIS CLASS KA HE TYPE KONSA HE ETC

EXAMPLES

print(type(skillf))
# iska use type dekhne k liye hota he

print(id(skillf))
# id kisi bhi function ki id dekhne k liye hota he 
# ye sbko uniqe id deta he

print(dir(skillf))
# iska use most off jab sab deatils print krvani ho tab hota but ye boht function ko print nhi krta


import inspect
print(inspect.getmembers(skillf)
# ye sab print kr dega jo dir nhi kr skta wobhi kr dega
"""

# GeneratorS

"""
ITERABLE == __ITER__() OR __GETITEM__
ITRATOR == __NEXT__()
ITREATION == ITERET KR N KI KRIYA KO ITREATION KHTE HE

GENERATORS = ITRETOR
JAB PROGRAMM BDA HOTA TAB PC KI RAN KAM PADTI HE TAB BDE PROGRAMM KO STEP BY STEP PRINT KRVANA HO TAB GENERATORS KA USE HOTA HE

def gen(n):
    for i in range(n)
    yield i

g = gen(3)
print(g.__next__())

#STRING EK ITERABLE HOTA HE
"""

# PYTHON COMPREHENSION

"""COMPREHENSIONS MEANS ONE LINER FUNCTION

1-LIST COMPREHENSION
ls = [i for in range(100) if i%3==0]
print(ls)

2-DICT COMPREHENSION
dic1 = {i:f"item{i}" for i in range(1000)
print(dict1)

value n interchange krva
sic1 = {value:keyfor key , value in dict1.item()}

3-SET COMPREHENSION
dresses = {dress for in ["dress1" , "dress2 , "dress1" ,"dress2"]}
print(dresses)

4-GENERATOR COMPREHENSION
even = (i for i in range(100) if i%2==0)
print(even.__next__())
#ek-ek krke print krega

full value print krni he to
for item in even():
        print(i)
"""

# USING ELSE WITH FOR LOOPS

"""
AGR LIST END HOTI HO YA LIST HE WO LIMITED HO TAB ELSE K SATH FOR LOOP KA USE KR SKTE HE


khana = ["roti","chawal","sabji"

for item in khana:
        print(item)
else:
    print("your item is good")
    
# yese bhi use kr skte  isme if bhi aata he
for item in khana:
            if item=="rplroti"
            break
else:
    print("ye list me nhi he")
"""

# FUNCTION CACHING IN PYTHON

"""
EK FUNCTION JAB TIME LETA H AUR WO DUSRI BAR USE HO AUR TIME NO LE TB USKO CACHING FUNCTION KA US HOTA HE

import time
from functools import lru_chche

@lru_cache(maximum=3)
def some_work(n):
            #some task talking n sec
            time.sleep(n)
            return n 

if__name__=='__main__':
        print("now running some work")
        some_work(3)
        print("please go again")
        some_work(3)
        print("go again")
"""
# TRY , EXCEPT , ELSE AND FINALLY IN PYHTON
"""
FINALLY KA USE CODE KO CLEANUP KRNE K LIYE HOTA HE
TRY EXPEXT HO YA NA HO FINALLY PRINT HOGA

f1 = open("does.txt")

try:
    f = open("lj.txt")
except Exception as e:
                print(e)
finally:
    print("run this any way")
    fl.close()
print("important stuff")

except k bad me else hoga to agr except run hoga to else nhi hoga aur else hoga to except nhi hoga
"""


# COROUTINES IN PYTHON

"""
MULTI TASK PROGRAMM KO 1-2 DELAY K BAD EASLIY RUN KREGA

def searcher():
            import time
            # some 4 sec time consuming
            book = "this is in")  #book badi hogi
            time.sleep(4)
            
            while true:
                    text = (yield) #value ko on the sky print krega
            if text in book:
                    print("your text in book"
            else:
                print("you are not in book")
                
search = searcher()
print("search , starting")
next(search)
search.send("lj")
input("press any key"
search.send("is in")

search.close() #close k bad kuch changes nhi honge

"""

# OS MODUAL
"""
import os

print(dir(os)) #os ki sab deatils milti he

print(os.getcwd()) #hum konse folder me he wo pta chlta he

print(os.chdir("c://") #location change krne k liye

print(os.listdir(c://") #drive m jitna h utna print krne k liye

print(mkdir("file name")) #new folder bnane k liye

os.remove("file name") #file ko remove krne k liye

# dusre google m se try krna

"""

# REQUEST MODULE FOR HTTP REQUEST
"""
ISKE USE WEBSITE YA FIR KISI BHI FILE KA SOURCE MULTA HE

import request

r=request.get("url")
print(r.text)
print(r.status_code) #iski help s status code milega

duska sab google me check kr lena
"""

# JASON MODULE
"""
JAVA SCRIPT OBJECT NOTESTION
DATA SEND TYPE
WEB PROTOCOL TYPE

json.loads = it is used to convert a json sting to a dictonary
json.dump = it is used to convert a dictonary to a json string
json.load = it is used to read a file which contains an json object
"""

# PICKLE MODULE

"""
import pickle  #iska use kisi bhi file ko pack krne k liye hota he

cars = ["audi" , "bmw", "tesla" , "suzuki"]
file = "filename.pkl"
fileobj = open(file , 'wb')
picke.dump(cars.fileobj)
fileobj.close()

# DEPICKLE KRNE K LIYE

file = "filename.pkl"
fileobj = opwn(file,'rb')
filename = pickle.load(fileobj)
print(filename)
"""
# REGULAR EXPRESSION RE MODUAL

"""
# SPECIFIES A SET OF SRINGS THAT MATCH IT

import re
my str = "file "
putt = re compiler(r'')

matches = patt.finditer(mystr)
for match in matches:
            print(match)
"""
"""
\A:         the resultant is a match if the input characters are at the beginning of the string
\b          the resultant is a match whether the input characters are at the beginning or the end of a word
\d          the resultant is a match if the string contains any digits
\s           the resultant is a match if the string contains a white space character


'.': Matches any single character except newline
'$': Anchors a match at the end of a string
' *': Matches zero or more repetitions
'+':Matches one or more repetitions
'{}':Matches an explicitly specified number of repetitions
'[]':Specifies a character class
'^' : start with

# baki he wo you tube se dekh lena
"""

# CONVERTING .PY TO .EXE
"""
pip install py installer

import pyinstall

my computer m jakar file khol kr powershell windows khole

pyinstaller file name

pyinstaller -- one file ek j file bnavi hoy to
"""

# RISE IN PYTHON
"""
a = input("what is your age")
is a.isnumeric()
        raise Exception ("number are not allowed")
# iske niche 1000 ya bdh code ho to use run hone time lgta he tb by chnce start me hi errror ho to time waste hoga tb start me eerror he ki nhi chake krne k lite iska use hota he start me error hoga ti a didha dega
"""

# PYTHON 'IS' VS '==' WHAT IS DEFFERNCE
"""
== = VALUE EQUALITY - TWO OBJECT REFERANCE
IS = REVERENCE EQUALITY - TWO REFERENCE SAME

== - ALG HO SKTE HE BUT USKO == KRK SAME KIYA JA SKTA HE
IS - IS ME JAB TWO VALUE SAME HO TO HI USE HOTA HE
"""

# CREATING A COMMAND LINE UTILITY IN PYTHON
"""
# A COMMAND LINE PROGRAM IS PROGRAM THAT OPERATERS FROM THE COMMAND LINE OR FROM A SHELL

import argparse
import sys

def calc(args):
        is args.0 = 'add'
        return.args.x = args.y
        
if __name__ == __'main'__:
            parser = argparse.Argumentparser()
            oarser.addargument('--x', type-float, defoult = 1.0 , help='contect harry bhai')
            oarser.addargument('--y', type-float, defoult = 2.0 , help='contect harry bhai')
            
args = parser.parse_args()
sys.stdout.write(str(calc(args)))

# A DIRECT POWERSHELL M KHULEHA
"""

# CREATING A PYTHON PACKAGE USING STEPUPTOOL

"""
MAKE FOLDER

MAKE FOLDER

SETUP.PY

README.TXT

LIANSCE.TXT

DUSRE FOLDER M POWER KHOLVU

ISKE ANDAR __INT__.PY

BAD ME VS CODE KHOLNA

"""
"""
from setuptools import setup

setup(name="filenname"
      verrsion=2.0",
      description = "write discription",
      long description = "write description",
      pakage = ("pakage name"),
      install_required = ()

terminal m
python stepup.py = sdist bdist.wheel
# wheel ko install kr lena

# APNA PAKAGE READY
"""


