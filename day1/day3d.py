# Sample list
my_list = ['apple', 'banana', 'cherry', 'date']

# Display the original list
print("Original list:", my_list)

# Take input for the value to replace and the new value
old_value = input("Enter the value to replace: ")
new_value = input("Enter the new value: ")

# Check if the old value exists in the list and replace it
if old_value in my_list:
    my_list = [new_value if item == old_value else item for item in my_list]
    print("Updated list:", my_list)
else:
    print(f"Value '{old_value}' not found in the list.")
