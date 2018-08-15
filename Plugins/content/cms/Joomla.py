# coding=utf-8

from PluginManager import Model_CMS

class Joomla(Model_CMS):
    name = "Joomla"
    desc = "Joomla!是一套全球知名的内容管理系统。Joomla!是使用PHP语言加上MySQL数据库所开发的软件系统,目前最新版本是3.8。"
    author = "h4ck3r007"

    def __init__(self):
        Model_CMS.__init__(self)

    def detect(self, target, index_content=""):
        if 'content="Joomla! - Open Source Content Management"' in index_content:
            return True
        return False

    def version(self, target, index_content=""):
        version_url = target + "/administrator/manifests/files/joomla.xml"
        res = self.cms_requests.get(version_url, timeout=self.cms_request_timeout)
        if res.status_code != 200:
            return Model_CMS.version(self, target)
        import xml.dom.minidom
        doc = xml.dom.minidom.parseString(res.content)
        bulkPmMrDataFile = doc.documentElement
        enbs = bulkPmMrDataFile.getElementsByTagName("version")
        return enbs[0].childNodes[0].data

