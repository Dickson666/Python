from selenium.webdriver.chrome.options import Options

co = Options();
co.add_argument('--headless');
co.add_argument('--disalbe-gpu');

import requests;
from selenium import  webdriver;
from bs4 import BeautifulSoup;

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    'Referer':'http://93.174.95.27'
    #"Cookie":"pgv_pvid=8583923331; fqm_pvqid=f2ceef4e-2ff6-4f01-8349-0c0343430799; fqm_sessionid=de9129f4-93e0-4af3-aeae-a5b4ce19c36c; pgv_info=ssid=s9722040664; _qpsvr_localtk=0.3214632464856175; RK=B69cA1TFb8; ptcz=aa9af8917dc9875df1066ab2bb8fbdc94225d58d4ba304dba71d20ffaa44d78b; qqmusic_key=Q_H_L_5yBisTnUMWcs-BpatJueLXSFIMZwcfqUn1zTKHja86cksA-vjIT98qg; psrf_access_token_expiresAt=1664372961; psrf_musickey_createtime=1656596961; tmeLoginType=2; euin=oKoqNKnioKE57n**"
}

url = "https://music.163.com/#/search/m/?s=";

'''uuu = "http://music.163.com/song/media/outer/url?id=26201899";

a = requests.get(uuu, headers = head);

with open("ふわふわ時間.mp3", "wb+") as f:

    f.write(a.content);'''

se = input("请输入要下载的歌名（VIP好像不行）：");

url = url + se + "&type=1";

#a = requests.get(url, headers = head);

a = webdriver.Chrome(chrome_options=co);

a.get(url);

a.switch_to.frame('g_iframe');

b = a.execute_script("return document.documentElement.outerHTML");

a.quit();

b = b.encode("utf-8");

f = open("test.html", "wb+");

f.write(b);'''

f = open("test.html", "rb+");

b = f.read();'''

b = BeautifulSoup(b, "lxml");

c = b.find_all("div", "text");

g = "/artist";

gg = "/song?i";

music_list = [];

cnt = 0;

for i in c:
    
    ee = i.find_all("a");

    for e in ee:

    #if e is None:

        #continue;

        #print(e);

        f = e.get("href");

        f = str(f)[:7];

        #print(f);

        if f == g:

            music_list[cnt-1].append(e.text);

        if f != gg:

            continue;

        f = e.get("href");

        #print(f);
        
        m_id = str(e.get("href"))[9:];

        name = e.text;

        music_list.append([m_id,name]);

        cnt = cnt + 1;

    #print("------------");

    #break;

#print("请输入你要的歌曲编号");


for i in range(1, len(music_list) + 1):

    if len(music_list[i-1]) == 2:

        print("编号:", i, ", 歌名:", music_list[i-1][1], ", 歌手没爬到。。。");

        continue;

    print("编号:", i, ", 歌名:", music_list[i-1][1], ", 歌手:", end = ' ');

    for j in range(2, len(music_list[i-1])):

        qwq = "";

        if(j == len(music_list[i-1])-1):

            qwq='\n';

        else:

            qwq = '/';
        
        print(music_list[i-1][j], end = qwq);

while(1):

    req_id = int(input("请输入你要的歌曲编号（输入0以结束下载）:"));

    if req_id == 0:

        break

    final_id = music_list[req_id-1][0];

    name = music_list[req_id-1][1] + '_' ;

    i = req_id;

    for j in range(2, len(music_list[i-1])):

        qwq = "";

        if(j == len(music_list[i-1])-1):

            qwq='.mp3';

        else:

            qwq = ',';
                
        name = name + music_list[i-1][j] + qwq;


    #https://m801.music.126.net/20220704211940/23c69ffd18296501d2f22f3dcb96df33/jdyyaac/555d/0e53/050f/b7410feace995a7b661e2e541cefff24.m4a
        
    download_url = "http://music.163.com/song/media/outer/url?id=";

    print("下载中......");

    a = requests.get(download_url + final_id + ".mp3", headers = head);

    print(a.status_code);

    if len(a.content) < 100 * 1024:

        print("可能是VIP？");

    else:

        with open(name, "wb+") as f:
        
           f.write(a.content);

        print("下完啦！");


'''

url = "http://dl.stream.qqmusic.qq.com/C400001HmcR90kSSA6.m4a?guid=8468772526&vkey=D1BCD767B61D429B519555572B9F3C20328921D8B82BB7756080556053249DF3AA1E30D4A0631E6EFDFDD41DB0475E33E8DA579A52E7C8BA&uin=&fromtag=120032";

a = requests.get(url, headers = head);

print(a.status_code);

with open("My Soul, Your Beats!.mp3", "wb+") as f:
    f.write(a.content);

'''
