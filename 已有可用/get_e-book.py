import requests
import string
import time
import os
from bs4 import BeautifulSoup

def pt(a):
    print(type(a));
    return;

NAME = 'e-book';

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Cookie" : ""
}

download_url = "https://www.linovelib.com/modules/article/packdown_k.php?type=txt&id="

def work(url):

    a = requests.get(url);

    b = a.content;

    print(type(b));

    '''
    b = "qwq";
    with open("test.txt", "rb+")as f:
        b = f.read();
    '''
    #b 是一个 html

    b = BeautifulSoup(b,"html.parser");

    print(type(b));

    #print(b.find_all('div', class_ = "tit fl"));

    #c = b.find('div', {'class':'lists'}).find_all('a');

    c = b.find_all('img');

    #c是b中所有的img分组内的元素

    pt(c);

    for d in c: # 枚举所有元素
        if str(d.get('alt')) == "None":# 没名字
            continue;
        if str(d.get('src'))[:5] != 'https': # 错误的url
            continue;
        #pt(d.get('data-original'));
        
        #print(d);
        #pt(d.get('src'));
        #print(d.get('src'));
        #print(d.get('data-original'));
        print(d.get('alt'));
        nam = NAME + '/' + d.get('alt');
        if os.path.exists(nam):
            continue;
        os.makedirs(nam);
        #两种可能的储存位置
        ln = "qwq";
        if str(d.get('data-original')) == "None":
            ln = str(d.get('src'));
            e = requests.get(ln);
            with open(nam + '/' + '封面' + '.jpg', "wb+") as f:
               f.write(e.content);
        else:
            ln = str(d.get('data-original'));
            e = requests.get(ln);
            with open(nam + '/' + '封面' + '.jpg', "wb+") as f:
               f.write(e.content);
        #切片提取id
        ln = ln[46:];
        iii = 0;
        while ln[iii] != '/':
            iii = iii + 1;
        iii = iii + 1;
        ln = ln[iii:];
        iii = 0;
        while ln[iii] != '/':
            iii = iii + 1;
        ln = ln[:iii];
        print(ln);
        #爬取正文
        url = download_url + ln + "&fname=" + str(d.get('alt'));
        e = requests.get(url = url, headers = head);
        while len(e.content) < 10240:
            e = requests.get(url = url, headers = head);
        print(e.status_code);
        #print(e.content);
        with open(nam + '/' + '正文.txt', "wb+") as f:
            f.write(e.content);
        time.sleep(20);
        
    with open("test.txt", "wb+") as f:
       f.write(a.content);
    return;

with open ("cook.ie", "r") as f:
    head["Cookie"] = f.read();

with open ("page.cts", "r") as f:
    qwq = f.read();
    
for i in range(int(qwq),10):
    work("https://www.linovelib.com/wenku/lastupdate_0_0_0_0_0_0_0_" + str(i) + "_0.html");
    with open("page.cts", "w") as f:
        f.write(str(i+1))

