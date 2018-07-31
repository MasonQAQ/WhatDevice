# coding=utf-8

from PluginManager import PluginManager
from PluginManager import Model_CMS

if __name__ == '__main__':
    # 加载所有插件
    PluginManager.LoadAllPlugin()

    target = "http://www.wellidc.net"
    target = "http://www.zkwuan.com"

    plugins = Model_CMS.GetPluginObject()

    for plugin in plugins:
        if plugin.detect(target):
            print(target + " : " + plugin.name)
