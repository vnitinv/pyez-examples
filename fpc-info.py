# Python PyEz script to collect the installed FPC hardware and show FPC status
__author__ = "Chris Booker"
import sys
from jnpr.junos import Device
from jnpr.junos.op.fpc import FpcHwTable
from jnpr.junos.op.fpc import FpcInfoTable
from getpass import getpass
from pprint import pprint as pp
from sys import exit
from lxml import etree


user = "lab"

print "\nPlease provide password for user '" + user + "' on device '" + sys.argv[1] + "'."
passwd = getpass()

dev = Device(sys.argv[1],user=user,password=passwd)
try:
  dev.open()
  print "Connected to " + sys.argv[1] + " as", (user)
except:
  print "Connection failed. :-("
  print "\n** Type exit() to quit **"


class style:
   BOLD = '\033[1m'
   END = '\033[0m'



#print FPC hardware Table
#get-chassis-inventory
print "\n*************************************************************************************"
print style.BOLD + "Chassis Installed FPC Details " + style.END
fpcs = FpcHwTable(dev)
fpcs.get()
print fpcs

for fpc in fpcs:
         print fpc.key," Description:", fpc.desc, "Model:", fpc.model,"Serial:", fpc.sn, "Part-number:", fpc.pn



#invoke get fpc information
print "\n*************************************************************************************"
print  style.BOLD + "Device FPC Status Details " + style.END 
jfpcs = FpcInfoTable(dev)
jfpcs.get()
print jfpcs
 
for item in jfpcs:
        print "Slot:", item.key,  "State:", item.state, "Memory Util%:", item.memory, "CPU%:", item.cpu 

dev.close()
