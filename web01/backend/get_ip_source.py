import json,urllib2

province_dic={}

def get_region(url):
	#res = urllib2.Request(url)
	result = urllib2.urlopen(url)
	region_dic = json.loads(result.read())
        #print region_dic
        province = region_dic['data']['region']
	if province_dic.has_key(province):
		province_dic[province] +=1
	else:
		province_dic[province] = 1
        #print province_dic


if __name__ == '__main__':
    get_region('http://ip.taobao.com/service/getIpInfo.php?ip=112.224.19.48')
