# PYTHON

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
#'1'

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
