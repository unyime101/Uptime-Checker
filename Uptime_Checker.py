import os
from datetime import datetime
with open("Uptime_Targets.txt") as f: #i have a text file with ip of my home router and home pc. Replace with your filename or can ignore this section if you want to hardcode ips
  list = f.read()
  list = list.splitlines()
  print(" {list} \n")  #prints the ips just to check

  for ip in list:
    response = os.popen(f"ping -c 4 {ip} ").read() # each ip is pinged 4 times
    if("Request timed out." or "unreachable") in response:
    print(response)
    ff = open("Uptime_Results.txt","a")
    f.write(str(ip) + ' link is down at:'+'\n')
    ff.close() 
