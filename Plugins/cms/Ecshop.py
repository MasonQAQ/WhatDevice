# coding=utf-8

from PluginManager import Model_CMS
import re

class Ecshop(Model_CMS):
    name = "ecshop"
    desc = "ECShop是一款B2C独立网店系统,适合企业及个人快速构建个性化网上商店。系统是基于PHP语言及MYSQL数据库构架开发的跨平台开源程序。"
    author = "h4ck3r007"

    def __init__(self):
        Model_CMS.__init__(self)

    def detect(self, target, index_content=""):
        if 'content="ECSHOP' in index_content:
            return True
        return False

    def version(self, target, index_content=""):
        return re.findall(r'<meta name="Generator" content="ECSHOP (.+?)" />', index_content)[0]
