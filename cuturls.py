# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:cuturls.py
@time:2019/8/17 21:38
"""

file = open("./public/sitemap.xml")
file_urls = open('./curl-7.65.3-win64-mingw/bin/urls.txt','w')

for line in file:
    if ('<loc>' in line ):
        begin=line.find('<loc>')
        end=line.find('</loc>')
        file_urls.write(line[begin+5:end] + '\n')

    pass # do something

file_urls.close()
file.close()