import os
import time
import datetime
import http.client

conn = http.client.HTTPConnection("142.251.141.46") #nslookuup google.com ip addr
message = '''
*******************************************************************************************
___________              .__        __   
\_   _____/__  __________|__|______/  |_ 
 |    __)_\  \/  /\_  __ \  \____ \   __\
 |        \>    <  |  | \/  |  |_> >  |  
/_______  /__/\_ \ |__|  |__|   __/|__|  
        \/      \/          |__|         
'''

headers = { "Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain" }

print("Running...")
def print_arp_table(conn, message, headers):
    current_time = datetime.datetime.now().time()
    arp_table = os.popen("arp -a").read()
    mac_list = []
    print("Safe ^_^")
    for line in arp_table.split("\n"):
        if "dynamic" in line:
            ip = line.split()[0]
            mac = line.split()[1]

            if mac in mac_list:
                print("Danger detected!!!  X_X")
                conn.request("POST", "", message.encode('utf-8'), headers)
                response = conn.getresponse()
                print(response.status, response.reason)
                print(current_time)
                print("IP adresi : " + ip)
                conn.close()
                break
            else:

                mac_list.append(mac)
while True:
    print_arp_table(conn,message,headers)
    time.sleep(5)
