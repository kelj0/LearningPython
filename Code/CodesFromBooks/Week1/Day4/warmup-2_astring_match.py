#!/usr/bin/python3
def string_match(a, b):
  counter =0
  if len(a)>len(b):
    c=b
  else:
    c=b
  for i in range(0,len(c)-1):
    if(len(a)==i or len(b)==i):
      break
    elif (a[i]==b[i]) and (a[i+1]==b[i+1]):
      counter+=1
  return counter

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))