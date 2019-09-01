# *_*coding:utf-8 *_*
import requests
from bs4 import BeautifulSoup
import sys
"""
类说明：爬取中国统计局2016年全国各省份城市划分准则及其统计编号
parameters：无
Returns：无
Modify：2018-6-14
注：频繁点击网页的链接可能会导致网页的崩溃从而没有办法实现输出，
而在尝试后，发现在county level设置一个输出可以降低访问网页链接的速度，但同时也增加了程序运行时间
"""

class Inf_Province(object):
    def __init__(self):
        self.serve='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'
        self.target='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html'
        self.pnames=[]
        self.cinames=[]
        self.conames=[]
        self.tnames=[]
        self.vnames=[]
        self.cinames1 = []
        self.conames1 = []
        self.tnames1 = []
        self.purls=[]
        self.ciurls=[]
        self.courls=[]
        self.turls=[]
        self.vurls=[]
        self.pnums=0
        self.cinums=0
        self.conums=0
        self.tnums=0
        self.vnums=0
    """
    函数说明：爬取省份信息以及它的超链接
    Parameters：无
    Returns：无
    Modify：2018-6-14
    """
    def get_province(self):
        req = requests.get(self.target)
        html = req.text.encode("iso-8859-1").decode("gb18030")
        tr_bf = BeautifulSoup(html,"lxml")
        tr = tr_bf.find_all('tr', class_='provincetr')
        a_bf = BeautifulSoup(str(tr),"lxml")
        a = a_bf.find_all('a')
        self.pnums=len(a)
        for each in a:
            self.pnames.append(each.text)
            self.purls.append(self.serve+each.get('href'))

    """
    函数说明：爬取城市信息包括名字和统计代码，以及它的超链接
    Parameters：target-下载链接(string)
    Returns：无
    Modify：2018-6-14
    """
    def get_city(self,target):
        req = requests.get(url=target)
        html = req.text.encode("iso-8859-1").decode("gb18030")
        tr_bf = BeautifulSoup(html,"lxml")
        tr = tr_bf.find_all('tr', class_='citytr')
        a_bf = BeautifulSoup(str(tr),"lxml")
        a = a_bf.find_all('a')
        self.cinums = int(len(a)/2)
        for each in a:
            self.cinames.append(each.text)
            self.ciurls.append(each.get('href'))
        self.ciurls = sorted(set(self.ciurls))
        for i in range(0,len(a),2):
            self.cinames1.append(self.cinames[i] + '  ' + CN.cinames[i+1])

    """
    函数说明：爬取县区信息包括名字和统计代码，以及它的超链接
    Parameters：target-下载链接(string)
    Returns：无
    Modify：2018-6-14
    """
    def get_county(self,target):
        req = requests.get(url=target)
        html = req.text.encode("iso-8859-1").decode("gb18030")
        tr_bf = BeautifulSoup(html,"lxml")
        tr = tr_bf.find_all('tr', class_='countytr')
        a_bf = BeautifulSoup(str(tr),"lxml")
        a = a_bf.find_all('a')
        self.conums = int(len(a)/2)
        for each in a:
            self.conames.append(each.text)
            self.courls.append(each.get('href'))
        self.courls = sorted(set(self.courls))
        for i in range(0,len(a),2):
            self.conames1.append(self.conames[i] + '  ' + CN.conames[i+1])

    """
        函数说明：爬取办事处信息包括名字和统计代码，以及它的超链接
        Parameters：target-下载链接(string)
        Returns：无
        Modify：2018-6-14
        """
    def get_town(self, target):
        req = requests.get(url=target)
        html = req.text.encode("iso-8859-1").decode("gb18030")
        tr_bf = BeautifulSoup(html,"lxml")
        tr = tr_bf.find_all('tr', class_='towntr')
        a_bf = BeautifulSoup(str(tr),"lxml")
        a = a_bf.find_all('a')
        self.tnums = int(len(a)/2)
        for each in a:
            self.tnames.append(each.text)
            self.turls.append(each.get('href'))
        self.turls = sorted(set(self.turls))
        for i in range(0,len(a),2):
            self.tnames1.append(self.tnames[i] + '  ' + CN.tnames[i+1])

    """
        函数说明：爬取居民委员会信息包括名字和统计代码
        Parameters：target-下载链接(string)
        Returns：无
        Modify：2018-6-14
        """
    def get_village(self, target):
        req = requests.get(url=target)
        html = req.text.encode("iso-8859-1").decode("gb18030")
        tr_bf = BeautifulSoup(html,"lxml")
        tr = tr_bf.find_all('tr', class_='villagetr')
        td_bf = BeautifulSoup(str(tr),"lxml")
        td = td_bf.find_all('td')
        self.vnums = int(len(td))
        for each in td:
            self.vnames.append(each.text)
    """
    函数说明:将爬取的信息写入文件
    Parameters:
        name - 
    Returns:
        无
    Modify:
        2017-09-13
    """
    """
    待定，暂时先不定义输出函数
    def writer(self, name, path):
        write_flag = True
        with open(path, 'a') as f:
            f.write(name+'\n')
    """
if __name__=="__main__":
    CN=Inf_Province()
    CN.get_province()
    print('爬虫开始！')
    """for i in range(CN.pnums):
        print(CN.pnames[i])
        print(CN.purls[i])"""
    with open(u'贵州.txt','a') as f:
        for i in range(23,24): # 31个省份的循环
            f.write('\n\n------------------省份分割线------------------\n')
            f.write(CN.pnames[i]+'\n') # 北京
            print(CN.pnames[i])
            p_target = CN.purls[i]
            #print(p_target)
            CN.get_city(p_target)  # 北京的市的链接
            for j in range(3,9):
                f.write('    '+CN.cinames1[j]+'\n') # 第一个：直辖区
                print(CN.cinames1[j])
                ci_target=p_target.replace('.html','/')[0:-3]+CN.ciurls[j]
                CN.get_county(ci_target) # 直辖区的区的链接
                #print(ci_target)
                for k in range(CN.conums):
                    f.write('        '+CN.conames1[k]+'\n') # 第一个：东城区
                    print(CN.conames1[k])
                    co_target=ci_target.replace('.html','/',1)[0:-5]+CN.courls[k]
                    CN.get_town(co_target)
                    #print('  '+co_target)# 东城区的所有街道办事处链接
                    for l in range(CN.tnums):
                        f.write('            '+CN.tnames1[l]+'\n')# 输出所有街道办事处
                        #print(CN.tnames1[l])
                        t_target=co_target.replace('.html','/',1)[0:-7]+CN.turls[l]
                        CN.get_village(t_target)
                        #print(t_target)
                        for m in range(0,CN.vnums,3):
                            f.write('                '+CN.vnames[m]+'  '+CN.vnames[m+1]+'  '+CN.vnames[m+2]+'\n') # 输出所有居委会
                        CN.vnames.clear()
                    CN.tnames1.clear()
                    CN.tnames.clear()
                    CN.turls.clear()
                CN.conames1.clear()
                CN.conames.clear()
                CN.courls.clear()
            CN.cinames1.clear()
            CN.cinames.clear()
            CN.ciurls.clear()
    print('爬虫结束！')
del(CN)










