#Website Blocker 
import time
from datetime import datetime as dt 

hosts_temp = r"C:\Users\jideo\hello\WebsiteBlocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.twitter.com","twitter.com"]

while True: #Checks for the statement True which is always Yes
    if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,4): #compares the time right now with the working range
        print("It's Working hours...")

        with open(hosts_temp,"r+")as file: #opens the host file
            content = file.read() #store the host file in content and read 
            #print(content)
            for website in website_list:
                if website in content: #if website already in content it passes and move forward
                    pass
                else:
                    file.write(redirect+" "+website+"\n") #if website is not in content, it adds it


    else:
        print("This is fun hours")

        with open(hosts_temp,"r+")as file: #opens the host file
            content = file.readlines() #store the host file in content and read
            #print(content)
            file.seek(0) #Takes the cursor back up
            for line in content:
                if not any(website in line for website in website_list): #Takes all the website in website list and checks it line by line in the content
                    file.write(line)
            file.truncate()



    
    time.sleep(5) #sleep the script for 5 seconds