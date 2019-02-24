#利用代理的IP去请求网页，爬取内容
import  urllib.request
import random
import  time
from lxml import etree
def paquip():
    def paip(url, hp, ip):
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
        proxy_support = urllib.request.ProxyHandler({hp: ip})
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [('User-Agent', ader)]
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(url, timeout=5)
        html = response.read().decode('utf-8')
        return html

    with open('源ip.txt') as f:
        ip = f.read()
    ip = ip.split()
    i = 1
    #max = input("输入xici爬取最大页码 ")
    max = 50
    max1 = 10
    max1 = int(max1)
    max = int(max)

    print("开始爬取快代理")
    i = 1
    while i <= max1:
        try:
            print("开始第", i, "轮抓取")
            ips = []
            ipp = []
            i = str(i)
            url = 'https://www.kuaidaili.com/ops/proxylist/' + i
            i = int(i)
            IP = random.choice(ip)
            print("目标ip ", IP)
            res = paip(url, 'https', IP)
            res = etree.HTML(res)
            reson = res.xpath('//td/text()')
            j = 0
            for s in reson:
                if s == 'HTTP, HTTPS' and reson[j-1]!='透明':
                    ips.append(reson[j - 3] + ':' + reson[j - 2])
                if s == 'HTTP' and reson[j-1]!='透明':
                    ipp.append(reson[j - 3] + ':' + reson[j - 2])
                j = j + 1
            print("第", i, "轮抓取成功")
            # print(i,'\t',"https")
            # for s in ips:
            #   print(s)
            # print("http")
            # for s in ipp:
            #   print(s)
            with open('httplist.txt', 'a+') as f:
                for s in ipp:
                    f.write(s)
                    f.write('\n')
            with open('httpslist.txt', 'a+') as f:
                for s in ips:
                    f.write(s)
                    f.write('\n')
            i = i + 1
            time.sleep(1)
        except:
            continue

    print("快代理网抓取完毕")
    print("开始爬取xici网")
    i = 1
    while i <= max:
        try:
            print("开始第", i, "轮抓取")
            ips = []
            ipp = []
            i = str(i)
            url = 'https://www.xicidaili.com/nn/' + i
            i = int(i)
            IP = random.choice(ip)
            print("目标ip ", IP)
            res = paip(url, 'https', IP)
            res = etree.HTML(res)
            reson = res.xpath('//td/text()')
            j = 0
            for s in reson:
                if s == 'HTTPS'and reson[j-1]!='透明':
                    ips.append(reson[j - 5] + ':' + reson[j - 4])
                if s == 'HTTP'and reson[j-1]!='透明':
                    ipp.append(reson[j - 5] + ':' + reson[j - 4])
                j = j + 1
            print("第", i, "轮抓取成功")
            # print(i,'\t',"https")
            # for s in ips:
            #   print(s)
            # print("http")
            # for s in ipp:
            #   print(s)
            with open('httplist.txt', 'a+') as f:
                for s in ipp:
                    f.write(s)
                    f.write('\n')
            with open('httpslist.txt', 'a+') as f:
                for s in ips:
                    f.write(s)
                    f.write('\n')
            i = i + 1
            time.sleep(1)
        except:
            continue
