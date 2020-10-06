# -*-coding:utf-8-*-

import time
import random
import requests

__version__ = "0.0.1"


def puyun():
    ret1 = True
    error1 = {}
    pyloginurl = "https://pucloud.vip/auth/login"
    pylogouturl = "https://pucloud.vip/user/logout"
    pycheckinurl = "https://pucloud.vip/user/checkin"
    pyheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }
    pycheckinheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Content-Type": "application/json",
    }
    pyaccountpostdata = {
        "email": "",
        "passwd": "",
    }
    pycheckinpostdata = {}
    s = requests.Session()
    pyplogin = s.post(url=pyloginurl, headers=pyheaders, data=pyaccountpostdata)
    if pyplogin.text.split("ret\":")[1][0] == "1":
        pass
    else:
        ret1 = False
        error1['login'] = pyplogin.text
    time.sleep(random.randint(1, 3))
    pypcheckin = s.post(url=pycheckinurl, headers=pycheckinheaders, data=pycheckinpostdata)
    if pypcheckin.text.split("ret\":")[1][0] == "1":
        pass
    else:
        ret1 = False
        error1['checkin'] = pypcheckin.text
    time.sleep(random.randint(1, 3))
    pyrlogout = s.get(url=pylogouturl, headers=pyheaders)
    if "<title>PU Cloud</title>" in pyrlogout.text and "\"welcome\": \"有疑问吗? 联系我们!\"," in pyrlogout.text:
        pass
    else:
        ret1 = False
        error1['logout'] = pyplogin.text
    s.close()
    return ret1, error1


def fpork():
    ret1 = True
    error1 = {}
    pyloginurl = "https://forever.fpork.com/auth/login"
    pylogouturl = "https://forever.fpork.com/user/logout"
    pycheckinurl = "https://forever.fpork.com/user/checkin"
    pyheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }
    pycheckinheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Content-Type": "application/json",
    }
    pyaccountpostdata = {
        "email": "",
        "passwd": "",
    }
    pycheckinpostdata = {}
    s = requests.Session()
    pyplogin = s.post(url=pyloginurl, headers=pyheaders, data=pyaccountpostdata)
    if pyplogin.text.split("ret\":")[1][0] == "1":
        pass
    else:
        ret1 = False
        error1["login"] = pyplogin.text
    time.sleep(random.randint(1, 3))
    pypcheckin = s.post(url=pycheckinurl, headers=pycheckinheaders, data=pycheckinpostdata)
    if pypcheckin.text.split("ret\":")[1][0] == "1":
        pass
    else:
        ret1 = False
        error1['checkin'] = pypcheckin.text
    time.sleep(random.randint(1, 3))
    pyrlogout = s.get(url=pylogouturl, headers=pyheaders)
    if "<title>猪の免费大飞机</title>" in pyrlogout.text and "<h1>猪の免费大飞机</h1>" in pyrlogout.text:
        pass
    else:
        ret1 = False
        error1['logout'] = pyplogin.text
    s.close()
    return ret1, error1


def main():
    f = open(r"autocheckin.txt", "a", encoding="utf-8")
    f.write("\n" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "--")
    f.close()
    f = open(r"error.txt", "a", encoding="utf-8")
    f.write("\n")
    f.close()
    ret1, error1 = puyun()
    if ret1:
        f = open(r"autocheckin.txt", "a", encoding="utf-8")
        f.write("py签到成功,")
        f.close()
    else:
        f = open(r"autocheckin.txt", "a", encoding="utf-8")
        f.write("py签到失败,")
        f.close()
        f = open(r"error.txt", "a", encoding="utf-8")
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "--py签到失败:\n")
        for i, j in error1.items():
            f.write("   " + i + ":" + j + "\n")
        f.close()
    ret2, error2 = fpork()
    if ret2:
        f = open(r"autocheckin.txt", "a", encoding="utf-8")
        f.write("fp签到成功,")
        f.close()
    else:
        f = open(r"autocheckin.txt", "a", encoding="utf-8")
        f.write("fp签到失败,")
        f.close()
        f = open(r"error.txt", "a", encoding="utf-8")
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "--fp签到失败:\n")
        for i, j in error1.items():
            f.write("   " + i + ":" + j + "\n")
        f.close()
    return True


if __name__ == "__main__":
    main()
