import sys
string = sys.argv
print(string)
numbers = [int(num) for num in string if num.isnumeric()]
print(numbers)
