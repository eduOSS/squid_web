#coding=utf-8
import json,urllib2,csv,sys
import time
import ipsearch

region_ip_dic = {}

def alex_method(internet_ip):
    """docstring for alex_method"""
    global region_ip_dic
    region_ip = '.'.join(internet_ip.split('.')[:2])
    if region_ip_dic.has_key(region_ip):
        region_ip_dic[region_ip][0] += 1
    else :
        region_ip_dic[region_ip] = [1, internet_ip]
    #sorted_region_ip_list = sorted(region_ip_dic.items(), key=lambda x:x[1][0])[:100]
    #return sorted_region_ip_list

def get_region_ip_list(fname):
    f = file(fname)
    for line in f.xreadlines():
        line = line.split()
        access_time,raw_ip , cache_type, response_size,request_url,content_type,MIME_content_type= float(line[0]) ,line[2], line[3],line[4],line[6],line[9],line[11]
        internet_ip, intranet_ip = raw_ip.split('/')
        if "%20" in internet_ip:
            internet_ip = internet_ip.split('%20')[1]
        alex_method(internet_ip)
    sorted_region_ip_list = sorted(region_ip_dic.items(), key=lambda x:x[1][0])[:100]
    return sorted_region_ip_list

def handle():
    province_dic = {}
    region_ip_list = get_region_ip_list('log25w.log')
    ct = 0
    for i in region_ip_list:
        ct = ct +1
        #url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=%s' % i
        #get_region(url)
        i = i[1][1]
        line_items = ipsearch.IPSearch(i)
        province,city = line_items[3].encode('gb2312'),line_items[4].encode('gb2312')
        if province_dic.has_key(province):
            province_dic[province] +=1
        else:
            province_dic[province] = 1
        sys.stdout.write('%d%% have done \r' %(ct))
        sys.stdout.flush()
        province_list = []
        for k,v in squid_data['province_dic'].items():
            province_list.append([k,v])

        f = csv.writer(open("test.csv","wb+"))
        f.writerow(["province","click"])

        for i in ppie_list:
            i0 = i[0].encode('gb2312')
            f.writerow([i0,i[1]])
    get_squid_log(result)



if __name__ == '__main__':
    result = handle
    def get_squid_log(result):
        squid_data = result

