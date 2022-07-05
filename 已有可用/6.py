import requests
import re
import time
import os
import sys

illegal = ["<", ":", "\"", ">", "\*", "/", "\\\\", "\?", "\|"]
'''
for i in range(0, 9):
   illegal[i] = re.compile(illegal[i]);

qwq = "Re|从零开始。。。";
print(qwq[0]);
# qwq[0] = 'Z';
if re.findall(r':', qwq) or re.findall('。', qwq):
   print("QWQ");
for j in illegal:
    print(j);
    il = re.search(j, qwq);
    if il:
       while il:
           # print(il.span());
           ct = 0;
           qwq1 = "";
           qwq2 = "";
           for k in il.span():
              if ct:
                  qwq2 = qwq[k:];
              else:
                  qwq1 = qwq[:k];
              ct = ct + 1;
           qwq = qwq1 + qwq2;
           il = re.search(j, qwq);
           print(qwq);
sys.exit();
'''
userinfo = "Hm_lvt_d29ecd95ff28d58324c09b9dc0bee919=1654433059; jieqiVisitId=article_articleviews%3D2847; PHPSESSID=alsfg6gnropn5ta3k5usm3gqdp; jieqiUserInfo=jieqiUserId%3D277678%2CjieqiUserUname%3Ddickson%2CjieqiUserName%3Ddickson%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%E6%99%AE%E9%80%9A%E4%BC%9A%E5%91%98%2CjieqiUserVip%3D0%2CjieqiUserHonorId%3D1%2CjieqiUserHonor%3D%E5%A4%A9%E7%84%B6%2CjieqiUserToken%3D1933f4ce425f90c5481cdbe0033c9cc6%2CjieqiCodeLogin%3D0%2CjieqiCodePost%3D0%2CjieqiUserLogin%3D1654435552; jieqiVisitInfo=jieqiUserLogin%3D1654435552%2CjieqiUserId%3D277678; Hm_lpvt_d29ecd95ff28d58324c09b9dc0bee919=1654435612";

# 使用前先登录并修改userinfo

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Cookie":userinfo
}
url = "https://www.linovelib.com/";
a = requests.post(url = url, headers = head);
print(a.text);
if(a):
   print("Successfully Connected");
b = a.text;
c = re.findall(r'<a href=\"/novel/(.*?)\"', b);
# print(c);
for i in c:
    #i = "111/156884.html";
    time.sleep(0.5);
    a = requests.post(url = url + "/txtfull/" + i, headers = head);
    b = re.findall(r'<a href=\"(.*?)\" rel=\"', a.text);
    Na = re.findall(r'<title>(.*?)TXT全文下载_哔哩轻小说', a.text);
    # print(Na);
    if b:
        d = b[0];
        name = Na[0];
        print(d);

    else:
        print("Fail! Reason : unkown website : " + i);
        continue;
    for j in illegal:
        il = re.search(j, name);
        while il:
            ct = 0;
            qwq1 = "";
            qwq2 = "";
            for k in il.span():
               if ct:
                  qwq2 = name[k:];
               else:
                  qwq1 = name[:k];
               ct = ct + 1;
            name = qwq1 + "_" + qwq2;
            il = re.search(j, name);
    if os.path.exists("D:\lmq\python\e-books\\"+name + ".txt"):
        print("Fail! Reason : " + name + "has been download.");
        continue;
    e = requests.get(url = d, headers = head);
    while len(e.content) < 10240:
        e = requests.get(url = d, headers = head);
    print(d);
    with open("D:\lmq\python\e-books\\"+name+".txt", "wb+") as f:
        f.write(e.content);
    # with open(i + ".txt", "wb+") as f:
    #    f.write(a.content);
    print(name);
    print("Success!");
