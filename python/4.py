#!/usr/bin/python3

import requests
from termcolor import colored
from datetime import datetime

url = 'http://localhost'
uri = '/vulnerabilities/fi/'
param = '?page=/../../../'
now = str(datetime.now())
full_req: str= url + uri + param
headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'test'
    }
)
req = requests.get(full_req, headers=headers)
print(colored(full_req + "\nSending the request...", 'green'))

file = open("/var/log/usertest/user.log", "a+")
if req:
    print(colored('The rule is not correct. Please check...', 'red', attrs=['reverse', 'blink']))
    file.write(full_req + ' ' + now + " FAILED!\n")
else:
    print(colored('The rule is correct!', 'blue', attrs=['reverse', 'blink']))
    file.write(full_req + ' ' + now +" OK!\n")
file.close()
