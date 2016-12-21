# -*- coding: utf-8 -*-
import requests
import re

class GetIP(object):

    def getFromWeb(self):
        page = requests.get('http://23.239.11.100:8888/')
        return page.text

    def findIP(self, page):
        ipPattern = re.compile(r'\d+.\d+.\d+.\d+')
        portPattern = re.compile(r'(?<=", )\d+')
        ips = ipPattern.finditer(page)
        ports = portPattern.finditer(page)
        result = []
        count = 0
        total = 30
        for i, p in zip(ips, ports):
            proxy = {'ip_port' : i.group() + ':' + p.group(), 'user_pass': ''}
            result.append(proxy)
            count += 1
            if count == total:
                break
        return result

    def getIP(self):
        page = self.getFromWeb()
        return self.findIP(page)



