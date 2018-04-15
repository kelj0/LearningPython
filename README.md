# NOTES FOR PYTHON

### DEBUGGER

If you want to get input in debugger 

>go in launch.json file (ctrl+shitf+D)

>in first part add python path to pythonPath

>below add "console":"externalTerminal" (dont forget to put ',' after line)

---

## Table of contents

-    [Basics](#Basics)
-    [Data types](#Data-Types)
-    [Web Scraping](#Web-Scraping)
-    [Bat](#Bat)
-    [Strings](#Strings)
-    [Assertions](#Assertions)
-    [Logging](#Logging)
-    [Working with files](#Working-with-files)
-    [ZIP FILES](#ZIP-FILES)
-    [Excel](#Excel)
-    [Shutil](#Shutil)
-    [Regex](#Regex)
-    [Time](#Time)
-    [Multithreading](#Multithreading)
-    [Launching Programs](#Launching_Programs)
-    [Sending email and Text messages](#Sending_email_and_Text_messages)
-    [Manipulating Images](#Manipulating_Images)
-    [Controling Mouse Keyboard with GUI Automation](#Controling_Mouse&Keyboard_with_GUI_Automation)

---

## Basic <a name="Basics"></a>
Printing text
```py
print("Print text")

#Random
import random
a=[1,2,3]
random.shuffle(a)#Shuffles elements in list 
random.sample(a,2)#Takes random 2 elements in list 

#While
while True:
    s=input("Enter string")
    if s=='quit':
      break
    else:
      print(s)

#For
for i in range(0,5):
    print(i)
#prints from 0 to 4(if added 3rd number in brackets(0,5,X) prints every i+X)

#---------------------------------------------------------------------
# Functions
#---------------------------------------------------------------------
# Lets make 2 files -> foo.py and test.py
def foo():
    print('Hello from function!')
# Save it as foo.py in same dir as test.py
# in test.py write following

from foo import *
foo() # Prints "Hello from funciton!"
# Read as from file foo.py import all 
# This is usefull for making your code cleaner :)

# Getting values to foo
def changeA(a):
    a=5
    return a
a=1
changeA(a)
# If we call this foo it will change "scoped a" that means that every variable in
# function is diferend from variables in other functions
# a is still 1 after function, if we want to change global variables write following

a=10

def changeA(a):
    global a=20
    return a

changeA(a)
# This indeed changes a to 20 :)

def testFoo(incomingVariable):
    return incomingVariable

sendingVariable = "Here comes nothing"
testFoo(sendingVariable)
# This calls testFoo and sends "sendingVariable" , function recives variable(makes copy)
# and calls it "incomingVariable" in his scope 

#---------------------------------------------------------------------
# Advanced
#---------------------------------------------------------------------
def makeLine(a,b):
    def y(x):
        return x*5
    return y
    
a = makeLine(5,2)
a(1)
# returns 5

# This is called creating functions on the fly, this makes foo that RETURNS FOO!
# You can now call a ,pass parametar and it will return parametar multiplyed by 5
# C,C++ and many other languages dont allow you to define foo that retunrs foo

```

## Data types<a name="Data-Types"></a>
```py
#---------------------------------------------------------------------
#LIST
#---------------------------------------------------------------------
list=["item1","item2","item3"]
#printing it
print(list)

#---------------------------------------------------------------------
#TUPLES
#---------------------------------------------------------------------
#Same like list but without extensive funcionality  (they are immutable also)
tuple=("Car",1,0,5)
print(tuple)
#>> car 1 0.5

#---------------------------------------------------------------------
#DICTIONARY
#---------------------------------------------------------------------
ab={
'Key1':'Item1',
'Key2':'Item2'
}
#printing
print(ab['Key1'])#prints Item1

#printing list element as in dict parametar valute()
names={"imena":["karlo","pero","duro"],"prezimena":["kegljo","peric","duric"]}
 for i in range(3):
      print("IME:",names['imena'][i])
      print("PREZIME:",names['prezimena'][i])

#Nested dictionary
dic={'nested':{'name':karlo,'year':1},'nestedList':[1,2,3]}

print(dic['nested']['name'])
#'karlo'
print(dic['nested']['nestedList'][0])
'1'

#---------------------------------------------------------------------
#SEQUENCES
#---------------------------------------------------------------------
#same ase list but with aditional foo
#first parameter is where to begin(if not it begins from start)
#second parametar is where to end(if not it ends on end)
#third parametar is jump ( if 2 then 1,3 from seq[1,2,3,4]
print("List from 0-2",shopinglist[0:3])
print("List all",shopinglist[:]
print("List by i+=X",shopinglist[::X]
#lists all seq but every X item
```

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

res.raise_for_status() #this will raise an exception if there was and error downloading the file
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

## Bat<a name="Bat"></a>
```
#---------------------------------------------------------------------
To run python scripts
#---------------------------------------------------------------------
@py.exe C:\path\to\your\pythonScript.py %*
python must be in sys PATH, advice: put all bat files in one folder and add folder to sys PATH 
you will be able to run your bat files with run (win+r on windows)
```

## Strings<a name="Strings"></a>
```py
#---------------------------------------------------------------------
#Basics
#---------------------------------------------------------------------
#CONVERTING LIST TO STRING
some_list=["k","a","r","l","o"]
names=''.join(some_list)

# default spaces in rjust ljust in second parametar 
'hello'.rjust(10,'*')
#prints '*****hello'
'hello'.ljust(10,'*')
#prints 'hello*****'
'hello'.center(10,'=')
#prints '==hello==='
#---------------------------------------------------------------------
#Checks
#---------------------------------------------------------------------
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
#---------------------------------------------------------------------
delimiter='_*_'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist))#prints mylist[0] delimiter then mylist[1] ..
```

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

## Working with files<a name="Working-with-files"></a>
```py
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
#---------------------------------------------------------------------
#Basics(r/w to files)
#---------------------------------------------------------------------
baconFile=open('bacon.txt','w') #second argument in open is 'w'(overwrites file with new contet)
#if there is no file named 'bacon.txt' then it will create it 
baconFile.write('Hello world!\n') #it returns num of chars written including newline
text = baconFile.read() # This reads file in string "text"
#dont forget to close file after writing/reading to it
baconFile.close()

# Trick to delete condent from file
open(fileName,"w").close() # As you learned "w" clears file to make it clear to write in it 
# we close file immediately and file is clear as new :P

baconFile=open('bacon.txt','a') #second arg is 'a' unlike 'w'  it appends contet
baconFile.write('Bacon is not a vegetable.')
#dont forget to close 
baconFile.close()

baconFile.open('bacon.txt')
content=baconFile.read()
baconFile.close()
print(content)
#prints content of baconFile(Hello world!\nBacon is not a vegetable)

# Reading files without whitespaces
from scanner import *
s= Scanner("")


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
#(<Cell Sheet1.A2>,#<Cell Sheet1.B2>, <Cell Sheet1.C2>), (<Cell Sheet1.A3>,
#<Cell Sheet1.B3>,<Cell Sheet1.C3>))

for row in sheet['A1':'C3']):
        for cell in row:
                print(cell.coordinate, cell.value)
        print('--- END OF ROW ---')
        
#outputs following 
#A1 2015-04-05 13:34:02
#B1 Apples
#C1 73
#--- END OF ROW ---
#A2 2015-04-05 03:41:23
#B2 Cherries
#C2 85
#--- END OF ROW ---
#A3 2015-04-06 12:46:51
#B3 Pears
#C3 14
#--- END OF ROW ---

#---------------------------------------------------------------------
#Create/remove Sheet, save file ..
#---------------------------------------------------------------------
sheet = wb.worksheets[0]
sheet.max_row #returns max row, good for for iterations..

>>wb.get_sheet_names()
['Sheet']
>>sheet = wb.get_active_sheet()
>>sheet.title
'Sheet'
>>sheet.title = 'Spam Bacon Eggs Sheet' #Every time you change name you need to save file to "make it count"
>>wb.get_sheet_names()
['Spam Bacon Eggs Sheet']
>>wb.save('example_copy.xlsx') #Saves new changed file in example_copy.xlsx

>>wb.create_sheet()
<Worksheet Sheet1>
>>wb.get_sheet_names()
['Sheet','Sheet1']
>>wb.create_sheet(index=0,title = 'First Sheet')
<Worksheet "First Sheet">
>>wb.get_sheet_names()
['First Sheet','Sheet','Sheet1']
>>wb.remove_sheet(wb.get_sheet_by_name('Sheet'))
>>wb.get_sheet_names()
['First Sheet','Sheet1']
#---------------------------------------------------------------------
#Adding new content to tables..
#---------------------------------------------------------------------
>>sheet = wb.get_sheet_by_name('Sheet')
>>sheet['A1'] = 'Test' #Writes Test to A1 cell in 'Sheet'
>>sheet['A1'].value
'Test'


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
constantRegex.findall("Robocop eats baby food.BabyFood.")
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
#THIS IS INCORRECT WAY!
threadObj = threading.Thread(target=print('cats','dogs',sep=' & '))
#---------------------------------------------------------------------

#This is de wai xD
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
  -> https://i.imgur.com/nrr0rqh.png
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
