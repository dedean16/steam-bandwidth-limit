# steam-bandwidth-limit
Set a custom Steam bandwidth limit with a shortcut.

The Steam bandwidth limit can be set to any value by adjusting the *DownloadThrottleKbps* in *C:\Program Files (x86)\Steam\config\config.vdf*. This script does that for you, so you don't need to redo it manually everytime the setting gets overwritten. Recommended use: create a shortcut to the script with the bandwidth in Kbit/s as first the argument.

Example: To set a bandwidth limit of 4.5MB/s, in the shortcut's properties, edit the Target of the shortcut as: *C:\path\to\bandwidth-limit-script.py 36000*

Note 1: Close Steam before running this.

Note 2: I hardcoded the path to C:\Program Files (x86)\Steam\config\config.vdf, so change that line of code if you've installed Steam to a custom location.

Note 3: I used f-strings so you need Python 3.6 or higher.
