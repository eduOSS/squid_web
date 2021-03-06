#coding=utf-8
import json,urllib2,csv,sys,os
import time
import ipsearch

def get_region_ip_list(ip_list):
    """docstring for alex_method"""
    region_ip_dic = {}
    region_ip_list = []
    related_ip_number = 0
    for i in ip_list:
        region_ip = '.'.join(i.split('.')[:2])
        if region_ip_dic.has_key(region_ip):
            region_ip_dic[region_ip][1] += 1
        else :
            region_ip_dic[region_ip] = [i,1]
    print "length of region ip dic",len(region_ip_dic)
    sorted_region_ip_list = sorted(region_ip_dic.items(), key=lambda x:x[1][1],reverse = True)[:100]
    for j in sorted_region_ip_list:
        region_ip_list.append(j[1])
        related_ip_number += j[1][1]
    print 'related ip number: ',related_ip_number
    return region_ip_list

def raw_decrease_ip_list(ip_list):
    """docstring for alex_method"""
    related_ip_number = 0
    ip_dic = {}
    decreased_ip_list = []
    for i in ip_list:
        if ip_dic.has_key(i):
            ip_dic[i] += 1
        else :
            ip_dic[i] = 1
    #decreased_ip_list = sorted(ip_dic.items(), key=lambda x:x[1])[:100]
    for k,v in ip_dic.items():
        temp = [k,v]
        decreased_ip_list.append(temp)
        related_ip_number += v
    print 'related ip number: ',related_ip_number
    return decreased_ip_list

def get_ip_list_from_log(logfile):
    error_line_num = 0
    ip_list = []
    f = file(logfile)
    for raw_line in f.xreadlines():
        line = raw_line.split()
        access_time,raw_ip , cache_type, response_size,request_url,content_type,MIME_content_type= float(line[0]) ,line[2], line[3],line[4],line[6],line[9],line[11]
        internet_ip, intranet_ip = raw_ip.split('/')
        if "%20" in internet_ip:
            internet_ip = internet_ip.split('%20')[1]
        if '-' in internet_ip:
            error_line_num += 1
            #sys.exit()
            continue
        ip_list.append(internet_ip)
    print 'error line number',error_line_num
    return ip_list

def get_province_list(ip_list):
    """docstring for get_province_list"""
    province_dic = {}
    province_list = []
    for i in ip_list:
        chosen_ip_info = ipsearch.IPSearch(i[0])
        #province,city = line_items[3].encode('gb2312'),line_items[4].encode('gb2312')
        province,city = chosen_ip_info[3],chosen_ip_info[4]
        if province_dic.has_key(province):
            province_dic[province] += i[1]
        else:
            province_dic[province] = i[1]
    sorted_province_list = sorted(province_dic.items(), key=lambda x:x[1], reverse = True)
    return sorted_province_list

def write_to_excel(province_list):
    f = csv.writer(open("region_test.csv","wb+"))
    f.writerow(["province","click"])
    for i in province_list:
        #i[0] = i[0].encode('gb2312')
        f.writerow([i[0],i[1]])

def main():
    """docstring for main"""
    ip_list = get_ip_list_from_log('log25w.log')
    print 'total ip number: ',len(ip_list)
    decreased_ip_list = get_region_ip_list(ip_list)
    #decreased_ip_list = raw_decrease_ip_list(ip_list)
    print 'choose ',len(decreased_ip_list),'ip to search ip'
    province_list = get_province_list(decreased_ip_list)
    print 'related province number: ',len(province_list)
    write_to_excel(province_list)
    print 'have writen to excel'

if __name__ == '__main__':
    main()
