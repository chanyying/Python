# def sayhello():
# 	print 'hello world!'

# def printMax(a,b):
# 	if a>b:
# 		print a,"is max"
# 	else:
# 		print b,"is max"


# def fun1(x):
# 	print "x is",x
# 	x=2
# 	print "changed local x to ",x

# def func():
#     global x

#     print 'x is', x
#     x = 2
#     print 'Changed local x to', x

# x = 50
# func()
# print 'Value of x is', x

def say(msg,time=1):
	print msg*time


def fun3(a,b=2,c=3):
	print "a is",a ,"and b is",b,"and c is",c
fun3(3, 7)
fun3(25, c=24)
fun3(c=50, a=100)