import requests

for i in range(10):
    a = requests.get('https://api.ixiaowai.cn/api/api.php');
    print(a);
    print(a.status_code);
    with open("photos/" + str(i) +".jpg", "wb+") as f:
       f.write(a.content);
    print("Finish!");
