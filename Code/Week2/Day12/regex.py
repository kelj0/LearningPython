import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo= phoneNumRegex.search("My number is 123-213-2412")
print("Phone number found: " + mo.group())