#coding:utf-8
#!/usr/bin/env python
# Filename: pickling.py

import cPickle as p
#import pickle as p

shoplistfile='shoplist.data'
# the name of the file where we will store the object

shoplist=['apple','mango','carrot']

# Write to the file
f=file(shoplistfile,'w')
p.dump(shoplist,f) # dump the object to a file
f.close()

del shoplist # remove the shoplist

# Read back from the storage
f=file(shoplistfile)
storedlist=p.load(f)
print storedlist

#import cPickle as  p的意思是，讲引入的模块用P表示，在以后的正文中，都可以使用P代替cPIickle来使用。
#至于cPickle和pickele这都是使用它你可以在一个文件中储存任何Python对象，而且可以完整的取出来。就是用来存储对象的。pickle比cpickle快
