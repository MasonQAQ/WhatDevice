# coding=utf-8

import requests
from bs4 import BeautifulSoup as bs
import re
import sys


class Crawler:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.108 Safari/537.36'
    }

    @staticmethod
    def baidu_search(keyword, page=76):
        url_list = set()
        for i in range(0, page * 10, 10):
            # pn IS page_number * 10
            sys.stdout.write("正在爬取[百度], 第%s页\r" % (i / 10 + 1))
            sys.stdout.flush()
            current_url = 'http://www.baidu.com/s?wd=%s&pn=%s' % (keyword, str(i))
            r = requests.get(url=current_url, headers=Crawler.headers)
            soup = bs(r.content, "html.parser")
            urls = soup.find_all(name='a', attrs={'href': re.compile('.'), 'class': 'c-showurl'})
            for i in urls:
                if 'www.baidu.com/link?url=' in i['href']:
                    try:
                        a = requests.get(url=i['href'], headers=Crawler.headers, timeout=5)
                    except:
                        continue
                    if a.status_code == 200:
                        rr = re.compile("[a-zA-z]+://[^\s]*?/")  # 非贪婪匹配，找出前缀
                        res_urls = rr.findall(a.url)
                        if len(res_urls) > 0:
                            url_list.add(res_urls[0])
        return url_list

    # todo: 补充google搜索接口
    def google_search(self, keyword):
        pass

    # todo: 补充bing搜索接口
    def bing_search(self, keyword):
        pass

    # todo: 补充zoomeye搜索接口
    @staticmethod
    def zoomeye_search(keyword):

        zoomeye_headers = {
            'Host': 'www.zoomeye.org',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Cube-Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inl5bG92ZXNsaWZlQGdtYWlsLmNvbSIsInV1aWQiOiJlZGVjMTE5YTBlYzVkMjgxOGE1NDc0OTVkZDAwYzZjZiIsImlhdCI6MTUzMzEyMTIwNywiZXhwIjoxNTMzMjA3NjA3fQ.XDhHPk_sZEDhbUm1R3dYQQN-ZZBvxvQpNyrFIwtKwuY',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer': 'https://www.zoomeye.org/searchResult?q=app%3Adedecms',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'

        }

        for i in range(10):
            requests.session()
            cookie = {'__jsluid': 'daaec0014d2191a25adc7ab2250b72a1',
                      'Hm_lvt_3c8266fabffc08ed4774a252adcb9263': '1532420643,1532420661',
                      ' __jsl_clearance': '1533121108.615|0|muc1bVnpd4xmMLWl0VqWll9TsvM%3D',
                      'Hm_lpvt_3c8266fabffc08ed4774a252adcb9263': '1533121217'}
            res = requests.get("https://www.zoomeye.org/api/search?q=app%3Adedecms&p=" + str(i), cookies=cookie, headers=zoomeye_headers).text
            print(res)
        pass
