#coding=utf-8
import json,urllib2,csv,sys
import time
import ipsearch

province_dic = {}

def get_region(url):
    result = urllib2.urlopen(url)
    region_dic = json.loads(result.read())
    global province_dic
    province = region_dic['city']
    if province_dic.has_key(province):
        province_dic[province] +=1
    else:
        province_dic[province] = 1

def handle(fname):
    f = file(fname)
    region_ip_dic = {}
    for line in f.xreadlines():
        line = line.split()
        access_time,raw_ip , cache_type, response_size,request_url,content_type,MIME_content_type= float(line[0]) ,line[2], line[3],line[4],line[6],line[9],line[11]
        internet_ip, intranet_ip = raw_ip.split('/')
        region_ip = '.'.join(internet_ip.split('.')[:2])
        if region_ip_dic.has_key(region_ip):
            region_ip_dic[region_ip][0] += 1
        else :
            region_ip_dic[region_ip] = [1, internet_ip]

    sorted_region_ip_list = sorted(region_ip_dic.items(), key=lambda x:x[1][0])[:100]
    ct = 0
    for i in sorted_region_ip_list:
        ct = ct +1
        if "%20" in i[1][1]:
            i = i[1][1].split('%20')[1]
        else:
            i = i[1][1]
        url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=%s' % i
        get_region(url)
        time.sleep(0.15)
        sys.stdout.write('%d%% have done \r' %(ct))
        sys.stdout.flush()

    result_dic = {
        'province_dic': province_dic
    }

    return result_dic

if __name__ == '__main__':
    result = handle('log25w.log')
    def get_squid_log(result):
        squid_data = result

        ppie_list = []
        for k,v in squid_data['province_dic'].items():
            ppie_list.append([k,v])

        f = csv.writer(open("test.csv","wb+"))
        f.writerow(["province","click"])

        for i in ppie_list:
            i0 = i[0].encode('gb2312')
            f.writerow([i0,i[1]])
    get_squid_log(result)
