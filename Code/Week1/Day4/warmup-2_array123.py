def array123(nums):
   i=0
   while i<len(nums):
    array=nums[i:i+3]
    if i==len(nums)-2:
      break
    elif array[0]==1 and array[1]==2 and array[2]==3:
      return True
    i+=1
   return False
print(array123([1,1,2,3,1]))
print(array123([1,1,2,4,1]))
print(array123([1,1,2,1,2,3]))