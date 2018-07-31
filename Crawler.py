# coding=utf-8
import requests
from bs4 import BeautifulSoup as bs
import re


class Crawler:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.108 Safari/537.36'
    }

    @staticmethod
    def baidu_search(keyword):
        url_list = set()
        for i in range(0, 760, 10):
            # pn IS page_number * 10
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
                        url_list.add(rr.findall(a.url)[0])
        return url_list

    # todo: 补充google搜索接口
    def google_search(self, keyword):
        pass

    # todo: 补充bing搜索接口
    def bing_search(self, keyword):
        pass

    # todo: 补充zoomeye搜索接口
    def zoomeye_search(self, keyword):
        pass
