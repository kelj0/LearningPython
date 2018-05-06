def string_match(a, b):
  for i in range(0,len(a)-1):
      print(i,a[i+1]==b[i+1])
  


string_match('abc', 'abc')
string_match('abc', 'axc')