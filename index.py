import random
from urllib.request import urlopen
while 1:
    u = random.randint(100000000, 9999999999)
    p = random.randint(100000000000, 9999999999999)
    url = f"http://xyw.xxwtd.store/status.php?action=add&u={u}&p={p}&id=&system_str=PC"
    url2 = f"http://xyw.xxwtd.store/status.php?action=add&u={u + 1}&p={p - 1}&id=&system_str=Android"
    p = urlopen(url).read().decode("utf-8")
    p2 = urlopen(url2).read().decode("utf-8")
    print(f"{p}\n{p2}")
