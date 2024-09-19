import os
import json
import platform

# Placeholder for subprocess if not available
def run_command(command):
    return f"Command '{command}' cannot be executed because the subprocess module is unavailable."

def netinfo():
    # Define the input and output file names
    input_file = 'Ifcfg.conf'
    output_file_txt = 'net_ifcfg.conf'
    output_file_json = 'net_ifcfg.json'
    
    # Read the Ifcfg.conf file and convert to a dictionary
    config_dict = {}
    with open(input_file, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=', 1)
                config_dict[key.strip()] = value.strip()

    # Modify specific parameters
    config_dict['onboot'] = 'yes'
    config_dict['bootproto'] = 'static'
    config_dict['defroute'] = 'no'

    # Add new entries
    config_dict['IPADDR'] = '192.168.1.100'  # Example IP Address
    config_dict['PREFIX'] = '24'  # Example subnet prefix

    # Write updated dictionary to the output files
    with open(output_file_txt, 'w') as file:
        for key, value in config_dict.items():
            file.write(f"{key}={value}\n")

    with open(output_file_json, 'w') as file:
        json.dump(config_dict, file, indent=4)

    # Determine the current operating system
    os_name = platform.system().lower()
    netinfo = {os_name: []}

    # Execute commands based on OS
    if os_name == 'linux':
        commands = ['ifconfig', 'netstat', 'nmcli general']
    elif os_name == 'windows':
        commands = ['powershell Get-NetRoute', 'powershell Get-NetIPAddress']
    else:
        print("Unsupported OS")
        return

    for cmd in commands:
        try:
            # Attempt to run the command
            result = run_command(cmd)  # Placeholder function
            netinfo[os_name].append(result)
        except Exception as e:
            netinfo[os_name].append(f"Error executing command '{cmd}': {str(e)}")

    # Append netinfo dictionary to existing JSON file
    if os.path.exists(output_file_json):
        with open(output_file_json, 'r+') as file:
            existing_data = json.load(file)
            existing_data.update(netinfo)
            file.seek(0)
            json.dump(existing_data, file, indent=4)
    else:
        with open(output_file_json, 'w') as file:
            json.dump(netinfo, file, indent=4)

# Run the function
if __name__ == "__main__":
    netinfo()
