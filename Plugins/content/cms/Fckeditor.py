# coding=utf-8
from PluginManager import Model_CMS
import re

class Fckeditor(Model_CMS):
    name = "Fckeditor"
    desc = "FCKeditor是一个专门使用在网页上属于开放源代码的所见即所得文字编辑器。"
    author = "h4ck3r007"

    def __init__(self):
        Model_CMS.__init__(self)

    def detect(self, target, index_content=""):
        detect_url = target + "/fckeditor/fckeditor.js"
        res = self.cms_requests.get(detect_url, timeout=self.cms_request_timeout)
        if res.status_code != 200:
            return False
        res = res.text
        if "FCKeditor - The text editor for Internet" in res:
            return True
        return False

    def version(self, target, index_content=""):
        detect_url = target + "/fckeditor/fckeditor.js"
        res = self.cms_requests.get(detect_url, timeout=self.cms_request_timeout)
        if res.status_code != 200:
            return Model_CMS.version(self, target)
        r = re.findall("FCKeditor.prototype.Version.*=.*'(.+?)'.*;", res.content)
        if len(r) > 0:
            return r[0]
        return Model_CMS.version(self, target, index_content)
