my_list=[]
n=int(input("Enter number of element:"))
largest_num=my_list[0]
i=1
while i < len(my_list):
    if my_list[i]>largest_num:
        largest_num=my_list[i]
    i+=1
print("The largest number in the is:", largest_num)
