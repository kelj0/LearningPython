#!/usr/bin/python3
#!/usr/bin/python3
import re

password=input("Enter your password:")


passwordNUMRegex = re.compile(r'\d+')
passwordCHARRegex= re.compile(r'\w+')

has_char=False
has_num=False
has_upper=False

for i in password:
    if passwordCHARRegex.search(i)!=None:
        has_char=True
    if passwordNUMRegex.search(i)!=None:
        has_num=True
    if str(i).isupper():
        has_upper=True


if has_char and has_num and has_upper:
    print("Your password is good")
else:
    print("Bad password")


