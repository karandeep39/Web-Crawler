import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificates errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

f=open('myfile2.txt',"w")

url=input('Enter location: ')
print('Retrieving',url)
data=urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree=ET.fromstring(data)
lst=tree.findall('comments/comment')
#print(lst)

print('Count:',len(lst))
ct=[]
for item in lst:
    ct.append(int(item.find('count').text))
    #print(item.find('count').text)


print('Sum=',sum(ct))



f.writelines("%s\n" % data.decode())
    
    
f.close()



