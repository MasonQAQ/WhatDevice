# coding=utf-8

from PluginManager import Model_CMS

class Ecshop(Model_CMS):
    name = "ecshop"
    desc = "ECShop是一款B2C独立网店系统,适合企业及个人快速构建个性化网上商店。系统是基于PHP语言及MYSQL数据库构架开发的跨平台开源程序。"
    author = "h4ck3r007"

    def __init__(self):
        Model_CMS.__init__(self)

    def detect(self, target):
        detect_url = target + "/api/checkorder.php"
        res = self.cms_requests.get(detect_url,timeout=self.cms_request_timeout)
        if res.status_code != 200:
            return False
        res = res.text
        if "new_orders" in res and "new_paid" in res:
            return True
        return False
