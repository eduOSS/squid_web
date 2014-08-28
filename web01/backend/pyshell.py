#references:
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


import os,subprocess
#handle = subprocess.Popen("ls -l",stdout=subprocess.PIPE,shell=True)
#print handle.stdout.read()
print int(os.popen("wc -l ipv2.txt").readline().split()[0])+1
