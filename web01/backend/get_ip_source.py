#import json,urllib2
#
#province_dic={}
#
#def get_region(url):
#	#res = urllib2.Request(url)
#	result = urllib2.urlopen(url)
#	region_dic = json.loads(result.read())
#        print region_dic
#        #print province_dic
#        #return region_dic
#        province = region_dic['city']
#        print province
#	#if province_dic.has_key(province):
#	#	province_dic[province] +=1
#	#else:
#	#	province_dic[province] = 1
#
#
#if __name__ == '__main__':
#    url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=112.224.19.48'
#    get_region(url)
