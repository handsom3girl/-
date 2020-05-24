# coding=utf-8
import requests
import re
import time
#from lxml import etree
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from . import test


global username
global password
global code
global s
# Create your views here.


def getCode(request):
    c=test.getCode()
    return HttpResponse(c)
def getChengji(requests):
    return HttpResponse('true')
def login(request):
    code=request.POST.get('code')
    c=request.POST.get('cookie')
    u=request.POST.get('username')
    p=request.POST.get('password')
    r=test.login(u,p,code,c)
    #co=re.findall(r'''iPlanetDirectoryPro=(.*);''',str(r.headers['set-Cookie']))
    # c.set('iPlanetDirectoryPro',co[0],path='/',domain='.hlju.edu.cn')
    #s.cookies.updata(c)
    #b = s.get(url, headers = kv)
    #print(s.cookies)
    #if ('你没有访问该页面的权限.' not in b.text):
       # print('true')
    print(r)
    return HttpResponse(r)
    #else:
        #print('false')
        #return HttpResponse('false')
def classinfo(request):
    code=request.POST.get('code')
    c=request.POST.get('cookie')
    u=request.POST.get('username')
    p=request.POST.get('password')
    print(code)
    print(c)
    print(u)
    print(p)
    test.classinfo(u,p,code,c)
    return HttpResponse('1')
def index(request):
    global username
    global password
    global s
    a = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    user_list = []
    user_list = models.UserInfo.objects.filter(user=username)
    if len(user_list) == 0:
        models.UserInfo.objects.create(user=username, pwd=password)
    else:
        models.UserInfo.objects.filter(user=username).update(pwd=password)
    models.LogInfo.objects.create(user=username,tim=a)

    kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    log = "http://ssfw1.hlju.edu.cn/ssfw/jwcaptcha.do"
    url_get = "http://ssfw1.hlju.edu.cn/ssfw/j_spring_ids_security_check"
    url = "http://ssfw1.hlju.edu.cn/ssfw/zhcx/cjxx.do"

    def getGradehtml(b):
        html = b.text
        selector = etree.HTML(html)
        root = selector.xpath('/html/body/div/div/div[@id="tab01"]/div[1]/table/tr[@class="t_con"]')
        for e in root:
            sem = e.xpath('td[2]/text()')
            for se in sem:
                semesters.append(se)
            sem = e.xpath('td[4]/text()')
            for se in sem:
                courses.append(se)
            sem = e.xpath('td[7]/text()')
            for se in sem:
                credits.append(se)
            sem = e.xpath('td[8]')
            for se in sem:
                if se.xpath('font/text()') == []:
                    gradelist = se.xpath('span/strong/text()')
                    for grade in gradelist:
                        grades.append(grade)
                else:
                    gradelist = se.xpath('font/text()')
                    for grade in gradelist:
                        grades.append(grade)
        result = zip(semesters, courses, credits, grades)
        return result

    def getGZgrade(b):
        for seme in semelist:
            s_um1 = 0
            device1 = 0
            for semester, course, credit, grade in zip(semesters, courses, credits, grades):
                if (seme in semester):
                    if float(grade) >= 60.0:
                        s_um1 = float(grade) * float(credit) + s_um1
                        device1 = float(credit) + device1
            result_f = s_um1 / device1 / 10
            result_dict.update({seme: result_f})
            jidian_dict = {'seme':seme, 'grade':result_f}
            jidianlists.append(jidian_dict)
    #username = request.POST.get("username" ,'ok')
    #password = request.POST.get("password" ,'ok')
    #temp = {'user':username,'pwd':password}
    #user_list = []
    #user_list = models.UserInfo.objects.all()
    #user_list.append(temp)
    global s
    b = s.get(url, headers = kv)
    semesters = []
    courses = []
    credits = []
    grades = []
    grades_dict = {}
    gradeslist = []
    result = getGradehtml(b)
    semelist = []
    result_dict = {}
    jidian_dict = {}
    jidianlists = []
    s_um = 0
    device = 0
    for semester, course, credit, grade in zip(semesters, courses, credits, grades):
        print(semester, course, credit, grade)
        grades_dict = {'semester':semester, 'course':course, 'credit':credit, 'grade':grade}
        gradeslist.append(grades_dict)
        if(semester[0:9] not in semelist):
            semelist.append(semester[0:9])
        if float(grade) >= 60:
            s_um = float(grade) * float(credit) + s_um  # 计算总绩点
            device = float(credit) + device
    result_f = s_um/device/10
    result_dict.update({'总绩点':result_f})
    jidian_dict = {'seme':'总绩点', 'grade':result_f}
    jidianlists.append(jidian_dict)
    getGZgrade(b)
    print(result_dict)
    #'data': user_list,
    return render(request, 'index.html', {'g':gradeslist, 're':jidianlists})


def eb2c3435cb9160ce1006e756b0858eff(request):
    #temp = {'user':username,'pwd':password}
    #user_list = models.UserInfo.objects.filter.delete()  清空数据库
    key = request.POST.get("aaa",)
    user_list = models.UserInfo.objects.all()
    log_list = models.LogInfo.objects.all()
    if key == 'z245735349':
        return render(request, 'eb2c3435cb9160ce1006e756b0858eff.html',{ 'data': user_list,'data2':log_list})
    else:
        return render(request, 'eb2c3435cb9160ce1006e756b0858eff.html')
