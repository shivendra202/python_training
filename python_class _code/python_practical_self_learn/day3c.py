sweets = input('Enter few sweets(space seperated):').split()
sweets_set= set(sweets)
sweets_fset = frozenset(sweets)
sweets_dict={name:len(name) for name in sweets_fset}
print(f'Original List : {sweets}')
print(f'Set of sweets (No duplicates):{sweets}')
print(f'Frozen set:{sweets_fset}')
print(f'Dictionary of sweets:{sweets_dict}')
import json
with open('sweets2.json','w')as fptr:
    json.dump(sweets_dict, fptr)
    print('Dictionary of sweets writen to file')
    with open('sweets2.json','r')as fptr:
        sweets=json('sweets1.json','r')as fptr:
    #sweets=json.load(fptr)
    print('Dictionary of sweets writen to file')
print(f'Words:{words_tupple}')