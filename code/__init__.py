# -*-coding:utf-8-*-

import time
import random
import requests

__version__ = "0.0.3"


def puyun(account: dict):
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
    pycheckinpostdata = {}
    for email, passwd in account.items():
        email = str(email)
        passwd = str(passwd)
        pyaccountpostdata = {
            "email": email,
            "passwd": passwd,
        }
        error1 = {}
        s = requests.Session()
        pyplogin = s.post(url=pyloginurl, headers=pyheaders, data=pyaccountpostdata)
        if "\"ret\":0" not in pyplogin.text:
            error1['login'] = pyplogin.text
        time.sleep(random.randint(1, 3))
        pypcheckin = s.post(url=pycheckinurl, headers=pycheckinheaders, data=pycheckinpostdata)
        if "\"ret\":0" not in pypcheckin:
            error1['checkin'] = pypcheckin.text
        time.sleep(random.randint(1, 3))
        pyrlogout = s.get(url=pylogouturl, headers=pyheaders)
        if "<title>PU Cloud</title>" not in pyrlogout.text and "\"welcome\": \"有疑问吗? 联系我们!\"," not in pyrlogout.text:
            error1['logout'] = pyplogin.text
        s.close()
        if error1:
            f = open(r"autocheckin_log.txt", "a", encoding="utf-8")
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "--用户    " + email + "    puyun签到失败" + "\n")
            f.close()
            f = open(r"autocheckin_error.txt", "a", encoding="utf-8")
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "--用户    " + email + "    puyun签到失败:\n")
            for i, j in error1.items():
                f.write("    " + i + ":" + j + "\n")
            f.close()
        else:
            f = open(r"autocheckin_log.txt", "a", encoding="utf-8")
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "--用户    " + email + "    puyun签到成功" + "\n")
            f.close()
    return True


def fpork(account: dict):
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
    pycheckinpostdata = {}
    for email, passwd in account.items():
        email = str(email)
        passwd = str(passwd)
        pyaccountpostdata = {
            "email": email,
            "passwd": passwd,
        }
        s = requests.Session()
        pyplogin = s.post(url=pyloginurl, headers=pyheaders, data=pyaccountpostdata)
        if "\"ret\":0" not in pyplogin.text:
            error1["login"] = pyplogin.text
        time.sleep(random.randint(1, 3))
        pypcheckin = s.post(url=pycheckinurl, headers=pycheckinheaders, data=pycheckinpostdata)
        if "\"ret\":0" not in pypcheckin:
            error1['checkin'] = pypcheckin.text
        time.sleep(random.randint(1, 3))
        pyrlogout = s.get(url=pylogouturl, headers=pyheaders)
        if "<title>猪の免费大飞机</title>" not in pyrlogout.text and "<h1>猪の免费大飞机</h1>" not in pyrlogout.text:
            error1['logout'] = pyplogin.text
        s.close()
        if error1:
            f = open(r"autocheckin_log.txt", "a", encoding="utf-8")
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "--用户    " + email + "    fpork签到失败" + "\n")
            f.close()
            f = open(r"autocheckin_error.txt", "a", encoding="utf-8")
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "--用户    " + email + "    fpork签到失败:\n")
            for i, j in error1.items():
                f.write("   " + i + ":" + j + "\n")
            f.close()
        else:
            f = open(r"autocheckin_log.txt", "a", encoding="utf-8")
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "--用户    " + email + "    fpork签到成功," + "\n")
            f.close()
    return True


def allcheckin(puyunaccount: dict, fporkaccount: dict):
    puyun(puyunaccount)
    fpork(fporkaccount)
    return True
