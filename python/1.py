#!/usr/bin/python3

import requests
from termcolor import colored
from datetime import datetime


now = str(datetime.now())

url = 'http://localhost'
uri = '/login.php'
url = url + uri

param = '?doc=/bin/ls'
full_req: str= url + param
req = requests.get(full_req)
print(colored(full_req + "\nSending the request...", 'green'))

file = open("/var/log/usertest/user.log", "a+")
if req:
    print(colored('The rule is not correct. Please check...', 'red', attrs=['reverse', 'blink']))
    file.write(full_req + ' ' + now + " Try again! 1\n")
else:
    print(colored('The rule is correct!', 'blue', attrs=['reverse', 'blink']))
    file.write(full_req + ' ' + now +" Succeeded 1 \n")
file.close()
