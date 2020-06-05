import requests,lxml.html
from lxml import etree
agents=['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36']
#for loop checks all the corresponding agents for Error message and which user agents can be used to other users laptops
for a in agents:
    agent={"User-Agent":a}
    url='https://www.justdial.com/'+'Mumbai'+'/Provision-Stores'+'/page-'+'23'
    html=requests.get(url,headers=agent)
    #print(html.content)
    tree = lxml.html.fromstring(html.content)
    flag=False
    a=(tree.findtext('.//title'))
    #print(a)
    if a=='Error':
        flag=flag or True   
    print(flag)
#print(type(html.content))
    
