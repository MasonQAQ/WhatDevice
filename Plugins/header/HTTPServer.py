# coding=utf-8
from PluginManager import Model_Header


class HTTPServer(Model_Header):
    def get(self, header):
        server_str = header.get("Server")
        if server_str:
            server_str = server_str.split(" ")
            return server_str
