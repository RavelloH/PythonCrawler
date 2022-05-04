## PornImgBot
## Author: RavelloH
## LICENSE: LGPL 2.1
## 使用第三方API

import urllib
from urllib.request import Request, urlopen, urlretrieve, urlopen, build_opener,ProxyHandler
import random
from wget import download
import time # 反反爬

url = "https://api.liitk.com/s/yepic/api.php?type=zrz"

# 构建循环
for i in range(0, 100):
    # UA库
    user_agent_list = [
        "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
        "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
        "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
    ]
    # 随机UA
    headers = {
        'User-Agent':random.choice(user_agent_list)## 随机抽取UA
    }
    # 随机IP
    ip_list = [
        '122.224.227.202:3128',
        '47.90.80.88:8080',
        '47.89.22.200:80',
        '183.95.80.102:8080',
        '123.160.31.71:8080',
        '115.231.128.79:8080',
        '166.111.77.32:80',
        '43.240.138.31:8080',
        '218.201.98.196:3128',


    ]
    # IP配置
    ip = {
        'http': random.choice(ip_list)
    }
    # 用ProxyHandler创建代理IP对象                   
    pro_han = ProxyHandler(ip)
    # 使用build_opener替代urlopen()创建一个对象
    opener = build_opener(pro_han)                   
    # 发送请求
    req = Request(url, headers = headers)
    res = opener.open(req)
    # 处理请求
    data = res.read()
    # 转换成字符串
    strs = str(data)
    # 截取字符串
    strs_for_json = strs[32: ]
    strs_for_json = strs_for_json[: -3]
    print(strs_for_json)
    # 保存到本地
    time.sleep(2)
    # download(strs_for_json)
    # 下载有问题，对应网站禁止下载
    
