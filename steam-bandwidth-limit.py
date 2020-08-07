# Set Steam download bandwidth limit (for Windows)

import argparse
from time import sleep

# Config
configpath = "C:\\Program Files (x86)\\Steam\\config\\config.vdf"
throttlestr = "DownloadThrottleKbps"

# Make the user at least see error messages when launched from a shortcut
# Please don't judge me for my lazy exceptions XD
try:
    # Parse bandwidth argument
    parser = argparse.ArgumentParser(description='Set Steam download bandwidth limit in Windows.')
    parser.add_argument('bandwidth', metavar='bandwidth', type=int, nargs=1,
            help='Bandwidth limit in Kbit/s. 0 = no limit.\n\
            Recommended use: create a shortcut to the script with bandwidth as first the argument.')
    args = parser.parse_args()
    bandwidth = args.bandwidth[0]

except:
    input('Press Enter to exit')
    exit()

try:
    # Open config file
    with open(configpath, 'r') as f:
        contents = f.readlines()
    
    # Find DownloadThrottleKbps line
    for n in range(len(contents)):                  # Loop over lines of config
        if throttlestr in contents[n]:              # Check for 'DownloadThrottleKbps'
            contents[n] = f'\t\t\t\t"{throttlestr}"\t\t"{bandwidth}"\n' # Replace line
            break                                   # Exit loop

    # Write new config to file file
    with open(configpath, 'w') as f:
        f.writelines(contents)

except:
    input(f'Error during file access of {configpath}\nPress Enter to exit')
    exit()

print(f'Steam bandwidth limit was set to {bandwidth} Kbit/s')
sleep(1)
