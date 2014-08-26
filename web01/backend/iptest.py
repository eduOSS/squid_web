#references:
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


import urllib2,json
url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=58.198.191.100'
result = urllib2.urlopen(url)
json_result = json.loads(result.read())
print json_result
