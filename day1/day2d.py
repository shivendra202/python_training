list1=[3,7,19,11,13,5,17]
#list 2= [3,7,19,11,13,]
list2 = [29, 23, 31]
print(list1+ list2)
print(list2>list1)

import sys
string = sys.argv
print(string)
numbers = [int(num) for num in string if num.isnumeric()]
print(numbers)
