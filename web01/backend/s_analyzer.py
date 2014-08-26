import json,urllib2
import threading,time
import redis_connector as redis
#import get_ip_source # I have moved the function to this file

province_dic={}

def get_region(url):
	#res = urllib2.Request(url)
        global province_dic
	result = urllib2.urlopen(url)
	region_dic = json.loads(result.read())
        #print province_dic
        #print region_dic
        #province = region_dic['data']['city']
        province = region_dic['province']
        print province
	if province_dic.has_key(province):
		province_dic[province] +=1
	else:
		province_dic[province] = 1
        #print region_dic

def handle(fname):
	f = file(fname)
	hour_end_time = float(f.readline().split()[0]) + 3600 
	ip_hour_dic = { hour_end_time : {'total_pv': 0 }  }
	uv_dic = {}
	region_ip_dic = {}
	cache_type_dic = {}
	for line in f.xreadlines():
		line = line.split()
 		access_time,raw_ip , cache_type, response_size,request_url,content_type,MIME_content_type= float(line[0]) ,line[2], line[3],line[4],line[6],line[9],line[11]
		if access_time < hour_end_time : # put this record into this time period 
			ip_hour_dic[hour_end_time]['total_pv'] +=1 
			
		else:
			hour_end_time +=3600 
			ip_hour_dic[hour_end_time] = {'total_pv': 1}
			#print hour_end_time
		# handle uv 
		if uv_dic.has_key(raw_ip):
			uv_dic[raw_ip] +=1
		else: 
			uv_dic[raw_ip] = 1
		#handle region ranking 
		internet_ip, intranet_ip = raw_ip.split('/')
		region_ip = '.'.join(internet_ip.split('.')[:2])
		if region_ip_dic.has_key(region_ip):
			region_ip_dic[region_ip][0] += 1
		else :
			region_ip_dic[region_ip] = [1, internet_ip]
		#handle squid request status
		cache_type = cache_type.split('/')[0] 
		if cache_type_dic.has_key(cache_type):
			cache_type_dic[cache_type] +=1
		else:
			cache_type_dic[cache_type] = 1


	#print ip_hour_dic
	#print len(uv_dic)
	#print 'InternetIP : ', len(region_dic)
	#print 'Cache types:', cache_type_dic

        #start get ip source





	sorted_region_ip_list = sorted(region_ip_dic.items(), key=lambda x:x[1][0])[:20]
	for i in sorted_region_ip_list:
		#get all regions
                #print i
                if "%20" in i[1][1]:
                    i = i[1][1].split('%20')[1]
                else:
                    i = i[1][1]
                #print i[1][1] 
                #print i
                url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=%s' % i
                get_region(url)
                time.sleep(0.15)
        #print province_dic


		#p=threading.Thread(target=get_region, args=(url,) )
                #threads.append(p)
		#p.start()

	result_dic = {
		'ip_hour_dic' : ip_hour_dic,
		'cache_type_dic': cache_type_dic,
                'province_dic': province_dic
	}

        #print result_dic['province_dic']

if __name__ == '__main__':
	result = handle('log25w.log')			
	#result = handle('/usr/local/squid/var/logs/squid_access.log')			
	redis.r['SQUID_LOG'] =  json.dumps(result)
	#handle('../squid_access.log')			
