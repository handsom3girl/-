import requests
import re
import pandas as pd
import requests
import re
import time
# from lxml import etree
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect

# from cmdb import models


global username
global password
global code
global s


# Create your views here.


def getCode():
    def getHTMLcontent(url, kv, s):
        try:
            r = s.get(url, headers=kv)
            r.raise_for_status()
            print(r.headers['set-Cookie'])
            return r
        except:
            return "产生异常"

    url = "http://ssfw1.hlju.edu.cn/ssfw/jwcaptcha.do"
    kv = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    # openID = request.POST.get("openID")
    # print(type(openID))
    global s
    s = requests.session()
    ver = getHTMLcontent(url, kv, s)
    pic = './static/code.jpg'
    with open(pic, 'wb') as f:
        f.write(ver.content)
    
    c = ver.headers['set-Cookie']
    return c
def login(u,p,code,c):
    global username
    global password

    global s
    log = "http://ssfw1.hlju.edu.cn/ssfw/jwcaptcha.do"
    url_get = "http://ssfw1.hlju.edu.cn/ssfw/j_spring_ids_security_check"
    url = "http://ssfw1.hlju.edu.cn/ssfw/zhcx/cjxx.do"

    def getHTMLcontent(url, kv, s):
        try:
            r = s.get(url, headers=kv)
            r.raise_for_status()
            return r.content
        except:
            return "产生异常"


    def getCookies(u,p,code):
        message = {}
        message['j_username'] = u
        message['j_password'] = p
        message['validateCode'] = code
        return message


    # code = request.POST.get("Code")
    # cookie  = request.POST.get("cookie")
    # print(cookie)
    co=re.findall(r'''JSESSIONID=(.*);''',str(c))
    print(co)
    print(type(co))
    c = requests.cookies.RequestsCookieJar()
    c.set('JSESSIONID', co[0], path='/', domain='ssfw1.hlju.edu.cn')
    s=requests.session()
    s.cookies.update(c)
    message = getCookies(u,p,code)
    kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    r = s.post(url = url_get, data = message, headers = kv)
    print(r.headers)
    if 'success'in r.text:
        return s.cookies
    else:
        return 'false'

def classinfo(u,p,code,c):
    global username
    global password
    global s
    log = "http://ssfw1.hlju.edu.cn/ssfw/jwcaptcha.do"
    url_get = "http://ssfw1.hlju.edu.cn/ssfw/j_spring_ids_security_check"
    url = "http://ssfw1.hlju.edu.cn/ssfw/pkgl/kcbxx/4/2019-2020-2.do"

    def getHTMLcontent(url, kv, s):
        try:
            r = s.get(url, headers=kv)
            r.raise_for_status()
            return r.content
        except:
            return "产生异常"


    def getCookies(u,p,code):
        message = {}
        message['j_username'] = u
        message['j_password'] = p
        message['validateCode'] = code
        return message


    # code = request.POST.get("Code")
    # cookie  = request.POST.get("cookie")
    # print(cookie)
    co=re.findall(r'''JSESSIONID=(.*);''',str(c))
    
    c = requests.cookies.RequestsCookieJar()
    c.set('JSESSIONID', co[0], path='/', domain='ssfw1.hlju.edu.cn')
    s=requests.session()
    s.cookies.update(c)
    message = getCookies(u,p,code)
    kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    r = s.post(url = url_get, data = message, headers = kv)
    print(r.headers)
    if 'success'  not in r.text:
        print('n')
        return 'false'
    else:
        m=s.get(url,headers=kv)
        #print(s.cookies)
        #print(m.text)
        df = pd.read_html(m.text)[0]
        print(df) 
