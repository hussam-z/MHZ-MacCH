#!/usr/bin/env python3

import subprocess

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

def the_inputs() :


    interface = input("{+} Enter The Interface Name => ")
    if not interface :
        print("\n{!} 00ps , you forget to enter the Interface Name , Run the tool again to enter it ...")
        exit()
    
    new_mac = input("{+} Enter The New Mac => ")
    if not new_mac :
        print("\n{!} 00ps , you forget to enter the New Mac , Run the tool again to enter it  ...")  
        exit()

    return (os , interface , new_mac)

##############################################

def the_changing(the_inputs_function) : 

    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

(interface , new_mac) =  the_inputs()
the_changing(the_inputs)


