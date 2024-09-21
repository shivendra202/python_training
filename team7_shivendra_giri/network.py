import os
import platform
import json
import subprocess
from network_choice import menu

def netinfo():
    netinfo_dict = {}

    config_file = 'ifcfg.conf'
    new_config_file = 'net_ifcfg.conf'
    json_file = 'net_ifcfg.json'
    print('|','-'*152,'|')

    if not os.path.exists(config_file):
        print('|',' '*152,'|')
        print(f"| Configuration file {config_file} does not exist.{'':107}|")
        print('|',' '*152,'|')
        print('|','-'*152,'|')
        return

    with open(config_file, 'r') as file:
        lines = file.readlines()
        print('|',' '*152,'|')
        print(f"| Network parameters are read successfully....{'':109}|")
        print('|',' '*152,'|')
        print('|','-'*152,'|')

    config_dict = {}
    for line in lines:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            config_dict[key.strip()] = value.strip()

    config_dict['IPADDR'] = input("| Enter the IP Address: ")
    config_dict['PREFIX'] = int(input("| Enter Subnet value: "))
    
    toggle = True
    while toggle:
        toggle = modify(config_dict, toggle)

    with open(new_config_file, 'w') as file:
        for key, value in config_dict.items():
            file.write(f'{key}={value}\n')
        print('|','-'*152,'|')
        print('|',' '*152,'|')
        print(f"| Network parameters are modified successfully....{'':105}|")
        print('|',' '*152,'|')
        print('|','-'*152,'|')

    with open(json_file, 'w') as file:
        json.dump(config_dict, file, indent=4)
    os_name = platform.system().lower()
    netinfo_dict[os_name] = []

    if os_name == 'linux':
        commands = ['ip addr', 'netstat', 'nmcli gen']
        print(f'| This Operating System is {os_name:130}')
    elif os_name == 'windows':
        commands = ['powershell Get-NetRoute', 'powershell Get-NetIPAddress']
        print(f'| This Operating System is {os_name:127}')
    elif os_name == 'darwin': 
        commands = ['ifconfig', 'networksetup -listallhardwareports','pwd','ls']
        print(f'| This Operating System is {os_name}(Mac){'':117}|')
    else:
        print(f"Unsupported operating system: {os_name}")
        return
    print('|',' '*152,'|')
    print(f'| Command executed are:{'':132}|')
    print('|',' '*152,'|')
    for command in commands:
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            netinfo_dict[os_name].append(result)
            print(f'| {command:60} executed successfully....{'':66}','|')
        except subprocess.CalledProcessError as e:
            print(f"Error executing command '{command}': {e}")
    print('|',' '*152,'|')
    
    try:
        with open(json_file, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(netinfo_dict)

    with open(json_file, 'w') as file:
        json.dump(existing_data, file, indent=4)
        print('|','-'*152,'|')
        print('|',' '*152,'|')
        print(f'| Data stored successfully in {json_file:125}|')
        print('|',' '*152,'|')
        print('|','-'*152,'|')

def modify(config_dict, toggle):
        config_key_list = list(config_dict.keys())
        print('|','-'*152,'|')
        print('|',' '*152,'|')
        print(f"| Please choose the network parameter to update{'':108}|")
        print("| ",end='')
        for i in range(len(config_key_list)):
            print(f'{i+1}) {config_key_list[i]}',end='   ')
        print("12) Exit   |")
        choice = int(input('| Your choice: '))
        choice, toggle = menu(choice,config_key_list, config_dict, toggle)
        return toggle
        

netinfo()