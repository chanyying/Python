#coding:utf-8

shoplist=['apple','mango','carrot','banana']
#首先定义一个序列
mylist=shoplist
#将shoplist的序列赋值给mylist，这样两个mylist就等于shoplist了。
del shoplist[0]
#删除shoplist当中的第一个
print 'shoplist is',shoplist
print 'mylist is',mylist
#输出的答案是相同的：[mango','carrot','banana']，因为你删除了shoplist当中的就等于删除了mylist当中的。
#怎样实现，删除两个相等的序列当中的一个，另外一个序列不受影响呢？方法如下：

#mylist等于shoplist当中的项目，将shoplist当中的全部项目赋值给mylist
mylist=shoplist[:] 
del mylist[0]
#删除mylist当中的第一个
print 'shoplist is', shoplist#shoplist还是shoplist
print 'mylist is', mylist#mylist显示的就是除删除的第一个之外的
