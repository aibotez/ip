from lxml import etree
import time
import random
import  urllib.request


def testipp():


    def paqu(url, ip):
        list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        ader = random.choice(list)
        proxy_support = urllib.request.ProxyHandler({'http': ip})
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [('User-Agent', ader)]
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(url, timeout=4)
        html = response.read().decode('utf-8')
        return html



    #ipfile = input("http ip 文件 ")
    #ipfile = ipfile+'.txt'
    #ipfilet = input("校验后的ip输出文件 ")
    #ipfilet = ipfilet+'.txt'

    ipfile = 'httplist.txt'
    ipfilet = 'httplist-1.txt'

    with open(ipfile) as f:
        inf = f.read()
    ip = inf.split()
    lens = len(ip)
    lens = lens - 1  # https ip列表长度

    url = 'http://ip.tool.chinaz.com/'
    hp = 'http'
    i = 0  # i用来遍历整个ip列表
    i1 = 0  # i1用来判断所用ip是否为本机ip，如果是再次重新用该ip访问一次，如果依然是本机ip则不保留该ip
    i2 = 0  # i2用来捕获异常，连续两次都异常不保留该ip
    ipc = '114.96.193.198'

    while (i <= lens):
        try:
            print("目标ip", ip[i], "\t\t", i + 1, "/", lens + 1)
            res = paqu(url,ip[i])
            res = etree.HTML(res)
            reson = res.xpath('//dd/text()')
            rnip = reson[0]
            print("本机ip", ipc, "\t返回ip", rnip)
            if rnip != ipc:
                with open(ipfilet, 'a+') as f:
                    f.write(ip[i])
                    f.write('\n')
                i = i + 1
            if rnip == ipc:
                i1 = i1 + 1
                if i1 == 2:
                    i = i + 1
                    i1 = 0
        except:
            i2 = i2 + 1
            if i2 == 1:
                i = i + 1
                i2 = 0
            continue
    with open('httplist.txt','w')as f:
        f.write('')

    with open('httplist-1.txt') as f:
        inf = f.read()
    ip = inf.split()
    set0 = set(ip)
    li = list(set0)
    with open('httplist-1.txt', 'w')as f:
        for s in li:
            f.write(s)
            f.write('\n')

