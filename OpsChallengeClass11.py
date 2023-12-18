#!/usr/bin/env python3

# Script: Psutil
# Author: Renona Gay
# Date: 12/17/2023

 # This line installs psutil, which lets us see the proccesses happening inside the computer.
import psutil

# This line gets various system time from different ares of the computer using psutil

def get_system_times():

# A dictionary containing time stats for different processes in the computer.
system_times = {}

 # User time spent using everyday processes.
  system_times["user_normal"] = psutil.cpu_times().user

 # Time spent by processes in kernel mode
  system_times["system"] = psutil.cpu_times().system

# Time when system was idle
  system_times["idle"] = psutil.cpu_times().idle

# User time spent by really important (priority) processes (can't be done on all platforms).
  try:
    system_times["user_priority"] = psutil.cpu_times().user_nice
  except AttributeError:
    system_times["user_priority"] = None

 # Time spent waiting for I/O to complete.(I/O are kernel mode structures used by Windows Drive Model
 # and Windows NT device drives to communicate with each otehr and the OS.)   
  system_times["iowait"] = psutil.cpu_times().iowait

 # Time spent fixing hardware interrupts
  system_times["irq"] = psutil.cpu_times().irq

  # Time spent fixing software interrupts
  system_times["softirq"] = psutil.cpu_times().softirq

  # Time spent by other operating systems in a VM 
  if psutil.virtual_memory().vmalloc_used:

  # How many OS VMs that are running  
    system_times["guest"] = psutil.virtual_memory().vmalloc_used / psutil.cpu_freq()
  
  # If no VMs are running (0)
  else:
    system_times["guest"] = 0

  # Checking for time spent running a virtual CPU for guest OS (in Linux only)
  if psutil.LINUX:

    # Find how long the VM is spent being used
    try:
      system_times["guest_hypervisor"] = psutil.virtualization().guest_cpu_time() / psutil.cpu_freq()
   
   # No time spent using the VM
    except AttributeError:
      system_times["guest_hypervisor"] = 0

  # This line is for when the VM isn't being at all    
  else:
    system_times["guest_hypervisor"] = 0

  # Sends all the findings of all processes to this file.   
  return system_times

https://g.co/bard/share/c9a567743ef5