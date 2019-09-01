# *_*coding:utf-8 *_*
import requests
from bs4 import BeautifulSoup
target='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/42/06/84/420684001.html'
req = requests.get(url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/42/06/84/420684001.html')
html=req.text.encode("iso-8859-1").decode('gb18030')
#print(html)
tr_bf = BeautifulSoup(html,"lxml")
#print(tr_bf)
tr = tr_bf.find_all('tr', class_='villagetr')
#print(tr)
td_bf = BeautifulSoup(str(tr),"lxml")
td = td_bf.find_all('td')
print(td)
nums=int(len(td)/3)
#print(nums)
names=[]
#urls=[]
#courls=[]
names1=[]
for each in td:
    names.append(each.text)
    #courls.append(each.get('href'))
for i in range(3*nums):
    print(names[i])
#courls = sorted(set(courls))
#for i in range(nums):
    #print(courls[i])

for i in range(0,nums*3,3):
    names1.append(names[i]+ '  ' +names[i + 1]+ '  ' +names[i + 2])
for i in range(0,int(nums)):
    print(names1[i])
    #urls.append(target.replace('.html', '/', 1)[0:-7] + courls[i])
    #print(urls[i])
