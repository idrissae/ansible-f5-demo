
import requests, json
import json


bigip_address= "172.16.43.20"
bigip_admin= "admin"
bigip_password= "Idri$$2020"


url = 'https://172.16.45.20/mgmt/tm/ltm/pool'


r = requests.get(url, auth= (bigip_admin,bigip_password), verify=False)
resp = r.json()
#print(r.status_code)
#print(r.text)
for item in resp["items"]:
    print (item["fullPath"])
    print ("********************")