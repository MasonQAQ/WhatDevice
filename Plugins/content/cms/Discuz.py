# coding=utf-8

from PluginManager import Model_CMS

class Discuz(Model_CMS):
    name = "discuz"
    desc = "Discuz!是全球市场占有率第一的社区论坛(BBS)软件"
    author = "h4ck3r007"

    def __init__(self):
        Model_CMS.__init__(self)

    def detect(self, target, index_content=""):
        detect_url = target + "/static/js/swfupload.queue.js"
        res = self.cms_requests.get(detect_url, timeout=self.cms_request_timeout)
        if res.status_code != 200:
            return False
        res = res.text
        if "[Discuz!]" in res:
            return True
        return False
