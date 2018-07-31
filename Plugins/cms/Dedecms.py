# coding=utf-8

from PluginManager import Model_CMS
import requests
import os
from Utils import calculate_md5


class Dedecms(Model_CMS):
    name = "dedecms"
    desc = "织梦CMS(dedecms)是集简单、健壮、灵活、开源几大特点的开源内容管理系统,是国内开源CMS的领先品牌"
    author = "h4ck3r007"

    def detect(self, target):
        flag = False
        detect_url = target + "/plus/img/dfpic.gif"
        res = requests.get(detect_url)
        if res.status_code == 200:
            with open('Temp/dedecms.jpg', 'a+') as file:
                file.write(res.content)
                file.flush()
                md5sum = calculate_md5(file)
                if md5sum == "d41d8cd98f00b204e9800998ecf8427e":
                    flag = True
            file.close()
            os.remove("Temp/dedecms.jpg")
        return flag



