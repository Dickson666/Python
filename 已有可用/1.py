import requests;
import random
import string

for i in range(10):
    a = requests.get('https://api.ixiaowai.cn/api/api.php');
    print(a);
    print(a.status_code);
    with open("photos\\" + ''.join(random.sample(string.ascii_letters + string.digits, 20)) + ".jpg", "wb+") as f:
       f.write(a.content);
    print("Finish!");
