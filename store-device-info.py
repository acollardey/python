#!/usr/bin/python3

# This python script captures android device data to stores it into a spreadsheet (TBD).

import subprocess

# capture, decode, and store device info into a string variable
device_info = subprocess.check_output("adb devices -l",shell=True)
device_info = bytes.decode(device_info)

# capture, decode, and store device screen resolution into a string variable
device_resolution = subprocess.check_output("adb shell wm size",shell=True)
device_resolution = bytes.decode(device_resolution)

# isolate device serial number
device_serial = device_info[25:41]

# find and isolate device model
word = "model"
device_model = device_info.find(word)
word = "device:"
device_device = device_info.find(word)
device_model_final = device_info[(device_model+6):(device_device-1)]

#find and isolate device screen resolution
word = "Pyhsical size:"
device_physical_size = device_resolution.find(word)
word = "Override size:"
device_override_size = device_resolution.find(word)
device_screen_resolution = device_resolution[(device_physical_size+16):(device_override_size-1)]

#insert data into spreadhseet
