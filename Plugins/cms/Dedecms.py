# coding=utf-8

from PluginManager import Model_CMS
import requests
import hashlib


class Dedecms(Model_CMS):
    name = "dedecms"
    desc = "织梦CMS(dedecms)是集简单、健壮、灵活、开源几大特点的开源内容管理系统,是国内开源CMS的领先品牌"
    author = "h4ck3r007"

    def detect(self, target):
        detect_url = target + "/plus/img/dfpic.gif"
        res = requests.get(detect_url)
        if res.status_code != 200:
            return False
        md5sum = hashlib.md5(res.text.encode("utf-8")).hexdigest()
        if md5sum == "53ec2a55c702dcce530b258fd1d96308":
            return True
        return False



