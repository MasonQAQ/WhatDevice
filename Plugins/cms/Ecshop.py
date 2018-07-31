# coding=utf-8

from PluginManager import Model_CMS
import requests

class Ecshop(Model_CMS):
    name = "ecshop"
    desc = "ECShop是一款B2C独立网店系统,适合企业及个人快速构建个性化网上商店。系统是基于PHP语言及MYSQL数据库构架开发的跨平台开源程序。"
    author = "h4ck3r007"

    def detect(self, target):
        detect_url = target + "/api/checkorder.php"
        res = requests.get(detect_url).text
        if "new_orders" in res and "new_paid" in res:
            return True
        return False
