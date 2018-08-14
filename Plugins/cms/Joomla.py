# coding=utf-8

from PluginManager import Model_CMS

class Joomla(Model_CMS):
    name = "Joomla"
    desc = "Joomla!是一套全球知名的内容管理系统。Joomla!是使用PHP语言加上MySQL数据库所开发的软件系统,目前最新版本是3.8。"
    author = "h4ck3r007"

    def __init__(self):
        Model_CMS.__init__(self)

    def detect(self, target):
        detect_url = target + "/index.php/component/ajax?format=json"
        res = self.cms_requests.get(detect_url, timeout=self.cms_request_timeout)
        if res.status_code != 200:
            return False
        if res.text.strip() == '{"success":true,"message":null,"messages":null,"data":null}':
            return True
        return False



