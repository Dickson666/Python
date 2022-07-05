import requests
import time
from bs4 import BeautifulSoup
#from urllib.request import urlopen
import urllib

def work(url):

    print(url);

    c = requests.get(url = url);

    print(c.status_code);

    s = BeautifulSoup(c.text, 'lxml');

    i1 = s.find_all('tr');

    ipl = [];

    ipll = [];

    for i in i1:

        j = i.find_all('td');

        if len(j) < 2:
            continue;
        
        ipl.append(j[0].text + ':' + j[1].text);

    print(len(ipl));
    
    for i in ipl:

        print(i);

        time.sleep(0.2);
        
        try:
            px = {"http" : "http://" + i};

            #re = urllib.parse.urlopen(url, proxies = px).read();
            
            re = requests.get("http://baidu.com/", proxies = px, timeout = 3);
            
            ipll.append(i);
            
        except Exception as e:

            print(e);

            print("Error");

            continue;
    return ipll;


url = "https://free.kuaidaili.com/free/inha/";

ip_l = [];

for i in range(1, 5):
    j = work(url + str(i));
    for k in j:
        ip_l.append(k);

for i in ip_l:
    with open("IP LIST.txt", "a") as f:
        f.write(i + '\n');
