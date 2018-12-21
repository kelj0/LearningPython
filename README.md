# Python references
---

### Table of contents

### Setting up
-	[Install](#install)
-	[Development Enviroment](#development-enviroment)
-	[Versions](#python3-or-2)
### Basics

-    [Basic syntax](#basic-syntax)
-    [Data types](#Data-Types)

### Usefull stuff
-    [Random](#Random)
-    [Time](#Time)
-    [Multithreading](#Multithreading)
-    [Regex](#Regex)
-    [Launching Programs](#Launching_Programs)
-    [Useful data](#Useful-data)
-    [OOP](#Object-Oriented-programming)
-    [Working with JSON](#JSON)
### Working with files
-    [Bat](#Bat)
-    [Working with files](#Working-with-files)
-    [ZIP FILES](#ZIP-FILES)
-    [Excel](#Excel)
-    [Shutil](#Shutil)
-    [Manipulating Images](#Manipulating_Images)

### Working online
-    [Web Scraping](#Web-Scraping)
-    [Sending email and Text messages](#Sending_email_and_Text_messages)

### DEBUGGING
```
If you want to get input in debugger 
>go in launch.json file (ctrl+shitf+D)
>in first part add python path to pythonPath
>below add "console":"externalTerminal" (dont forget to put ',' after line)
```
-    [Assertions](#Assertions)
-    [Logging](#Logging)


### Controling GUI
-    [Controling Mouse Keyboard with GUI Automation](#Controling_Mouse&Keyboard_with_GUI_Automation)

### Random libs
-    [Turtle module](#Turtle_module)
-    [Pygame](#Pygame)


---

## Install <a name="install"></a>
```
Probably already have it installed. If you are windows user gl :)

Exception
[Python is not installed by default in any of the BSDs, unless you count OS X. 
You may well find that it is available on a BSD system because it was added 
after the system was installed. If not, it is available through the default 
package system in all cases](https://unix.stackexchange.com/a/24808)

Check it with 
$ python --version
```

## Development Enviroment <a name="development-enviroment"></a>

### Text Editors

#### Vim
```
Vim is a text editor which uses keyboard shortcuts for editing 
instead of menus or icons. There are a couple of plugins and 
settings for the Vim editor to aid Python development. If you only 
develop in Python, a good start is to set the default settings 
for indentation and line-wrapping to values compliant with PEP 8. 
In your home directory, open a file called .vimrc and add the following lines:

---------------------------------------------------------------------------
set textwidth=79  " lines longer than 79 columns will be broken
set shiftwidth=4  " operation >> indents 4 columns; << unindents 4 columns
set tabstop=4     " a hard TAB displays as 4 columns
set expandtab     " insert spaces when hitting TABs
set softtabstop=4 " insert/delete 4 spaces when hitting a TAB/BACKSPACE
set shiftround    " round indent to multiple of 'shiftwidth'
set autoindent    " align the new line indent with the previous line
---------------------------------------------------------------------------

Also SuperTab (https://www.vim.org/scripts/script.php?script_id=1643) 
is small Vim plugin that makes code completion more convenient 
by using <Tab> key or any other customized keys
```

#### Emacs
```
Emacs is another powerful text editor. It is fully programmable (Lisp), 
but it can be some work to wire up correctly. A good start if you’re 
already an Emacs user is Python Programming in Emacs at EmacsWiki
(https://www.emacswiki.org/emacs/PythonProgrammingInEmacs)
```

#### Sublime Text
```
Sublime Text is a sophisticated text editor for code, markup, and prose. 
You’ll love the slick user interface, extraordinary features, 
and amazing performance.
```


### IDEs

#### PyCharm/IntelliJ IDEA
```
PyCharm is developed by JetBrains, also known for IntelliJ IDEA. Both share 
the same code base and most of PyCharm’s features can be brought to IntelliJ 
with the free Python Plug-In(https://plugins.jetbrains.com/plugin/631-python)
```

#### Visual Studio Code
```
Python for Visual Studio is an extension for the Visual Studio Code IDE. 
This is a free, lightweight, open source IDE, with support for Mac, Windows, and 
Linux. Built using open source technologies such as Node.js and Python, with 
compelling features such as Intellisense (autocompletion), local and remote 
debugging, linting, and the like.

https://code.visualstudio.com/
```

#### Enthought Canopy
```
Enthought Canopy is a Python IDE which is focused towards Scientists 
and Engineers as it provides pre installed libraries for data analysis.
https://www.enthought.com/product/canopy/
```

#### Spyder
```
Spyder is an IDE specifically geared toward working with scientific Python 
libraries (namely Scipy). It includes integration with pyflakes, pylint and rope.

Spyder is open source (free), offers code completion, syntax highlighting, 
a class and function browser, and object inspection.
https://github.com/spyder-ide/spyder
```

#### WingIDE
```
WingIDE is a Python specific IDE. It runs on Linux, Windows, and 
Mac (as an X11 application, which frustrates some Mac users).

WingIDE offers code completion, syntax highlighting, source browser, 
graphical debugger and support for version control systems.
https://wingware.com/
```

### Other Tools

#### IPython
```
IPython provides a rich toolkit to help you make the most out of using Python interactively. 
Its main components are:

    Powerful Python shells (terminal- and Qt-based)
    A web-based notebook with the same core features but support for rich media, text, code, 
		mathematical expressions and inline plots
    Support for interactive data visualization and use of GUI toolkits
    Flexible, embeddable interpreters to load into your own projects
    Tools for high level and interactive parallel computing

$ pip install ipython

To download and install IPython with all its optional dependencies for the 
notebook, qtconsole, tests, and other functionalities:

$ pip install ipython[all]
```

#### BPython
```
bpython is an alternative interface to the Python interpreter for Unix-like operating systems. 

It has the following features:
    In-line syntax highlighting
    Readline-like autocomplete with suggestions displayed as you type
    Expected parameter list for any Python function
    “Rewind” function to pop the last line of code from memory and re-evaluate
    Send entered code off to a pastebin
    Save entered code to a file
    Auto-indentation
    Python 3 support

$ pip install bpython
```

#### ptpython
```
ptpython is a REPL build on top of the prompt_toolkit library. It is considered to 
be an alternative to BPython. 

Features include:
    Syntax highlighting
    Autocompletion
    Multiline editing
    Emacs and Vim Modes
    Embedding REPL inside of your code
    Syntax validation
    Tab pages
    Support for integrating with IPython’s shell, by installing IPython 
	(pip install ipython) and running ptipython.

$ pip install ptpython
```

## Versions <a name="python3-or-2"></a>

The basic gist of the state of things is as follows:
* Most production applications today use Python 2.7.
* Python 3 is ready for the production deployment of applications today.
* Python 2.7 will only receive necessary security updates [until 2020](https://www.python.org/dev/peps/pep-0373/#id2)
* The brand name “Python” encapsulates both Python 3 and Python 2.
 
```
Recommendations (based on Hitchhiker's Guide to Python!)

- Use Python 3 for new Python applications.
- If you’re learning Python for the first time, familiarizing yourself with 
   Python 2.7 will be very useful, but not more useful than learning Python 3.
- Learn both. They are both “Python”.
- Software that is already built often depends on Python 2.7.
- If you are writing a new open source Python library, it’s best to write 
   it for both Python 2 and 3 simultaneously. Only supporting Python 3 for a new 
   library you want to be widely adopted is a political statement and will alienate 
   many of your users. This is not a problem — slowly, over the next three years, 
   this will become less the case.
```

### Implementations
```
When people speak of Python they often mean not just the language but 
also the CPython implementation. Python is actually a specification for 
a language that can be implemented in many different ways.
```

#### CPython
```
CPython is the reference implementation of Python, written in C. It compiles Python 
code to intermediate bytecode which is then interpreted by a virtual machine. 
CPython provides the highest level of compatibility with Python packages and C 
extension modules.
```

#### PyPy
```
PyPy is a Python interpreter implemented in a restricted statically-typed 
subset of the Python language called RPython. The interpreter features a 
just-in-time compiler and supports multiple back-ends (C, CLI, JVM).
```

#### Jython
```
Jython is a Python implementation that compiles Python code to Java bytecode 
which is then executed by the JVM (Java Virtual Machine). Additionally, it 
is able to import and use any Java class like a Python module.
```

#### IronPython
```
IronPython is an implementation of Python for the .NET framework. It can use 
both Python and .NET framework libraries, and can also expose Python code to 
other languages in the .NET framework.
```

#### PythonNet
```
Python for .NET is a package which provides near seamless integration of a 
natively installed Python installation with the .NET Common Language Runtime 
(CLR). This is the inverse approach to that taken by IronPython (see above), 
to which it is more complementary than competing with.
```

---

## Basic syntax <a name="basic-syntax"></a>
```py
# Printing text
print("Print text")
>>Print text
# Important note * print default uses \n after calling so if im using for loop it will look like this
>>for i in range(3):
      print(i)
0
1
2
# To put all parametars in same line ( remove default for print)
>>for i in range(3):
      print(i, end=" ")
0 1 2
#IMPORTANT NOTE IF YOU ARE USING PY 2.6+ (untill py3)
# you need to import print function like this
from __future__ import print_function
#This will allow you to use end in print while using python that is 2.6-py3 :)

# Using type we can see what type is something in py
>>type("Hello world")
<class 'str'>
>>type(19)
<class 'int'>

#---------------------------------------------------------------------
# Strings
#---------------------------------------------------------------------
# If using this type of quotes -> ' then we can use this type -> " inside and vice versa
# if you use triple quoted(''' or """) string you can store multiple lines and " , ' inside

a = 'Test"test"'
>>print(a)
Test"test"

>> b = "Test'test'"
>>print(b)
Test'test'

c = """ This is a multi
        line 'string'
        named "c". """
>> print(c)
This is a multi
line 'string'
named "c".
#---------------------------------------------------------------------
#If
if True:    # This is always True, so this is always executed,
    pass    # But it does nothing cause we put pass in body (pass is placeholder)
else:
    pass

if x<0:
    print("The negative number ", x ," is not valid here!")
    x = 4
    print("I've decided t ouse the number 4 instead")
print("The square root of ", x , "is", math.sqrt(x)) # Note this will give error if we dont import math
# Above code checks if its negative and changes it to 4 if it is < 0

# We can also type something like this 
if x is 10:  # 'is' can be used as ==
    print("X has value of 10")
    

value = 2
if value % 2 == 0:
    print("even")
else:
    print("odd")
# or you can do something like this
value = 2 
print("even") if value % 2 == 0 else "odd"

#---------------------------------------------------------------------
#While
while True:
    s=input("Enter string")
    if s=='quit':
      break
    else:
      print(s)
#---------------------------------------------------------------------
#For
for i in range(0,5):
    print(i)
#prints from 0 to 4(if added 3rd number in brackets(0,5,X) prints every i+X)

something = ["k","a","r","l","o"]
for letter in something:
    print(letter,end=" ")
> k a r l o

#---------------------------------------------------------------------
# try except
#---------------------------------------------------------------------

# Simple trying to open a file 

try:
    f = open("myfile.txt")
    f.close()
except:
    print("Cant open file!")
    
    
# We can use multiple exceptions
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# To see how exceptions actualy work lets make ours
try:
    age = int(input("Please enter your age:")
    if age <0:
        my_error = ValueError("something is fishy with entered age".format(age))
        raise my_error
except ValueError as v:
    print(type(v))
    print(v)

>> <class 'ValueError'>
>> something is fishy with entered age

# finaly
import turtle,time
try:
    win = turtle.Screen()
    tess = turtle.Turtle()
    # Important line below
    n = int(input("How many sides do you want in your polygon?")
    angle = 360/n
    for i in range(n):
        tess.forward(10)
        tess.left(angle)
    time.sleep(3)       # Make program wait a few seconds
finaly:
    win.bye()           # Close the turtle's window
# What if we enteret 's' in input ? we cant cast 's' to int so we would get exception raised, what finaly does
# It secures execution of that code regarding raised exception and then it crashes and shows exception
# So we would actualy close window before our program crashes and pops out exception


#---------------------------------------------------------------------
# Functions
#---------------------------------------------------------------------

# Basics

def f(x):
      return x*2

>> f(1)
2
>>f('a')
'aa'
>> a = 'a'
>> f(a)
'aa'
 
def f1(x,y):
      return x,y # This returns tuple
def f2(x,y):
      return [x,y]  # This returns list
>> f1(1,2)
(1,2)
>> f2(1,2)
[1,2]
>> a,b = f1(1,2)
>> print("a: %d, b: %d " % (a,b))
a: 1, b: 2

#---------------------------------
# Argument matching syntax
#------------------------------------------------------------------------------------------------------
#       /Syntax/          |/Location/|            /Interpretation/                                      
#------------------------------------------------------------------------------------------------------
# f(value)                |  Caller  | Normal argument : matched by position                          
#------------------------------------------------------------------------------------------------------
# f(name=value)           |  Caller  | Keyword argument: matched by name                              
#------------------------------------------------------------------------------------------------------
# func(*iterable)         |  Caller  | Pass all objects in iterable as individual positional arguments 
#------------------------------------------------------------------------------------------------------
# func(**dict)            |  Caller  | Pass all key/value pairs in dict as individual keyword arguments
#------------------------------------------------------------------------------------------------------
# def func(name)          | Function | Normal argument: matches any passed value by position or name
#------------------------------------------------------------------------------------------------------
# def func(name=value)    | Function | Default argument value, if not passed in the call
#------------------------------------------------------------------------------------------------------
# def func(*name)         | Function | Matches and collects remaining positional arguments in a tuple
#------------------------------------------------------------------------------------------------------
# def func(**name)        | Function | Matches and collects remaining keyword arguments in a dictionary
#------------------------------------------------------------------------------------------------------
# def func(*other, name)  | Function | Arguments that must be passed by keyword only in calls (3.X)
#------------------------------------------------------------------------------------------------------
# def func(*, name=value) | Function | Arguments that must be passed by keyword only in calls (3.X)
#------------------------------------------------------------------------------------------------------

#------------------------------
# Keyword basics
def f(a,b,c):print(a,b,c)
>> f(a=1,b=2,c=3)
1,2,3
>> f(c=1,b=2,a=3)
3,2,1
>> f(1,b=4,c=10)
1,4,10
#------------------------------
# Defaults
def f(a, b=2, c=3):print(a,b,c)  # a is required , b and c optional
>> f(1,2,3)
1,2,3
>> f(10)
10,2,3
>> f(10,b=20)
10,20,3

#------------------------------
# Any number of arguments
def f(*args): print(args)
>> f()
()
>> f(1)
(1,)
>> f(1,2,3,4)
(1,2,3,4)

def f(**args): print(args)  #** words for keyword arguments- it collects them into a new dictionary
>> f()
{}
>> f(a=1, b=2)
{'a': 1, 'b': 2}

#------------------------------
# Unpacking arguments
def f(a,b,c,d): print(a,b,c,d)
>> args = (1,2)
>> args += (3,4)
>> f(*args)
1,2,3,4

args = {'a': 1,'b': 2,'c': 3}
args['d'] = 4
>> f(**args)
1,2,3,4
#------------------------------
# Keyword-Only arguments
def kwonly(a,*,b='ham',c='eggs'): print(a,b,c)
# 'a' may be passed by position or name but 'b' and 'c' MUST by keywords
>> kwonly(1)
1 ham eggs
>> kwonly(1, c=3)
1 ham 3
>> kwonly(a=1)
1 ham eggs
>> kwonly(c=3,b=2,a=1)
1 2 3
>> kwonly(1,2)
TypeError: kwonly() takes 1 positional argument but 2 were given
#------------------------------
# Immutable and mutable passed objects 
def changer(a, b):
      a = 2
      b[0] = 'spam'

>> X = 1
>> L = [1,2]
>> changer(X,L)  # Pass immutable and mutable object
>> X,L           # X is unchanged, L is different!
(1, ['spam', 2])

#------------------------------
# Avoiding mutable argument changes
L = [1,2]
changer(X,L[:])  # Pass a copy , so our 'L' does not change
# We can also copy within the function itself, if we never want to change passed-in objects
def changer(a,b):
      b = b[:]
      a = 2
      b[0] = 'spam' #Changes our copy list
  
#------------------------------
# Ordering rules
#------------------------------
def f(a, *b, **d, c=6): print(a, b, c, d)
SyntaxError: invalid syntax                  # Keyword-only before **!

def f(a, *b, c=6, **d): print(a, b, c, d)    # Collect args in header

>> f(1, 2, 3, x=4, y=5)
1 (2, 3) 6 {'y': 5, 'x': 4}                  # Default used

>> f(1, 2, 3, x=4, y=5, c=7)
1 (2, 3) 7 {'y': 5, 'x': 4}                  # Override default

>> f(1, 2, 3, c=7, x=4, y=5)
1 (2, 3) 7 {'y': 5, 'x': 4}                  # Anywhere in keywords
>> def f(a, c=6, *b, **d): print(a, b, c, d) # c is not keyword-only here!
>> f(1, 2, 3, x=4)
1 (3,) 2 {'x': 4}

def f(a, *b, c=6, **d): print(a, b, c, d) # KW-only between * and **
>> f(1, *(2, 3), **dict(x=4, y=5))
1 (2, 3) 6 {'y': 5, 'x': 4}               # Unpack args at call
>> f(1, *(2, 3), **dict(x=4, y=5), c=7)
SyntaxError: invalid syntax               # Keywords before **args!
>> f(1, *(2, 3), c=7, **dict(x=4, y=5))
1 (2, 3) 7 {'y': 5, 'x': 4}               # Override default
>> f(1, c=7, *(2, 3), **dict(x=4, y=5))
1 (2, 3) 7 {'y': 5, 'x': 4}               # After or before *
>> f(1, *(2, 3), **dict(x=4, y=5, c=7))
1 (2, 3) 7 {'y': 5, 'x': 4}               # Keyword-only in **


#------------------------------------------------------------
# Lets make 2 files -> function.py and test.py
def function():
    print('Hello from function!')
# Save it as function.py in same dir as test.py
# in test.py write following

from function import *
function() # Prints "Hello from funciton!"
# Read as from file function.py import all 
# This is usefull for making your code cleaner :)


#--------------------------------
# Docstrings
#--------------------------------
# First comment when making function , it will be displayed when we open-close parenthesis ()
# Its key feature for documentation as in it explains what function should do ..
def function():
        """This is displayed when we type function()"""

#---------------------------------
# Function annotations (python 3.X)
#---------------------------------

# Python 2.x has docstrings, which allow you to attach a metadata string to various 
# types of object. This is amazingly handy, so Python 3 extends the feature by allowing you to 
# attach metadata to functions describing their parameters #and return values.
# More info -> https://www.python.org/dev/peps/pep-3107/

def f(a: 'spam', b: (1, 10), c: float) -> int:
      return a + b + c
>> f(1,2,3)
6
>> f.__annotations__
{'c': <class 'float'>, 'b': (1, 10), 'a': 'spam', 'return': <class 'int'>}


#------------------------------
# Function that returns function
#------------------------------
def makeLine(a,b):
    def y(x):
        return x*5
    return y
    
a = makeLine(5,2)
a(1)
# returns 5

# This is called creating functions on the fly, this makes function that RETURNS function!
# You can now call a ,pass parametar and it will return parametar multiplyed by 5
# C,C++ and many other languages dont allow you to define function that retunrs function

#-----------------------------\
# Function Design Concept     |
#/----------------------------|----------------------------------\
#| - use arguments for inputs and return for outputs              |
#| - use global variables only when truly necessary               |
#| - don’t change mutable arguments unless the caller expects it  |
#| - each function should have a single, unified purpose          |
#| - each function should be relatively small                     |
#| - avoid changing variables in another module file directly     |
#\---------------------------------------------------------------/
```


## Data types<a name="Data-Types"></a>
```py
# Every object in Python is classified as either immutable or not.
# In terms of the core types "numbers", "strings" and "tuples", are immutable;"lists", "dictionaries", and sets are not 

#---------------------------------------------------------------------
# STRING
#---------------------------------------------------------------------
#CONVERTING LIST TO STRING
some_list=["k","a","r","l","o"]
names=''.join(some_list)

# default spaces in rjust ljust in second parametar 
'hello'.rjust(10,'*')
# Working with files

#prints '*****hello'
'hello'.ljust(10,'*')
#prints 'hello*****'
'hello'.center(10,'=')
#prints '==hello==='
#-------------------------------
#Checks
#-------------------------------
name = 'Swaroop'
if name.startswith('Swa'):
  print('Yes, the string starts with "Swa"')
'hello'.isalpha()   #returns True if the string consists only of letters and is not blank
'hello'.isalnum()   #returns True if the string consists only of letters and numbers and is not blank
'hello'.isdecimal() #returns True if the string consists only of numeric characters and is not blank
'hello'.isspace()   #returns True if the string consists only of spaces, tabs, and newlines and is not blank
'hello'.istitle()   #returns True that begin with an uppercase letter followed by only lowercase letters.

if 'a' in name:
    print('Yes , it contains "a"')
if name.find('war')!= -1:
    print('Yes it conaints the string "war"')
    
name = 'Swaroop'
>>name.replace('Swa','??')
'??roop'  # despite the names of these string methods, we are not changing
          # the original strings here,but creating new strings as the result

#-------------------------------
delimiter='_*_'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist))#prints mylist[0] delimiter then mylist[1] ..
#-------------------------------
fruit  = "banana"
list(enumerate(fruit))
[(0, ’b’), (1, ’a’), (2, ’n’), (3, ’a’), (4, ’n’), (5, ’a’)]

# Using format as alignment in print 
n1 = "test1"
n2= "test2
n3= "test3
print("|||{0:<8}|||{1:^9}|||{2:>8}|||{3}|||".format(n1,n2,n3,0000))
#>>|||test1   |||  test1  |||   test3|||0000|||

# String Formatting Method 
>> print('{} am {}'.format('I','Karlo'))
'I am Karlo'
>> print('{1} am {0}'.format('I','Karlo'))
'Karlo am I'

>> template = '%s, %s and %s'
>> template % ('spam', 'ham', 'eggs')
spam, ham and eggs

>> template = '%(motto)s, %(pork)s and %(functiond)s'
>> template % dict(motto='spam', pork='ham', functiond='eggs')
'spam, ham and eggs'

>> import sys
>> print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'computer'}))
My computer runs linux

>> somelist = list('SPAM')
>> print('first={0[0]}, third={0[2]}'.format(somelist))
first=S, third=A


#---------------------------------------------------------------------
# LIST
#---------------------------------------------------------------------
list=["item1","item2","item3"]
#printing it
print(list)
> [item1,item2,item3]

# Slicing and updating to list 
a_list = ['a', 'b', 'c', 'd', 'e', 'f']
a_list[1:3] = ["x","y"]
print(a_list)
>>[a, x, y, d, e, f]
# You can also add to list with empty slice
a_list = ['a','d','e']
a_list[1:1] = ['b','c']
print(a_list)
>[a,b,c,d,e]

# Making lists
a_list = [] #empty list
a_list = [1,2,3,4]
a_list = range(1,5) # type(a_list) <class 'range'> but you can still for i in range(a) to get 1 2 3 4 outputed
a_list = [i for i in range(1,5)] #one-liner "iterator", print(a_list) outputs [1,2,3,4]


# List deletion
a = [1,2,3]
del a[1] # You can also use slicing here ( a[0:2] would delete [1,2])
print(a)
>[1,3]

# Aliasing
a = [1,2,3]
b=a
a is b
> True
b[0]=5
print(a)
>[5,2,3]

# Cloning lists
# Easyest way to clone lists is by slicing them
list1=[1,2,3]
list2=list1[:] # list2 is COPY of list1
# if you change list2 ,list1 will not change

# Printing lists
list = [1,2,3,4]
for number in list:
    print(number,end=' ')
>> 1 2 3 4

# Print list but skip first member
for number in list[1:]:
    print(number,end=' ')
>> 2 3 4

# Print last member of list
for number in list[-1:]:
    print(number,end=' ')
>> 4

# Print every second member of a list
for number in list[::2]:
    print(number,end=' ')
>> 1 3

# Print every second member of a list but start from second 
for number in list[1::2]:
    print(number,end=' ')
>> 2 4

# Print list backwards
for number in list[::-1]:
    print(number,end=' ')
>> 4 3 2 1

# Print list backwards but dont print first member
for number in list[:0:-1]:
    print(number,end=' ')
>> 4 3 2 


#---------------------------------------------------------------------
# TUPLES
#---------------------------------------------------------------------
#Same like list but without extensive funcionality  (they are immutable also)
tuple=("Car",1,0,5)
print(tuple)
>Car 1 0.5
# If you want to create tuple with 1 element
tup = (5,)   # You need to put comma after element, if you dont you will make int 
type(tup)
> <class 'tuple'>

# Tuple packing and unpacking 
b = ("Bob",19,"CS")
(name,age,studies) = b
name
>Bob
age
>19
studies
>CS


#---------------------------------------------------------------------
# DICTIONARY
#---------------------------------------------------------------------
# Creating
ab={
'Key1':'Item1',
'Key2':'Item2'
}
# or
ab = dict(Key1='Item1',Key2='Item2')
# or
ab = dict(zip(['Key1', 'Key2'] , ['Item1', 'Item2'])) # "Zipping"
# Note: left-to-right order of dictionary keys is scrambled. Mappings are not positionally ordered
# so unless you're lucky, they'll come back in different order than you typed them

# printing
>> print(ab['Key1'])
Item1
# or
>> ab.get("Key1")
Item1
>> test = ab.get("Key1")  # test == "Item1", if there is no key named "Key1" in dictionary test will be NoneType,
# You can pass second parametar to get
>> test = ab.get("Key999",0) 
# - now if there is no Key999 in dict , test == 0 

>> print(ab)
{'Key1':'Item1','Key2':'Item2'}

# delete item 
>> del ab['Key1']
>> print(ab)
{'Key2': 'Item2'}

ab = {"two": "dos", "one": "uno"}
>> for k,v in ab.items():
      print("Key {0} has value {1}".format(k,v))
Key two has value dos
Key one has value uno

# printing list element as in dict parametar valute()
names={"imena":["karlo","pero","duro"],"prezimena":["kegljo","peric","duric"]}
 for i in range(3):
      print("IME:",names['imena'][i])
      print("PREZIME:",names['prezimena'][i])

# Nested dictionary
dic={'nested':{'name':karlo,'year':1},'nestedList':[1,2,3]}

>> print(dic['nested']['name'])
'karlo'
>> print(dic['nested']['nestedList'][0])
'1'

# Counting letters in string
letters_counts = {} # empty dictionary
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get[letter,0] + 1  # get(key,return_value if no key in dict)/returns value
>> letter_counts
{’M’: 1, ’s’: 4, ’p’: 2, ’i’: 4}

# Dictionary-Based Formatting Expressions
>> '%(qty)d more %(functiond)s' % {'qty': 1, 'functiond': 'spam'}
'1 more spam'

>> reply = """
%(b)s u beton, planet stane
%(b)s u sunce, planet tame
"""
>> values = {'b': 'Besa'}
>>print(reply % values)
Besa u beton planet stane
Besa u sunce planet tame



#---------------------------------------------------------------------
# BYTEARRAY
#---------------------------------------------------------------------
# supports in-place changes for text, but only for text whose characters are all at most 8-bits wide(e.g.,ASCII)
# available in Pythons 2.6, 3.0, and later

B = bytearray(b'spam')  # A bytes/list hybrid
B
>>bytearray(b'spam')    # 'b' needed in 3.X, not 2.X
B[0] = ord('d')         
>>B                     # chr(B[i]) also works -B[i] returns ASCII value
bytearray(b'dpam')
>>B.extend(b'e')       
>>B
bytearray(b'dpame')
>>B.decode()             # Translate to normal
'dpame'
>>new = B.decode()
>>type(new)
<class 'str'>

#---------------------------------------------------------------------
# SET
#---------------------------------------------------------------------
X = set('spam')      # Make a set out of a sequence in 2.X and 3.X
Y = {'h', 'a', 'm'}  # Make a set with set literals in 3.X and 2.7

>> X, Y   # A tuple of two sets without parentheses
({'m', 'a', 'p', 's'}, {'m', 'a', 'h'})

>> X & Y  # Intersection
{'m','a'}

>> X | Y  # Union
{'m','h', 'a', 'p', 's'}

>> X - Y  # Difference
{'p', 's'}

# Set comprehensions in 3.X and 2.7
>> { n ** 2 for n in [1,2,3,4]}
{16, 1, 4, 9}

#---------
# Filter out duplicates (possibly reordered!) 
test = [1,2,3,2,4]
test = list(set(test))

# Order-neutral equality tests
>> set("karlo") == set("rloka")
True
#--------

```

# Usefull stuff

## Random<a name="Random"></a>
```py
#---------------------------------------------------------------------
# If you need more info about pseudorandom https://en.wikipedia.org/wiki/Pseudorandomness
#---------------------------------------------------------------------
# Basics
#---------------------------------------------------------------------
import random
rng = random.Random()  # create a black box obj that generates random numbers
dice_throw = rng.randrange(1,7) # Return and int, one of 1,2,3,4,5,6
randomODD = rng.randrange(1,100,2) #random odd number from 1 to 98
 #---------------------------------------------------------------------
# You can also do random like this
randomNumber = random.randrange(1,10) # [1,10>  it means 1 is included and 10 is not
 
#---------------------------------------------------------------------
#Random elements in list
#---------------------------------------------------------------------
import random
a=[1,2,3]
random.shuffle(a)#Shuffles elements in list 
random.sample(a,2)#Takes random 2 elements in list 
# Note: it cant take same number member times and it returns members randomly so in this example
# if it returns 2 and 3 it can return [2,3] or [3,2]
#---------------------------------------------------------------------
# For testing
drng = random.Random(123) # This is seed , if you are debugging use something like this so you know
# What will happen and you can see if its same as last time regarding random(its same random like last time)


#---------------------------------------------------------------------
# Example how to generate a list containing n random ints between [min,max>
#---------------------------------------------------------------------
import random

def make_random_ints(num,lower_bound,upper_bound):
    rng = random.Random()
    result = []
    for i in range (num):
        result.append(rng.randrange(lower_bound,upper_bound))
    return result

make_random_ints(4,1,10)  # make 4 random ints from 1 to 10(not including)
>[2,3,2,6]
# If you dont want duplicates returned use this (good for small lists!)
xs = list(range(1,13)) # make list [1,13>
rng = random.Random() #rng box
rng.shuffle(xs)
result = xs[:5] #first 4 elements

# For bigger lists , lets say ten milion items first algorithm is very bad , making 10mil items, shuffling,slicing..
# lets make better one

def make_random_ints_no_dups(num,lower_bound,upper_bound):
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound,upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result
    
xs = make_random_ints_no_dups(5,1,10000000)
print(xs)
[12312,421412,4123122,5214123,123124]
# Note: dont put bigger requests than you make list ( ect make_ran..(10,1,5))
# how can you take 10 elements from len(list)==5

```


## Regex<a name="Regex"></a>
```py
#---------------------------------------------------------------------
#Basics
#---------------------------------------------------------------------
import re
#\d stands for a digit character(0-9)

phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#makes search "term"
mo= phoneNumRegex.search('My number is 123-123-1234')#searches for "term" in string, and puts it* 
print('Phone number found: ' + mo.group())#mo.group() prints finded "term"             *in mo if it finds it
#you can also group items in phoneNumRegex-> phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#and then you can use mo.group(1) to print first group of phoneNumRegex(3digits) .group(0) prints all ,
# .groups() returns tuple of groups (3digits,3digs-4digs)
# you can add names to grouped parametars ( first,second = mo.groups()) first will be 3digs , 
# second will be 3digs-4digs
#---------------------------------------------------------------------

batRegex = re.compile(r'Bat(wo)?man')
mo1= batRegex.search('The adventures of Batman')
mo1.group()
# 'Batman'

mo2=batRegex.search('The adventure of Batwoman')
mo2.group()
# 'Batwoman'

batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
# 'Batwowowowoman'


batRegex = re.compile(r'Bat(wo)+man')
mo4 = batRegex.search('The Adventures of Batman')
mo4 == None
# True
#---------------------------------------------------------------------
#SHORTHAND CODES FOR COMMON CHARACTER CLASSES
#---------------------------------------------------------------------
# \d Any numeric digit from 0 to 9.
# \D Any character that is not a numeric digit from 0 to 9.
# \w Any letter, numeric digit, or the underscore character.(Think of this as matching “word” characters.)
# \W Any character that is not a letter, numeric digit, or the underscore character.
# \s Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S Any character that is not a space, tab, or newline.
#---------------------------------------------------------------------
#NEGATIVE CHAR CLASS
#---------------------------------------------------------------------
constantRegex = re.compile(r'[^aeiouAEIOU])
constantRegex.findall("Robocop eats baby food.Babyfunctiond.")
#it will output all chars that are != from constantRegex

#also you can use it to find first(^) or last match($)
beginingHello=re.compile(r'^Hello')
beginsWithHello.search('Hello world!')
# <_sre.SRE_Match object; span=(0, 5), match='Hello'>
beginingHello.search('He said hello.') == None
#True

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
#<_sre.SRE_Match object; span=(16, 17), match='2'>

#Findin all chars exept newline
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']
```

## Time <a name="Time"></a>
```py
#---------------------------------------------------------------------
#Basics TIME
#---------------------------------------------------------------------
import time
time.time() #Returns number of seconds(float) since 1.1.1970(Unix epoch)
#Calculating script time
startTime = time.time()
#----code----
endTime = time.time()
print(endTime-startTime) # prints time in seconds

#cProfile.run() much more informative level of detail that time.time()
#Read doc here -> https://docs.python.org/3/library/profile.html

time.sleep(1) #pass number of seconds you want your program to stay paused
#You cant interrupt program while "sleeping" , ADVICE: dont sleep for 30 seconds , rather for do a for loop
# that sleeps for 1 second every iteration , you can than press CTRL+C to raise KeyboardInterrupt exception

#Rounding Numbers
now = time.time()
round(now)# rounds time to int(clears all decimals),you can pass 2nd arg to round to specify
# number of rounded decimals

#---------------------------------------------------------------------
#Basics DATE&time
#---------------------------------------------------------------------
import datetime
daterime.datetime.now()
#returns datetime obj ( year,month,day,hour,minute,second,microsecond)

#you can compare dates
newYear2016 = datetime.datetime(2016,1,1,0,0,0)
newYear2015 = datetime.datetime(2015,1,1,0,0,0)
newYear2015<newYear2016
>>True

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days,delta.seconds,delta.microseconds
>>(11,36548,0)
delta.total_seconds()
>>986948.0
str(delta)
>>'11 days, 10:09:08'

#---------------------------------------------------------------------
#Converting datetime obj to string
#---------------------------------------------------------------------
oct21st = datetime.datetime(2015,10,21,16,29,0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
>>'2015/10/21 16:29:00'
#If you want all of %Y,%m..-> go to http://strftime.org/

#---------------------------------------------------------------------
#Converting string to datetime obj
#---------------------------------------------------------------------
#custom format string using the same directives
#as strftime() must be passed so that strptime() knows how to parse
#and understand the string.
datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
>>datetime.datetime(2015,10,21,0,0,0)
```


## Multithreading <a name="Multithreading"></a>
```py
#---------------------------------------------------------------------
#Bacics
#---------------------------------------------------------------------
import threading,time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')
    
threadObj = threading.Thread(targer=takeANap)
threadObj.start()
print('End of program.')
>>Start of program
>>End of program
>>Wake up!

#---------------------------------------------------------------------
#Passing arg to thread obj , kwargs stands for keyword argument 
#---------------------------------------------------------------------
# THIS IS INCORRECT WAY!
threadObj = threading.Thread(target=print('cats','dogs',sep=' & '))
#---------------------------------------------------------------------

# This is correct way
#---------------------------------------------------------------------
threadObj = threading.Thread(target=print, args=['Cats','Dogs'],kwargs={'sep':' & '})
threadObj.start()
>>Cats & Dogs
```

## Launching_Programs <a name="Launching_Programs"></a>
```py
#---------------------------------------------------------------------
#Bacics
#---------------------------------------------------------------------
import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# The return value is a Popen obj, which has 2 useful methods: poll() and wait()
# poll() method-> returns None if the process is still runing at the time poll() is called
#              -> if program has terminated it will return process's integer exit code
# You can use exit code to see if process terminated without errors(exit code == 0) if
# there is a error caused the process to terminate(exit code !=0(generally 1))
# wait() method -> Will block until the launched process has terminated
#               -> return value of wait() is exit code

#---------------------------------------------------------------------
#Passing command line arguments to Popen()
#---------------------------------------------------------------------
subprocess.Popen(['C:\\Windows\\notepad.exe','C:\\hello.txt'])
# Launches notepad.exe but also open hello.txt with it
# Can also do with other programs like ect. 
# in hello.py writes print('Hello')
subprocess.Popen(['FULL_PATH_TO_PYTHON.exe','D:\\hello.py'])
>>Hello

subprocess.Popen(['start','hello.txt'],shell=True)
# This should open hello.txt with associated application that opens .txt file extensions 
# in my case this is notepad
# 'start' means open with application associated with .txt in this example
# shell=True is needed only on windows!
```


## Object Oriented Programming<a name="Object-Oriented-programming"></a>
```py
#The 'self' in Python is equivalent to the 'this' pointer in C++

#---------------------------------------------------------------------
# Basics
#---------------------------------------------------------------------
# Lets make simple class
class Person:
    pass # An empty block
>> p = Person()
>> print(p)
<__main__.Person object at 0x07124850> # We print something like this(This tells us we have instance
# of the Person class in the __main__ module

#---------------------------------------------------------------------
# Methods
#---------------------------------------------------------------------
class Person:
    def say_hi(self):
        print('Hello')
>> p = Person()
>> p.say_hi()
Hello
# We can also write this as Person().say_hi()

#----------------------------------
# __init__ (as constructor in c++)
#----------------------------------
class Person:
    def __init__(self,name):
        self.name=name
    
    def say_hi(self):
        print('Hello',self.name)
    
>> p = Person('keljo')
>> p.say_hi()
Hello keljo

# Default init values

class Person:
    def __init__(self,name="Unknown")
        self.name=name
               
>> p = Person()
>> p.name
Unknown
>> p=Person("github")
>> p.name
github

# If you use data members with names using the double underscore prefix such as __private Python uses
# name-mangling to effectively make it a private variable

#----------------------------------
# __doc__
#----------------------------------
# You can write here explanation of your implemented class 
class Test():
    """This is doc"""
    def __init__(self):
        print("yo")

>> t = Test()
yo
>> t.__doc__
This is doc

#----------------------------------
# Inheritance
#----------------------------------
class Employ():   # General supeclass
      def __init__(self,name):       # - 
            self.name = name         # | Common or default behaviors
      def computeSalary(self,hours): # |
            return 20*hours          # -
            
class Engineer(Employ):               # Specialized subclass
      def computeSalary(self,hours):  # Custom behavior ( Engineer is same like Employ but it has better salary )
            return 50*hours           # we can inherid rather than make "new class" and repeat everything we did for Employ 
                                      # basicly that is ingeritance, Engineer has same methods like Employ but we can edit 
                                      # some if we want .. This is usefull if you have class with 10 methods and want to make
                                      # similar class with few diferend methods

>> Bob = Employ("Bob")
>> Sue = Employ("Sue")
>> Tom = Engineer("Tom")
>> company = [Bob,Sue,Tom]
>> for emp in company:
        print("{0}({1}$)".format(emp.name,emp.computeSalary(160)))
#Bob(3200$)
#Sue(3200$)
#Tom(8000$)


#------
# More Examples of inheritance
#-----
class House:
    def __init__(self,name):
        self.name = name
        print('Constructor in house!')
    def tell(self):
        print('Name: {}'.format(self.name),end=" ")

class Member(House):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def tell(self):
        House.tell(self)
        print('Age: {}'.format(self.age))
class Dog(House):
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def tell(self):
        House.tell(self)
        print('Color: {}'.format(self.color))

>> m = Member('keljo',10)
>> d = dog('doggo','Yellow')
# We make m and d ( as Member and Dog)

>> members = [m,d]
# We make list of members 'in' House


>> for member in members:
       member.tell()
Name: keljo Age:10
Name: doggo Color: Yellow
   
# Using for in loop we can easily access all 'members' of House class

# Inheritance is very usefull , we can easily make changes to "House" and it will apply
# to all inherited members ect. we can add new methods to House and we could access 
# that methods through Members and Dog( in this case) or even make new class like 
# Cat(House) and it would have all methods that House have

#----------------------------------
# Simplest python class (roughlt similar to struct in C
#----------------------------------
>> class rec: pass
>> rec.name="test"
>> rec.age = 99      # Just object with attributes
>>print(rec.name)
test
>> x = rec()     # Instances inherit class names
>> x.name
test
>> x.name = "iks"

>> def uppername(obj):
      return obj.name.upper()  #Still needs a self argument(obj)
>> uppername(x)
IKS
>> rec.method = uppername     # Now it's a class's method!
>> x.method()
IKS
>> rec.method()
TEST


#----------------------------------
# Operator overloading
#----------------------------------
# Lets objects coded with classes intercept and respond to operators that work on built-in types
# Classes may override most built-in type operations

#-------
# Example __add__
# Overloading '+'
#-------
class Test():
      def __init__(self,value):
            print("Setting value to: {0}".format(value))
            self.value=value
      def __add__(self,v):
            return 2*self.value+v
>> t = Test(2)
Setting value to: 2
>> t+2
6
# It returns 6 because we overloaded operator, in this example this means every time we add 
# with our class, we will add with 2* value that we gave to it

#-------
# Example __str__
Overloading 'print()'
#-------
class Test():
      def __init__(self,name):
            print("Setting name to: {0}".format(name))
            self.name=name
      def __str__(self):
            return "This class's name is %s" % self.name
>> t = Test("test class")
Setting name to: test class
>>print(t)
This class's name is test class
      
# now every time we write print(Test()) it will output "This class's name is " + class.name
# Example for print https://stackoverflow.com/questions/1535327/how-to-print-a-class-or-objects-of-class-using-print

```
## Working with JSON<a name="JSON"></a>
```py
#Example getting word from dictionary.com
import json,requests
#First get page api
# https://api-portal.dictionary.com/dcom/pageData/LookingWord

#Use request to get 
req = requests.get("https://api-portal.dictionary.com/dcom/pageData/LookingWord")
#Next use json.loads (returns dictionary)
parsed = json.loads(req.text)
#Now we can use json.dumps to pretty print it(easyer to find searched item in dictionary)
print(json.dumps(parsed, indent=4, sort_keys=True))

#And now we can access it
#for example 
>> parsed = {"content":[1,2,3],"users":["test","test"]}
>> print(json.dumps(parsed, indent=2, sort_keys=True))
# {
#   "content": [
#       1,
#       2,
#       3
#   ],
#   "users": [
#      "test",
#       "test"
#   ]
# }
```

# Working with files

## Bat<a name="Bat"></a>
```
#---------------------------------------------------------------------
To run python scripts
#---------------------------------------------------------------------
@py.exe C:\path\to\your\pythonScript.py %*
python must be in sys PATH, advice: put all bat files in one folder and add folder to sys PATH 
you will be able to run your bat files with run (win+r on windows)
```

## Working with files<a name="Working-with-files"></a>
```py
#---------------------------------------------------------------------
#Basics(r/w to files)
#---------------------------------------------------------------------
baconFile=open('bacon.txt','w') #second argument in open is 'w'(overwrites file with new contet)
#if there is no file named 'bacon.txt' then it will create it 
baconFile.write('Hello world!\n') #it returns num of chars written including newline
#dont forget to close file after writing/reading to it
baconFile.close()

baconFile=open('bacon.txt','a') #second arg is 'a' unlike 'w'  it appends contet
baconFile.write('Bacon is not a vegetable.')
#dont forget to close 
baconFile.close()

baconFile.open('bacon.txt')
contet=baconFile.read()
baconFile.close()
print(conte)
#prints contet of baconFile(Hello world!\nBacon is not a vegetable)
#---------------------------------------------------------------------
#Print content of 1 file reversed to another file
#---------------------------------------------------------------------
out = open("output.txt")
f = open ("input.txt")
out.writelines(reversed(f.readlines())
# This prints 'f' reversed to 'out'


# Using os
import os
#---------------------------------------------------------------------
#Getting basic info
#---------------------------------------------------------------------
os.getcwd() #Current working directory in string format
os.path.abspath(path) #returns string of apsolute path
os.path.relpath(path,start) #Will return string of a path from start to path

os.chdir("C:\\Windows\\System32") #Changes working dir
os.makedirs("C:\\delicious\\walnut\\waffles") #Makes dir delicious folder, then inside delicious walnut,
#then inside walnut waffles folder
#---------------------------------------------------------------------
#Checks
#---------------------------------------------------------------------
os.path.isabs(path) #Returns True if is absolute
os.path.exists(path) # returns True if refered file in path exists
os.path.isfile(path) #returns True if path argument exists and is file
os.path.isdir(path)  #returns True if path argument exists and is folder
#---------------------------------------------------------------------
#Delete files,folders(permanent or send to trash)
#---------------------------------------------------------------------
os.unlink(path) #will delete FILE a path
os.rmdir(path) # will delete FOLDER at path
shutil.rmtree(path) # will remove folder at path, and all files and folder it contains will also be deleted

import send2trash
send2trash.send2trash(path) #sends "path" to TRASH

#Prints folders,subfolders and files in folders (os.walk returns name of folder in path
#second parametar is name of subfolder and 3rd parametar is filenames in subfolders
for folderName,subfolders,filenames in os.walk(path):
    print('The current folder is' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF' + folderName + ': '+subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName+': '+ filename)
    print('')
    
```

## ZIP FILES<a name="ZIP-FILES"></a>
```py
#---------------------------------------------------------------------
#Basics
#---------------------------------------------------------------------
import zipfile
#navigate to foldere where is zip you wanna work with
exampleZip = zipfile.ZipFile('testzip.zip') #exampleZip is testzip.zip now
exampleZip.namelist() 
#prints all folders/subfolders and files of zip file
#---------------------------------------------------------------------
#Getting size,compressing size..extracting..
#---------------------------------------------------------------------
fileinsidezip.file_size() #prints size of file in bytes
fileinsidezip.compress_size #prints compressed size in bytes
exampleZip.extractall(path(optional)) # extracts files in zip in current working dir
#if no folder called like path extractall will make it
exampleZip.extract(file/folder,path(optional))#extracts specific file/folder to working dir | (optional) path
exampleZip.close() #When you finish working with file
#---------------------------------------------------------------------
#creating new zip files
#---------------------------------------------------------------------
newZip = zipfile.ZipFile('new.zip','w') #opens zipfile object in write('w') mode , also has append('a') mode
newZip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
```

## Excel<a name="Excel"></a>
```py
#---------------------------------------------------------------------
#Basics
#---------------------------------------------------------------------
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
type(wb)
>> <class 'openpyxl.workbook.workbook.Workbook'>
wb.get_sheet_names() #prints list of sheets
sheet = wb.get_sheet_by_name('Sheet3')
sheet #prints <Worksheet "Sheet3">
sheet['A1'] #returns <Cell Sheet3.A1>
sheet['A1'].value #Gets value of A1
c = sheet['B1']
c.value # gets value of c -> value of sheet['B1]
c.row #prints 1
c.column #prints B
c.coordinate #prints B1

sheet.cell(row = 1 , column = 2).value #Gets value at 1st row and 2nd column
for i in range (1,6,2):
        print(i, sheet.cell(row = i , column = 2).value)
#prints following..
1 Apples
3 Pears
5 Strawberries
#---------------------------------------------------------------------
#Getting full table printed
#---------------------------------------------------------------------
sheet = wb.get_sheet_by_name('Sheet1')
tuple(sheet['A1':'C3'])
#should write sth like this ((<Cell Sheet1.A1>, <Cell Sheet1.B1>, <Cell Sheet1.C1>),
>>(<Cell Sheet1.A2>,#<Cell Sheet1.B2>, <Cell Sheet1.C2>), (<Cell Sheet1.A3>,
>><Cell Sheet1.B3>,<Cell Sheet1.C3>))

for row in sheet['A1':'C3']):
        for cell in row:
                print(cell.coordinate, cell.value)
        print('--- END OF ROW ---')
        
#outputs following 
#>>A1 2015-04-05 13:34:02
#>>B1 Apples
#>>C1 73
#>>--- END OF ROW ---
#>>A2 2015-04-05 03:41:23
#>>B2 Cherries
#>>C2 85
#>>--- END OF ROW ---
#>>A3 2015-04-06 12:46:51
#>>B3 Pears
#>>C3 14
#>>--- END OF ROW ---

#---------------------------------------------------------------------
#Create/remove Sheet, save file ..
#---------------------------------------------------------------------
sheet = wb.worksheets[0]
sheet.max_row #returns max row, good for for iterations..

wb.get_sheet_names()
>>['Sheet']
sheet = wb.get_active_sheet()
sheet.title
>>'Sheet'
sheet.title = 'Spam Bacon Eggs Sheet' #Every time you change name you need to save file to "make it count"
wb.get_sheet_names()
>>['Spam Bacon Eggs Sheet']
wb.save('example_copy.xlsx') #Saves new changed file in example_copy.xlsx

wb.create_sheet()
>> <Worksheet Sheet1>
wb.get_sheet_names()
>>['Sheet','Sheet1']
wb.create_sheet(index=0,title = 'First Sheet')
>><Worksheet "First Sheet">
wb.get_sheet_names()
>>['First Sheet','Sheet','Sheet1']
wb.remove_sheet(wb.get_sheet_by_name('Sheet'))
wb.get_sheet_names()
>>['First Sheet','Sheet1']
#---------------------------------------------------------------------
#Adding new content to tables..
#---------------------------------------------------------------------
sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'] = 'Test' #Writes Test to A1 cell in 'Sheet'
sheet['A1'].value
>>'Test'
```

## Shutil<a name="Shutil"></a>
```py
import shutil
shutil.copy('source','destination')#it will copy source file to destination folder
shutil.copytree('source','destination')#it will copy everything from bacon to bacon_backup
shutil.move('source','destination')#move source to destination folder(if source exists it overwrites),you can
#also rename it if you put diferend name in destination ('C:\\bacon.txt','C:\\eggs\\new_bacon.txt')
shutil.rmtree(path) # will remove folder at path, and all files and folder it contains will also be deleted
```


## Manipulating_Images <a name="Manipulating_Images"></a>
```py
#---------------------------------------------------------------------
# Basics
#---------------------------------------------------------------------
from PIL import ImageColor
>>ImageColor.getcolor('red','RGBA')
(255,0,0,255) 
# Basicly getcolor returns RGBA tuple (its case INsensitive->'red'=='RED')

# Loading image 
from PIL import Image
catIm = Image.open('zophie.png')
# If img is not in cur working dir just import os and os.chdir('C:\\folder_with_image_file')

#---------------------------------------------------------------------
# Working with Image Data Type
#---------------------------------------------------------------------
>>catIm.size
(816,1088)
>>width,height = catIm.size

>>width
816
>>height
1088

>>catIm.filename
'zophie.png'
>>catIm.format
'PNG'
>>catIm.format_description
'Portable network graphic'
>>catIm.save('zophie.jpg')
# Saves zophie.jpg on hdd(now you have zophie.jpg and zophie.png)

im = Image.new('RGBA',(100,200),'purple') # Creates im obj(purple color 100x200 pix)
im.save('purpleImage.png') # Saves im obj as purpleImage in cur working dir 

#---------------------------------------------------------------------
# Cropping Images,Copying and Pasting images onto Other Images
#---------------------------------------------------------------------
catIm = image.open('zophie.png')
#---------------------------------------------------------------------
faceIm = catIm.crop((335,345,565,560)) # Crops and saves it to faceIm (catIm is still same)
# 1st parametar = left side,if ++ crop "goes" to left
# 2nd parametar = top side,++ == top side goes down
# 3 == (right side)+1, ++ == right side goes left
# 4 == (bottom side)+1 , ++ == bottom side goes down
>>faceIm.size
(230,215)
#---------------------------------------------------------------------
catCopyIm = catIm.copy() # Creates catCopyIm (copy of catIm)
catCopyIm = paste(faceIm,(0,0))
catCopyIm = paste(faceIm,(400,500))
catCopyIm.save('pasted.png')

# This code above opened cat img, cropped from it and saved to faceIm , pasted faceIm 2 times
# On copy of catIm (catCopyIm) on coordinates in (x,y)

# Making "matrix" of crops
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopy = catIm.copy() # Get copy so you dont mess with originaly photo :P
for left in range(0,catImWidth,faceImWidth):# For from left side to right "jumping" for len of crop width
    for top in range(0,catImHeight, faceimHeight): # For from top to bottom for crop height
        print(left,top) # Printing this is just for info
        catCopyTwo.paste(faceIm,(left,top) # Paste crop on picture on location(left,top)
        
#---------------------------------------------------------------------
# Resizing
#---------------------------------------------------------------------
W,H=catIm.size
quartersizedIm = catim.resize(( int(H/2) , int(W/2) ))
quartersizedIm.save('quartersized.png)

#---------------------------------------------------------------------
# Rotating,Flipping..
#---------------------------------------------------------------------
catIm.rotate(90).save('rotated90.png')
catIm.rotate(270).save('rotated270.png')

catIm.rotate(6).save('cat.png') # Edges will be "cut off" cause of rotation
catIm.rotate(6,expand=True).save('cat_expand.png') # Picture will fit to rotation(it will be bigger)

#---------------------------------------------------------------------
# Mirroring
#---------------------------------------------------------------------
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

#---------------------------------------------------------------------
# Changing Individual Pixels
#---------------------------------------------------------------------
im = Image.new('RGBA',(100,100))
>>im.getpixel((0,0))
(0,0,0,0)
for x in range(100):
    for y in range(50):
        im.putpixel((x,y),(210,210,210))
        
#---------------------------------------------------------------------
# Drawing on Images
#---------------------------------------------------------------------
from PIL import Image, ImageDraw
im = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(im) # Pass image obj to draw to create image draw obj

#---------------------------------------------------------------------
# Drawing Shapes
#---------------------------------------------------------------------
https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# Pointless to make notes of this, just throw look at this link above ,
# if link is broken when you are reading this google for python PIL drawing :)  

#---------------------------------------------------------------------
# Drawing Text
#---------------------------------------------------------------------
from PIL import ImageFont
# ImageFont is imported now , you can call ImageFont.truetype() ->takes 2 arg
# 1. is string for the font's TrueType file(.ttf)
# 2. is size :D
# Here's example!
#-----------------------------
from PIL import Image, ImageDraw, ImageFont
import os
#-----------------------------
im = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20,150), 'Hello', fill='purple')
#-----------------------------
fontsFolder = 'FONT_FOLDER' # e.g. 'C:\Windows\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100,150), 'Howday', fill='gray', font=arialFont)
#-----------------------------
im.save('text.png')
# This should make png with printed Hello and Howdy in diferend fonts and on diferend positions
# I showed there 2 ways of Drawing text
```

# Working online

## Web Scraping<a name="Web-Scraping"></a>
```py
#---------------------------------------------------------------------
#webbrowser,requests
#---------------------------------------------------------------------
import webbrowser
import requests

webbrowser.open(URL)#opens that page in new tab

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')#res == page source
res.status_code == requests.codes.ok #returns true if request succeeded
#you can also check len(res.text), and print it 
print(res.text[:250])

res.raise_for_status() #this will raise an exception if there was and error downloading
#and will do nothing if the download succeeded

#good practice to do is 
try:
    res.raise_for_status()
except Exception as exc:
    print('Problem with res: %s' % (exc))
    
#---------------------------------------------------------------------
#Saving to hard drive
#---------------------------------------------------------------------
res = requests.get(URL)
res.raise_for_status() #Check if any errors
playFile = open('Filename.txt','wb')
for chunk in res.iter_content(size of chunks):
    playFile.write(chunk)
#each chunk is of the bytes data type and you get to specify how many bytes each chunk will contain
#100 000 is generally a good size    
playFile.close()

#---------------------------------------------------------------------
#BeautifulSoup module
#---------------------------------------------------------------------
import bs4
res = requests.get(url)#get page source
noStarchSoup = bs4.BeautifulSoup(res.text)#stores res in noStarchSoup
#you can also load an HTML file from hdd 
exampleFile = open('example.html')
exampleSoup=bs4.BeautifulSoup(exampleFile)

#finding element with select()
soup.select('div') #All elements named <div>
soup.select('#author') #The element with and id attribute of author
soup.select('.notice') #All lements that use a CSS class attribute names notice
soup.select('div span') #All elements named <span> that are withing an element named <div>
soup.select('div>span') #All elements named <span> that are directly within and leement named <div>
soup.select('input[name]') #All elements named <input> that have a name attribute with any valute
soup.select('input[type="button"]') #All elements named <input>that have and attribute 
                                    #named type with value button
#working with files
exampleFile=open('example.html','r') #open html file for reading
exampleSoup = bs4.BeautifulSoup(exampleFile) read example.html in exampleSoup
print(exampleSoup.text[:200]) #print first 200 chars from exampleSoup(loaded from file)

elems = exampleSoup.select('#author') #creates list of all id="author"
>>len(elems) #checking how many "author" id's are
1

elems[0].getText() #elems has only 1 id="author" so we want 1st elem of elems(0 elem is first in list)
#'Al sweigart' , this is "inner" HTML , see diference on line below
str(elems[0]) # returns "html" version of "author"
#<span id="author">Al Sweigart</span>

#we can use exampleSoup.get to find some key elements
exampleSoup.get('id') #prints 'author'
exampleSoup.get('some_nonexistent_addr') == None #prints True
exampleSoup.attrs #prints {'id:'author'}
exampleFile.close()

#---------------------------------------------------------------------
#Selenium
#MORE INFO : http://selenium-python.readthedocs.org/
#---------------------------------------------------------------------
from selenium import webdriver

browser = webdriver.Firefox() #opens firefox
type(browser)
#<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('http://inventwithpython.com') #opens that site in 'browser'

#---------------------------------------------------------------------
# find_element_by...
#---------------------------------------------------------------------
#in basic syntax is browser.find_element/elements+something if you put element
#it returns single WebElement object , but if you put elements it returns list of all WebElement's
#ect. 
browser.find_element_by_class_name('name') #Elements that use CSS class 'name'
#if you use here browser.find_elements_by_class_name(name) it would return list of all classes
#named 'name'

css_selector(selector) #Elements that match the CSS selector
id(id) #Elements with a matching id attribute value
link_text(text) #<a> elements that completely match the text provided
partial_link_text(text) #<a> elements that contain the text provided
name(name) #Elements with a matching name atribute value
tag_name(name) #Elements with a matching tag name(case insensitive; an <a> element is matched by
# 'a' and 'A')
#---------------------------------------------------------------------
#Once you have the WebElement object you can find out more about it vy reading the attributes or 
#calling the methods
#---------------------------------------------------------------------
tag_name #The tag name , such as 'a' for an <a> element
get_attribute(name) #The value for the element's name attribute
text #  The the text within the element , such as 'Hello' in <span>Hello</span>
clear() #For text field or text area elements , clears the text typed into it
is_displayed() #Returns True if the element is visible
is_enabled() #For input elements , returns True if the element is enabled
is_selected() #For checkbox or radio button elements , returns True if the element is selected
location #A dictionary with keys 'x' and 'y' for the position of the element in page
#---------------------------------------------------------------------
#Special Keys (arrow,end,home..),Clicking,browser buttons..
#---------------------------------------------------------------------
from selenium.webdriver.common.keys import Keys
#you just sent them as normal key
linkElem.send_keys(Keys.END)# 'press END'

#Clicking
linkElem = browser.find_element_by_link_text('Read It Online')
linkElem.click() #Clicks on Read it online

#Browser buttons
browser.back() #Clicks Back button
browser.forward()
browser.refresh()
browser.quit()
#---------------------------------------------------------------------
```

## Sending_email_and_Text_messages <a name="Sending_email_and_Text_messages"></a>
```py
SMTP
#---------------------------------------------------------------------
#Connecting to server
#---------------------------------------------------------------------
import smtplib
# Search for <your provider> smtp settings to see server and port to use
# in this example il do with gmail

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
# if smptlib.SMPT() call is not successful your SMTP server might not support TLS on port 587
# in that case use smtplib.SMTP_SSL() and port 465 instead

#Call oddly named ehlo() to "say hello" to the SMTP email server
smtpObj.ehlo()
#for me it responded(its in 1 row but i put in 2 so i dont have long line :P)
#(250, b'smtp.gmail.com at your service, [your.ip.address.is.here]\nSIZE 35882577\n8BITMIME
#\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

#---------------------------------------------------------------------
#Sending mail and disconnectiong from server
#---------------------------------------------------------------------
# Logging in gmail
smtpObj.login('YOUR_EMAIL','YOUR_PASSWORD') 
# If you use 2-Step Verification create app password and copy that under your_password

smtpObj.sendmail('my_email_address@gmail.com', 'recipient@example.com',
'Subject: Some subject.\nEmail send with python <3')
# sendmail takes 3 arg-> Your email as a string
#                     -> Recipients email as a string or a list of strings(for multiple recipients)
#                     -> Email body as string
# Start of email body string must begin with 'Subject: \n' for the subject line of the email
>>{} #Empty dictionary means all recipients were successfully send the email

#Disconnecting from the SMTP Server
smtpObj.quit()
#The 221 in the return value menas the session is ending
#---------------------------------------------------------------------

IMAP
#---------------------------------------------------------------------
#Connecting to server
#---------------------------------------------------------------------
import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com',ssl=True)
imapObj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')

#---------------------------------------------------------------------
#Selecting Folder and searching for email
#---------------------------------------------------------------------
import pprint
pprint.pprint(imapObj.list_folders())
#should print alot of nested lists :D

#To select a folder to search through pass folders name as a string
imapObj.select_folder('INBOX',readonly=True)
#If selected folder does not exist python will raise an imaplib.error exception
#readonly=True prevents you from accidentally making changes or deletions to any of the emails in this folder
#---------------------------------------------------------------------
#Performing the search
#---------------------------------------------------------------------
#You will need IMAP Search Keys see link bellow , if not working just google for it :)
# -> https://afterlogic.com/mailbee-net/docs/MailBee.ImapMail.Imap.Search_overload_2.html
#Here are some example search() method calls
#---------------------------------------------------------------------
imapObj.search(['ALL'] # Returns every message in the currently selected folder.
imapObj.search(['ON 05-Jul-2015']) # Returns every message sent on July 5, 2015

imapObj.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015', 'UNSEEN'])
# Returns every message sent in January 2015 that is unread. (Note that
# this means on and after January 1 and up to but not including February 1.)

imapObj.search(['SINCE 01-Jan-2015', 'FROM alice@example.com']) 
# Returns every message from alice@example.com sent since the start of 2015.

imapObj.search(['SINCE 01-Jan-2015', 'NOT FROM alice@example.com'])
# Returns every message sent from everyone except alice@example.com
# since the start of 2015.
#---------------------------------------------------------------------
# Search method returns unique IDs (UIDs) for the emails, as integer values
# Pass UIDs to the fetch() method to obtain the email content
UIDs = imapObj.gmail_search('meaning of life') # this is googles search you can use it instead of search()
>>UIDs
[42]
#---------------------------------------------------------------------
#Fetching an Email and marking it as Read
#---------------------------------------------------------------------
#UIDs is list of UIDs xD , and BODY[] tells fetch() to download all body content of emails from UIDs
rawMessages = imapObj.fetch(UIDs,['BODY[]'])
import pprint
pprint.pprint('rawMessages')
# This is ect. what should be printed as rawMessages using pprint

# {40040: {'BODY[]': 'Delivered-To: my_email_address@gmail.com\r\n'
# 'Received: by 10.76.71.167 with SMTP id '
# --snip--
# '\r\n'
# '------=_Part_6000970_707736290.1404819487066--\r\n',
# 'SEQ': 5430}}


#---------------------------------------------------------------------
#Size limits
#---------------------------------------------------------------------
# If your search matches a large number of email messages, Python might
# raise an exception that says imaplib.error: got more than 10000 bytes. When
# this happens, you will have to disconnect and reconnect to the IMAP server and try again

import imaplib
imaplib._MAXLINE = 1000000
#This should fix the problem :) _MAXLINE changes limit


#---------------------------------------------------------------------
#Getting Email Addresses from a Raw Message
#---------------------------------------------------------------------
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
# Now you can use several methods that make easy to get email's subject,sender..
message.get_subject()
>>'Hello!'
message.get_addresses('from')
>>[('Some Name','somename@gmail.com')]
message.get_addresses('to')
>>[('My Email','myemail@gmail.com')]

message.text_part != None
>>True
message.html_part != None
>>True
# This are check to see "shape" of message, .text_part != None means it is builded with at least normal text
# .html_part != None means its builded with at least html, if both are True that means msg is html and normal
# Getting string of mail
# If its plaintext
message.text_part.get_payload().decode(message.text_part.charset)
# If its html content
message.html_part.get_payload().decode(message.html_part.charset)
#Current message is both html and plaintext :) so i can use both to extract string


#---------------------------------------------------------------------
#Deleting Emails
#---------------------------------------------------------------------
imapObj.select_folder('INBOX',readonly=False)
UIDs = imapObj.search(['ON 09-Jul-2015'])
imapObj.delete_messages(UIDs) # Puts /Deleted flag on all UIDs
>>{40066: ('\\Seen', '\\Deleted')}
imapObj.expunge() #Permanently deletes messages with /Deleted flag
>>('Success', [(5452, 'EXISTS')])

#---------------------------------------------------------------------
#Dissconecting from IMAP Server
#---------------------------------------------------------------------
imapObj.logout()
```

# Controling GUI

## Controling_Mouse&Keyboard_with_GUI_Automation <a name="Controling_Mouse&Keyboard_with_GUI_Automation"></a>
```py
#---------------------------------------------------------------------
#-----------------------------WARNING---------------------------------
#---------------------------------------------------------------------
# if you use GUI automation there are problems if program goes out of control,
# ect. missclicks something , python doesnt know that it missed so it will countinue to do its job
# and will do it than probably wrong and it can maybe make some unwanted damage to system xd
# To keep it safe you can add pauses after every autogui function call
import pyautogui
pyautogui.PAUSE = 1      # Pauses for 1 second so you have some time to exit program :P

# There is also option to use FAILSAFE feature , basicly moveing your mouse in top left corner
# raises FailSafeException exception
pyautogui.FAILSAFE = True # Put False if you want to disable it 

#---------------------------------------------------------------------
# Controlling Mouse Movement
#---------------------------------------------------------------------
import pyautogui
pyautogui.size() # Returns tuple of screens width and height in pixels
pyautogui.moveTo(x, y, duration=0.25) 
# Moves mouse to (x,y) on screen in 0.25s , duration parametar is not needed(mouse teleports then)

pyautogui.moveRel(x,y,duration=0.25) # Same as moveTo but moves mouse relative to current position
pyautogui.position() # Returns tuple of mouse's current position

#---------------------------------------------------------------------
# Clicking the Mouse
#---------------------------------------------------------------------
pyautogui.click(10,5) # [LEFT click by default] Clicks on x==10,y==5
pyautogui.click(10,5, button='left') # You can specify button->'left','middle' and 'right' click

pyautogui.mouseDown() # Do i need to explain this 2 ? :d,pushes left mouse button.,same as click
                      # It can also take button= argument for left,right and middle button
pyautogui.mouseUp()   # Releases the button

# You can also do this
pyautogui.middleClick()
pyautogui.doubleClick()
pyautogui.rightClick()

#---------------------------------------------------------------------
# Dragging the Mouse
#---------------------------------------------------------------------
pyautogui.dragTo(x, y, duration=0.25) # Arg are same as moveTo and moveRel
pyautogui.dragRel(x,y,duration=0.25)

#---------------------------------------------------------------------
# Scrolling the Mouse
#---------------------------------------------------------------------
pyautogui.scroll(200)
# Scrolls UP, if int in function is negative then it scrolls DOWN

#---------------------------------------------------------------------
# Working with the Screen
#---------------------------------------------------------------------
# Getting a Screenshot
im = pyautogui.screentshot()
#-------------------------------
#[Quick code]Screenshot,copy ss to clipboard so you can paste it to discord xD and save it to desktop :P
#-------------------------------
import os,pyperclip
os.chdir('C:Desktop/')
pyperclip.copy(im)
im.save('test.png')
#---------------------------------------------------------------------
# Image recognition
#---------------------------------------------------------------------
pyautogui.locateOnScreen('picture.png')
# Returns tuple of 4 int (x,y,W,H) x,y is top left corner of found element
# and W,H are width and height of that obj from x,y position 

# If there are multiple same obj(like picture) you can create list of tuples
list(pyautogui.locateAllOnScreen('picture.png')

pyautogui.center((643, 745, 70, 29)) # ect. Returns coordinates of obj's center
>> (678, 759)
pyautogui.click((678, 759)) # Clicks middle of located obj(picture)

#---------------------------------------------------------------------
# Controling the Keyboard
#---------------------------------------------------------------------
pyautogui.click(100,200); pyautogui.typewrite('Hello world!')
# I clicked first to put window in focus then i send virtual keys to clicked [text box ect]
# There is also second parametar in typewrite cause this will type string instantly.. you can pass
# number of s for each key stroke
pyautogui.typewrite("This",0.25)

# Writing key names
pyautogui.typewrite('a','left','b') # Thsi will write a,go left and write b
# finaly output will be 'ba' 

# Here are all of Keyboard Attributes
  - https://i.imgur.com/nrr0rqh.png
#-------------------------------------
# Pressing and Releasing the Keyboard
#-------------------------------------
# Much like mouseDown() and MouseUp()
pyautogui.keyDown('shift');pyautogui.press('4');pyautogui.keyUp('shift')
>> '$'
  
# Hotkeys
# If you want to press ctrl+c ( to copy something) you would need 2 keyDown and 2 keyUp lines
# you can use this instead
pyautogui.hotkey('ctrl','c') # Presses keys by order and releases them in reverse
```

# Random libs

## Turtle module <a name="Turtle_module"></a>
```py

#-------------------------------------
# Basics
#-------------------------------------
import turtle
wn = turtle.Screen()   # Creates a playground for turtles
alex = turtle.Turtle() # Create a turtle, assing to alex

alex.forward(50) # Tell alex to go forward by 50 units
alex.left(90) # Tell alex to turn by 90 degrees
wn.mainloop() # Wait for user to close window

#-------------------------------------
# Window
#-------------------------------------
wn.bgcolor("lightgreen") # Set the window background color
wn.title("Hello darknes my old friend") # Set the window title

#-------------------------------------
# Color,size..
#-------------------------------------
tess = turtle.Turtle()
tess.color("blue") # Change color of turtle to blue
tess.pensize(3) # Tell tess to set her pen width
#-------------------------------------
# More movement
#-------------------------------------
tess.forward(-100) # Moves back for 100 units
tess.left(-30) # turns to right
tess.backward(-100) # Moves forward for 100 units :D

#-------------------------------------
# More drawing
#-------------------------------------
tess.penup()  # Lifts 'pen' up , that means we can move turtle without drawing any lines on board
tess.forward(90)
tess.pendown() # We are drawing now

# Pen shapes
tess.shape("turtle") # Yaay we are turtle now 

# Leave stamps ( shape on current position)
tess.stamp() 


# Writing
tess.write("Hello!")
# displays Hello! at the turtle's position

# We can fill shapes (circle,semicircle,triangle...)
tess.color("blue","red") # blue is pen color and red is fill color 
tess.begin_fill() # We call this method , then draw shape
tess.end_fill()   # then call this method to 'fill' drawed shape

#-------------------------------------
# Events
#-------------------------------------
# Im not writing all code, just snippet that refers to event

# Key presses
wn.onkey(tess.forward(30),"Up")
wn.onkey(tess.left(45),"Left")
wn.onkey(tess.right(45),"Right")
wn.onkey(wn.bye(),"q")
wn.listen() # This tells window to start listening for events,if any of the keys that we're monitoring
# is presses ,its handler will be called

# Mouse clicks
def click(x, y):
    tess.goto(x,y)

wn.onclick(click)   # When you click tess moves on that position
wn.mainloop()  

# Timing

def h1():
    tess.forward(100)
    tess.left(12)
wn.ontimer(h1,2000)  # Set timer and after 2000 miliseconds(2s) it will execute h1()
```

## Pygame <a name="Pygame"></a>
```py

#---------------------------------------------------------------------
# Installing & Basics
#---------------------------------------------------------------------
pip3 install pygame
# More info if here not enough -> https://www.pygame.org/docs/

# Basic skeleton of games
# Setup game
# goto:
#      Poll and handle events  (if exit() -> close down game)
#      Update game events
#      Draw surface
#      Show surface
#      goto()


import pygame

def main():
    #----------setup game----------
    pygame.init()     # Prepare the pygame module for use
    surface_sz = 480  # Desired physical surface size, in pixels
    
    # Create surface of (width,height) , and its window
    main_surface = pygame.display.set_mode((surface_sz,surface_sz))
    
    # Set up some data to describe a small rectangle and its color
    small_rect = (300,200,150,90)
    some_color = (255,0,0)   # RGB

    while True:  # goto
        #---------Poll and handle events------------
        ev = pygame.event.poll()
        if ev.type==pygame.QUIT: # Window close button clicker?
            break              # ...leave game loop

        #----------Update your game objects and data structures here------
        #....
        #------------Draw surface----------------
        # we draw everything from scrath on each frame
        # So first fill everything with the background color
        main_surface.fill((0,200,255))
        
        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)
        
        #------------Show surface-----------------
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        # goto()
        
    pygame.quit() # Once we leave the loop, close the window

#---------------------------------------------------------------------
# Drawing pictures,text..
#---------------------------------------------------------------------

#-------------------------
# Pictures
#-------------------------
import pygame
# In setup game part you need to load image
ball = pygame.image.load("ball.png")

# In draw surface
main_surface.blit(ball, (100,120))  # blit- widely used in computer graphic,means to make 
#blit(what_to_display,(position))           |_ a fast copy of pixels from one area of memory to another
#-------------------------
# Text
#-------------------------
# Setup game part
my_font = pygame.font.SysFont('Courier',16) # Self explanation

# Draw surface part
the_text = my_font.render("Hello, world!",True,(0,0,0))
main_surface.blit(the_text,(10,10))
```


#  Debugging

## Assertions<a name="Assertions"></a>
```py
#---------------------------------------------------------------------
#Basics
#---------------------------------------------------------------------
#You can see where is bug in your program if you include them
# 1st "Paramar to chech if false then when problem happens you can write feedback to see what is the problem"
# 2nd "Feedback to output when problem occures
assert "red" in stoplight.values() , "Neither light is red!"+str(stoplight)
#if there is no red in dic keys then program writes this:
#AssertionError : Neither light is red! {'key1':'blue','key2':'green'}
#As you can see i would immediately assume that error is in dictionary
```

## Logging<a name="Logging"></a>
```py
#---------------------------------------------------------------------
#Basics
#---------------------------------------------------------------------
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
#basic syntax for logging , its usefull when debugging to see what is happening in program
#if you want to write logs in file just pass KEYWORD filename="nameoffile.txt" as one of parametars
logging.basicConfig(filename="log.txt",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Msg')
#Prints 2018-03-25 16:51:35,172 - DEBUG - Msg
#if debug is succesful then you can skip printing msg's with 
logging.disable(logging.CRITICAL)
#you simply pass logging.disable() a logging level , and it will suppress all log msg at that lvl and lower 
```

## Useful data <a name="Useful-data"></a>
```py
#---------------------------------------------------------------------
# Keywords(probably changed so look for it online this is just reminder)
#---------------------------------------------------------------------
If interpretrer complains about one of your variable names and you dont know what see this list
# +--------+-------+--------+---------+-------+----------+
# | and    | as    | assert | break   | class | continue |
# | def    | del   | elif   | else    | except| exec     |
# | finally| for   | from   | global  | if    | import   |
# | in     | is    | lambda | nonlocal| not   | or       |
# | pass   | raise | return | try     | while | with     |
# | yield  | True  | False  | None    |       |          |
# +--------+-------+--------+---------+-------+----------+
```
