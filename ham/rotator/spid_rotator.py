
#This is a test program for the Alfaspid RAK controller and
#is written in Python 2.7

#The program was written for demonstration purposes only and as
#a template for users to fashion any custom software project
#they may be attempting.

#Before using this program, the user must:
#   1.  Install python2 followed by the pyserial module on the computer to
#       be used.
#   2.  Install and set-up the RAK Rotator and Controller in accordance
#       with the Alfaspid RAK Manual and ensure that it is working with the
#       manual controls on the controller.
#   3.  Obtain a controller program such as ham Radio Deluxe or N1MM to
#       confirm that the RS232 or USB connection between the Computer
#       and Controller are fully functional.

#Obtain a copy of file "Program_format-Komunicacji-2005-08-10.pdf"
#from the Alfaradio website to fully understand this program.

#This program was developed on a DELL 610 Laptop with Windows XP and
#tested on a computers running Windows 7, Debian Linux and OSX 10.10

#No warranty is stated nor implied by Alfaradio for this program's use.


# required libraries
import serial
import time
import os
from time import sleep





# get the Comm Port information
#input_variable = raw_input ("Enter comm port: (Default /dev/cu.usbserial-A104FZJ8 ")
#if len(input_variable) < 5:
input_variable="/dev/cu.usbserial-A104FZJ8"

port = (input_variable)
# define constants.
loop = 1
zero5 = chr(0)+chr(0)+chr(0)+chr(0)+chr(0)

print ("Enter 888 to stop rotation.")
print ("Enter 999 to update rotator status.")
print ("Enter 987 to quit program.")

#Open Comm Port
ser = serial.Serial(port, 9600, timeout = 0)

while loop == 1:

   #Get desired azimuth
   print (" ")
   input_variable = eval(input ("Enter azimuth: "))
   az = int(input_variable)

   if az == 888:
      # Build the stop command word.
      out = chr(87)+zero5+zero5+chr(15)+chr(32)
      x = ser.write(bytes(out.encode('utf-8')))
      # Wait for answer from controller
      sleep (0.5)

      data = ser.read(9999)
	  # once all 5 characters are received, decode location.
      if len(data) >= 5:
         s1 = ord(data[1].encode('latin-1'))
         s2 = ord(data[2].encode('latin-1'))
         s3 = ord(data[3].encode('latin-1'))
         azs = s1*100 + s2*10 + s3
	 # Since the controller sends the status based on 0 degrees = 360
         # remove the 360 here
         azs = azs - 360
         print(("Rotator stopped at %3d " %(azs)+ "Degrees"))


   elif az == 999:
      # Build the status command word.
      out = chr(87)+zero5+zero5+chr(31)+chr(32)
      x = ser.write(bytes(out.encode('utf-8')))
      # Wait for answer from controller
      sleep (0.5)

      data = ser.read(9999)
      # once all 5 characters are received, decode location.
      if len(data) >= 5:
         s1 = ord(data[1].encode('latin-1'))
         s2 = ord(data[2].encode('latin-1'))
         s3 = ord(data[3].encode('latin-1'))
         azs = s1*100 + s2*10 + s3
         # Since the controller sends the status based on 0 degrees = 360
         # remove the 360 here
         azs = azs - 360
         print(("Rotator currently at %3d " %(azs)+ "Degrees"))

   elif az == 987:
      # Program is ending so escape the loop.
      loop = 0

   else:    # send command to rotator controller to move rotator
            # to the desired azimuth.

      #test to see if azimuth is in the range of 0 to 360 Degrees
      if (az < 0 or az > 360):
          print ("Invalid Azimuth")
      else:
         #Convert Azimuth to number required by controller
         az = az + 360
         # Build message to be sent to controller
         out = chr(87)+str(az)+chr(48)+chr(1)+zero5+chr(47)+chr(32)
         #Send message to Controller
         x = ser.write(bytes(out.encode('utf-8')))


#In [6]: ser = serial.Serial(
#    port='/dev/cu.usbserial-A104FZJ8',
#    baudrate=9600,
#    parity=serial.PARITY_ODD,
#    stopbits=serial.STOPBITS_TWO,
#    bytesize=serial.SEVENBITS
#)
#
#In [7]: ser.isOpen()
#Out[7]: True
#
#In [8]:  ser.flushInput()
#
#In [9]:  ser.flushOutput()