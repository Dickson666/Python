import m3u8
import os
import requests
from Crypto.Cipher import AES
# pycryptodome库
from bs4 import BeautifulSoup

namlist = ["零","一","二","三","四","五","六","七","八","九","十","十一","十二","十三"];

lines = []

fengexian = "--------------------";


head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

place = "中二病でも恋がしたい！/" ;

tot_url = "https://cdn.duduzx.cn"# 从樱花爬的

def work(i, pls):
    url = tot_url + i;

    name = url.split('/')[-1];


    if os.path.isfile(pls + name):
        #continue;
        return;
        
    a = requests.get(url = url, headers = head);

    with open(pls + name, "wb+") as f:
        f.write(a.content);

def download(pls, key_url):# 下载函数。

    if not os.path.exists(pls + "ts"):# 检查 "ts" 目录是否存在
        os.makedirs(pls + "ts");
    
    with open(pls + "index.m3u8", 'r') as f:
        lines = f.readlines();

    ts_list = [l[:-1] for l in lines if l [0:1]=="/"];

    print(len(ts_list));

    for i in ts_list:

        print(i);
        
        work(i, pls + "ts/");

    #if !(os.path.exists("ts"))
    #    os.path.makedirs("ts");

    mf = open(pls + "正片.mp4", "wb+");

    key = requests.get(key_url, headers = head).content;

    ak = AES.new(key, AES.MODE_CBC, key);

    print("");
    print(fengexian + "translating" + fengexian);
    print("");

    for i in ts_list:

        name = i.split('/')[-1];

        print(name);

        try:

            with open(pls + "ts/" + name, "rb+") as f:
                
                mf.write(ak.decrypt(f.read()));
                
        except: # 如果出现无法解码的情况，说明文件可能没有下载完整，重新下载。

            os.remove(pls + "ts/" + name);
               
            work(i, pls + "ts/");
            
            with open(pls + "ts/" + name, "rb+") as f:

               mf.write(ak.decrypt(f.read()));

base_url = "http://www.dmh8.com/player/4538-1-";

'''-------------------- M A I N --------------------'''

for i in range(4, 14):

    nam = "第" + namlist[i] + "集/"; 
    
    pls = place + nam;
    
    if not os.path.exists(pls): # 检查目录是否存在
        os.makedirs(pls);

    print("QWQ");

    b = "";

    if not os.path.isfile(pls + "index.m3u8"): # 还未爬取相应的 index 文件

        print("QwQ");

        a = requests.get(base_url + str(i-1), headers = head);

        #f = open("test.txt","wb+");
        
        #f.write(a.content);


        b = a.text;

        c = b.find("\"url\":\"htt");
        c1 = b.find("m3u8");
        
        url = b[c + 7 : c1 + 4];

        url = url.replace("\/", "/");
        

        a = requests.get(url, headers = head);

        #print(a.text);

        b = a.text;
        
        c = b.find("/");

        url = tot_url + b[c:];
        
        print(url);

        a = requests.get(url, headers = head);
        
        with open(pls + "index.m3u8", "wb+") as f:

            f.write(a.content);

    with open (pls + "index.m3u8", "r") as f:

        b = f.read();

    c = b.find("URI");

    c1 = b.find("key.key");

    key_url = tot_url + b[c + 5 : c1 + 7];

    print(key_url);

    download(pls, key_url);
