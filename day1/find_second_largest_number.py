my_list = [5, 12, 7, 19, 3, 8, 10]
largest_num = my_list[0]
second_largest = None
i = 1
while i < len(my_list):
    if my_list[i] > largest_num:
        second_largest = largest_num
        largest_num = my_list[i]
    elif my_list[i] > second_largest or second_largest is None:
        second_largest = my_list[i]
    i += 1
print("The second largest number in the list is:", second_largest)