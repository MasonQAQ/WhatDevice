# coding=utf-8

from PluginManager import Model_CMS
import requests

class Phpcms(Model_CMS):
    name = "phpcms"
    desc = "PHPCMS是一款网站管理软件。该软件采用模块化开发，支持多种分类方式，使用它可方便实现个性化网站的设计、开发与维护。"
    author = "h4ck3r007"

    def detect(self, target):
        detect_url = target + "/api.php?op=ojbk"
        res = requests.get(detect_url)
        if res.text == "API handler does not exist":
            return True
        return False



