'''
HTTP Reuests has following parameters:
1)Request URL
2)Header Fields
3)Parameter
4)Request body
'''
#!/usr/bin/env python

import requests
import json

GITHUB_API="https://api.github.com"
API_TOKEN='51e142e3665cd21741865226abd8f3881f234059'

#form a request URL
url=GITHUB_API+"/gists"
print("Request URL: %s"%url)

#print headers,parameters,payload
headers={'Authorization':'token %s'%API_TOKEN}
params={'scope':'gist'}
#payload={"description":"GIST created by python code","public":True,"files":{"python request module":{"content":"Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"}}}
payload={}

#make a requests
res=requests.get(url,headers=headers,params=params,data=json.dumps(payload))

#print response --> JSON
print(res.status_code)
print(res.url)
print(res.text)
j=json.loads(res.text)


print(j)