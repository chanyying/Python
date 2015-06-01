#coding:utf-8
#!/usr/bin/env python
# Filename: using_file.py

text = '''\
你好
'''

f=file('my.txt','w')#用write写的权限，创建一个文件
f.write(text)#在创建的my.txt文件中写入text文档进去
