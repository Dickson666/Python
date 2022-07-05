import requests;
import json
url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
dat = {
    # "from":"zh",
    # "to":"en",
    # "query": "你好",
    # "transtype": "translang",
    # "simple_means_flag": "3",
    # "sign": "232427.485594",
    # "token": "5836cf30e1cb45d57824876e289beba9",
    # "domain": "common"
    # "query": "你好"
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16400723154784",
    "sign": "802ad1f813a1c70dadd791861b4c1949",
    "lts": "1640072315478",
    "bv": "470df6afd582fe67e18c2221dab59fb3",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
    # "i": "你好世界"
}
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
dat['i'] = input();
a = requests.post(url = url, data = dat, headers = head);
b = a.json();
print(b['translateResult'][0][0]['tgt']);
