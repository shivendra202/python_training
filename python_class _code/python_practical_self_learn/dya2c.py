import sys
def split_states_capitals():
    states = []
    capitals=list()
    for i in range(1, len(sys.argv)):
        argument = sys.arvg[i]
        index_of_space=argument.find('')
        states.append(argument[:index_of_space])
        capitals.append(argument[index_of_space +1:])
        print('%-15s %s'%('STATES' , 'CAPITALS'))
        print('-' * 27)
        i-0
        while states:
            