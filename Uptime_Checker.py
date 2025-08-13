import os
from datetime import datetime
with open("Uptime_Targets.txt") as f: #i have a text file with ip of my home router and home pc. Replace with your filename or can ignore this section if you want to hardcode ips
  list = f.read()
  list = list.splitlines()
  print(f" {list} \n")  #prints the ips just to check

for ip in list:
  response = os.popen(f"ping -c 4 {ip} ").read() # each ip is pinged 4 times
 # response ="Request timed out."  Testing that if its down  it is logged
  if("Request timed out." or "unreachable") in response:
    print(response)
    message = f"{str(ip)} Home router is down at: {datetime.now()}\n"
    ff = open("Uptime_Log.txt","a") #Time of check is logged as well so i can keep track of when checks are made
    ff.write(message)
    ff.close() 
    print(message)
  else:
    print(response)
    ff = open("Uptime_Results.txt","a")
    ff.write(f"{str(ip)} Router is still up and running at: {datetime.now()}\n")
    ff.close()
    print(str(ip)+" Router is still up and running\n")
