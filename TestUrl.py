import requests


target = "http://www.dstex.cn/"
file = open("fingerprint")
for line in file:
    url = target + line
    print(url.strip())
    res = requests.get(url.strip())
    print("["+str(res.status_code)+"]"+line.strip())
file.close()