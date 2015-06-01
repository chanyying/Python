#coding:utf-8
#!/usr/bin/env python
# Filename: using_file.py

f=file('my.txt')#读取一个文件的内容，这里没有指定模式，默认就是读取模式
while True:
    line = f.readline()
    if len(line) == 0: # 如果文件内没有任何内容就返回
        break
    print line			
