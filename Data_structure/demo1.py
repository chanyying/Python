#coding:utf-8
# 最开始我的列表中有四个项目
shoplist = ['apple', 'mango', 'carrot', 'banana']
print 'I have', len(shoplist),'items to purchase.'



# 用遍历的方式，循环出来，他们分别是：
print 'These items are:',
for item in shoplist:
    print item,

# \n是回车的意思，我向我的列表末尾添加了rice，我的列表现在是
print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist



#我将对我的列表进行整理
print 'I will sort my list now'
shoplist.sort()
#sort函数可以对[,]进行排序
print 'Sorted shopping list is', shoplist

# \是转义符，%s 是后边的%shoplist[0]，我将买掉列表中的第一个
print 'I\'ll buy %s, the first one.' %shoplist[0]


# print 'I bought the', shoplist[0]
# #从列表中删除第一个项目
# del shoplist[0]
# #现在的列表是：
# print 'My shopping list is now', shoplist
#这里的注释块也可以这样写：



#将买掉的第一个赋值给olditem，全局使用不受影响
olditem = shoplist[0]
#然后删除买掉的第一个
del shoplist[0]
del olditem
#显示我买的第一个项目，用全局变量，如果不定义给全局变量，依然是shoplist[0]就会显示为删除shoplist[0]之后，就会显示后面的接着的第一个，banana
#为什么会显示banana，因为排序了
print 'I bought the', shoplist[0]
#然后再显示，删除第一个项目之后的shoplist
print 'My shopping list is now', shoplist
