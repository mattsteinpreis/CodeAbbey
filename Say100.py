__author__ = 'matt'


import requests
import re

data = {"token" : "vlXg/IE/Kt4s81q4WEwMNzU4"}
#token = raw_input()
#data = {"token": token}


myurl = "http://codeabbey.sourceforge.net/say-100.php"

r = requests.post(myurl, data = data)
secret = re.findall(("[0-9]{1,2}"), r.content)[0]
answer = str(100-int(secret))
data['answer'] = answer

r = requests.post(myurl, data = data)
end_token = re.findall("end: (.*)$", r.content)[0]
print end_token[:-1]