def menu(choice, config_key_list, config_dict, toggle):
    try :
        if choice == 1:
            print(f'| Seleceted parameter is {config_key_list[0]:130}|')
            config_dict[config_key_list[0]] = input("| Please enter new type of network: ")
        elif choice == 2:
            print(f'| Seleceted parameter is {config_key_list[1]:130}|')
            config_dict[config_key_list[1]] = input("| Please enter new interface of network: ")
        elif choice == 3:
            print(f'| Seleceted parameter is {config_key_list[2]:130}|')
            print(f'| Please Select a option from below{'':120}|')
            print(f'| 1) Yes\t2) No{'':134}|')
            config_dict[config_key_list[2]] = protocol_option(int(input('| Option: ')))
        elif choice == 4:
            print(f'| Seleceted parameter is {config_key_list[4]:130}|')
            config_dict[config_key_list[4]] = input("| Please enter new network protocol: ")
        elif choice == 5:
            print(f'| Seleceted parameter is {config_key_list[3]:130}|')
            print(f'| Please Select a option from below{'':120}|')
            print(f'| 1) Yes\t2) No{'':134}|')
            config_dict[config_key_list[3]] = protocol_option(int(input('| Option: ')))
        elif choice == 6:
            print(f'| Seleceted parameter is {config_key_list[5]:130}|')
            config_dict[config_key_list[5]] = input("| Please enter new Proxy Method: ")
        elif choice == 7:
            print(f'| Seleceted parameter is {config_key_list[6]:130}|')
            config_dict[config_key_list[6]] = input("| Please enter new name of device: ")
        elif choice == 8:
            print(f'| Seleceted parameter is {config_key_list[7]:130}|')
            config_dict[config_key_list[7]] = input("| Please enter new Slot of network: ")
        elif choice == 9:
            print(f'| Seleceted parameter is {config_key_list[8]:130}|')
            config_dict[config_key_list[7]] = input("| Please enter new UUID of network: ")
        elif choice == 10:
            print(f'| Seleceted parameter is {config_key_list[9]:130}|')
            config_dict[config_key_list[8]] = input("| Please enter new IPADDR: ")
        elif choice == 11:
            print(f'| Seleceted parameter is {config_key_list[10]:130}|')
            config_dict[config_key_list[9]] = input("| Please enter new PREFIX: ")
        elif choice == 12:
            print(f"| You have exited from parameter modification{'':110}|")
            toggle = False
        else:
            raise ValueError
    except ValueError:
        choice = int(input(f"| Please enter valid choice: "))
        choice,toggle = menu(choice, config_key_list, config_dict, toggle)
    return choice, toggle

def protocol_option(option):
    try:
        if option == 1:
            print(f'| You have selected "Yes"{'':130}|')
            val = 'yes'
        elif option == 2:
            print(f'| You have selected "No"{'':131}|')
            val = 'no'
        else:
            raise ValueError
    except ValueError:
        val = protocol_option(int(input("| Invalid option. Please enter valid option: ")))
    return val