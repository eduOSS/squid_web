#references:
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


import socket, struct
def testipv2(ipadd):
    """docstring for testipv2"""
    num_ip = struct.unpack("!I",socket.inet_aton(ipadd))[0]

    print num_ip

import urllib2,json
def testapi():
    """docstring for testapi"""
    url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=58.198.191.100'
    result = urllib2.urlopen(url)
    json_result = json.loads(result.read())
    print json_result

    def iptest():
        """docstring for iptest"""
        print "hello"

#import geoip2.database
def testgeoip():
    """docstring for testgeoip"""
    path_to_GeoLite2_City.mmdb = os.path.abspath(os.path.join(os.path.curdir,"GeoLite2-City.mmdb"))
    reader = geoip2.database.Reader(path_to_GeoLite2_City)
    response = reader.city('112.224.19.48')
    print response.country.name,response.subdivisions.most_specific.name,response.city.name
    reader.close()

import os,sys,linecache
ct = 0
def IPSearch(ip_add):
    global ct
    """docstring for BSearch"""
    #print ip_add
    try:
        ip_key = struct.unpack("!I",socket.inet_aton(ip_add))[0]
    except:
        sys.exit()

    file_name = "ipv2.txt"
    low = 0
    ip_file = open(file_name,'r')
    high = int(os.popen("wc -l ipv2.txt").readline().split()[0]) - 1
    i = 0
    while low <= high:
        i = i + 1
        mid = (low+high) / 2
        file_line = linecache.getline(file_name,mid)
        line_items = file_line.split("|")[2:7]
        if ip_key >= int(line_items[0]) and ip_key <= int(line_items[1]):
            #print line_items[3].encode('gb2312'),line_items[4].encode('gb2312')
            #print line_items,ip_key
            ct += 1
            sys.stdout.flush()
            sys.stdout.write('%d done \r' %(ct))
            return line_items
        else:
            if ip_key < int(line_items[0]):
                high = mid -1
            else:
                low = mid + 1
    else:
        print "404 error"

if __name__ == '__main__':
    ip_add = '112.224.19.48'
    IPSearch(ip_add)
