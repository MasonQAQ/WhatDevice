# coding=utf-8

from PluginManager import PluginManager
from PluginManager import Model_CMS
from Crawler import Crawler

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
    target = "http://www.dedecms.com"  # dedecms
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
    keyword = "powered by discuz"
    url_list = Crawler.baidu_search(keyword=keyword, page=2)
    for target in url_list:
        for plugin in plugins:
            if plugin.detect(target):
                print(target + " : " + plugin.name)


if __name__ == '__main__':
    # url_test()
    # single_test()
    crawler_multi_test()
