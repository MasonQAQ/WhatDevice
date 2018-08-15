# coding=utf-8

from PluginManager import Model_CMS

class WordPress(Model_CMS):
    name = "WordPress"
    desc = "WordPress是使用PHP语言开发的博客平台，用户可以在支持PHP和MySQL数据库的服务器上架设属于自己的网站. 也可以作为cms使用"
    author = "h4ck3r007"

    def __init__(self):
        Model_CMS.__init__(self)

    def detect(self, target, index_content=""):
        detect_url = target + "/wp-admin/admin-footer.php"
        res = self.cms_requests.get(detect_url, timeout=self.cms_request_timeout)
        if res.status_code != 200:
            return False
        if res.text == "-1":
            return True
        return False


