import json
import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore SSL certificates errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

f=open('myfile3.txt',"w")

url=input('Enter location: ')
print('Retrieving',url)
data=urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
info=json.loads(data)
#print('Count:',len(info))
#print(info)
#print(type(info))
ct=[]
for item in info["comments"]:
    ct.append(int(item["count"]))
    
    
print('Count:',len(ct))
print('Sum=',sum(ct))



f.writelines("%s\n" % data.decode())
    
    
f.close()


