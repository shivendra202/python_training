"""'Goa Panjim' 'Andhra Amaravati' 'Kerala Tiruvanantapuram' 'Himachal Shimla'"""

import sys
def split_states_capitals():
    states=[]
    capitals=list()
    for i in range(1,len(sys.argv)):
     arguments = sys.argv[i].split()
     states.append(arguments[0])
     capitals.append(arguments[1])
states = []
capitals = list()
for i in  range(1, len(sys.argv)):
    arguments  =sys.argv[i]
    argumrnt = arguments.split()
    states.append(arguments[0])
    capitals.append(arguments[1])
    print (states)
    print (capitals)
