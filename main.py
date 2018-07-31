# coding=utf-8

from PluginManager import PluginManager
from PluginManager import Model_CMS

if __name__ == '__main__':
    # 加载所有插件
    PluginManager.LoadAllPlugin()

    target = "http://www.wellidc.net" #phpcms
    target = "http://www.dedecms.com" #dedecms
    target = "http://www.dstex.cn/" #ecshop
    target = "http://bbs.heilanhome.com" #discuz

    plugins = Model_CMS.GetPluginObject()

    for plugin in plugins:
        if plugin.detect(target):
            print(target + " : " + plugin.name)
