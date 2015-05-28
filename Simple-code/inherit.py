#coding:utf-8
#!/usr/bin/env python
# Filename: inherit.py



#编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal:
    def run(self):
        print 'Animal is running...'


# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
# p=Animal().run()  打印出Animal的内容
#这个时候如果单独调用Dog类，后面没有跟调用这个类的什么方法，所以为空
# Dog()
#因为在Dog的类参数里面调用了Animal类，所以可以直接调用Animal里面的函数，下边的例子就成功了
# Dog().run()


class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

#在Dog类当中继承Animal类，并添加新方法,这个时候如果调用这个run()函数，就会执行Dog类的run函数，覆盖了Animal类的run了，这就是多态性
# Dog().run()

class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Tortoise())