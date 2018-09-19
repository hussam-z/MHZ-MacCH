#!/usr/bin/env python3

import subprocess
import re
import time
import sys

##############################################
 
print("""
    	 __  __ _    _ ______     __  __             _____ ______
     	|  \/  | |  | |___  /    |  \/  |           / ____| |  | |
 	| \  / | |__| |  / ______| \  / | __ _  ___| |    | |__| |
 	| |\/| |  __  | / |______| |\/| |/ _` |/ __| |    |  __  |
 	| |  | | |  | |/ /__     | |  | | (_| | (__| |____| |  | |
 	|_|  |_|_|  |_/_____|    |_|  |_|\__,_|\___|\_____|_|  |_|


			Welcome To MHZ-MacCH
			   created by : 
		  {*} Moammad Hussam Alzeyyat {*}
		      {*} bash_shabakate {*}

				FB :
	   https://www.facebook.com/muhammedhusam.alzeyyat.9
			     Github : 
		     https://github.com/hussam-z


Usage : 
	
	1- Enter the Interface name
	2- Enter the new Mac Address
.............................................................

""")

##############################################

def check_os_type():
    
    if sys.platform != "linux" :
        type(sys.platform)
        print('[!] 00ps , you can not use this tool on {} , it is for Linux only ...'.format(sys.platform)) 
        time.sleep(5)
        exit()
##############################################

def the_inputs() :


    interface = input("{+} Enter The Interface Name => ")
    if not interface :
        print("\n{!} 00ps , you forget to enter the Interface Name , Run the tool again to enter it ...")
        exit()
    
    global new_mac # make the new_mac global to compare with him if the mac changed in the bottom
    new_mac = input("{+} Enter The New Mac => ")
    if not new_mac :
        print("\n{!} 00ps , you forget to enter the New Mac , Run the tool again to enter it  ...")  
        exit()

    return (interface , new_mac)


##############################################

def the_changing(the_inputs_function) : 

    subprocess.call(["ifconfig",interface,"down"]) # the commands to change the mac address
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

##############################################

def check_current_mac(interface_input) : 

    ifconfig_result = subprocess.check_output(["ifconfig",interface]) # to check out the output of 'ifconfig' command
    re_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result)) # regular expression to take the mac address only

    if re_result : # if there are mac address 
        return re_result.group(0)
    else:
        print("{-} Could not read mac address .. !")

##############################################


check_os_type() # to check the os if it linux or another os

(interface,new_mac) = the_inputs()

current_mac = check_current_mac(the_inputs)
print("\n{+} The current mac --> " + str(current_mac))


the_changing(the_inputs)

time.sleep(10) # the sleep here to be sure the system take its time to change the mac address

current_mac = check_current_mac(the_inputs)
if current_mac == new_mac :
    
    print("\n{*} The mac address changing process completed.")

else:
    print("\n{!} Sorry the mac address does not change ... !")
    print("{*} Try a different mac address ...")

