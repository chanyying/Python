# Python-Flasky-api

> 从配置环境开始，到一步一步写出api程序

#函数：

> dir():返回模块定义的名称列表
> del:删除 一个变量/名称
> delimiter.join()在一个元组里面插入间隔符

<h3>demo1.py</h3>

> 一个简单的hello wolrd！实例程序

<h3>demo2.py</h3>

> 利用while,break,continue,raw_input,input做一个简单的猜程序，当你输入正确的时候才会打印出相应的东西，否则一直循环下去。

<h3>demo3.py</h3>

> 讲解函数的使用，形参，实参，可选参数，默认参数等等的使用，根据参数名称输入参数值，这样可以避免因为参数的顺序导致错误的问题。

<h3>demo4.py</h3>

> <p>pass语句在Python中表示一个空的语句块。</p> 
> <p>没有返回值的return语句等价于return None,如果没有return就相当于pass</p>

<h3>demo5.py</h3>

> <p>DocStrings.__doc__的使用，显示在程序中DocStrings函数下的文档流</p>
> <p>如果在函数内有文档流的信息，...之间，“.”号视为换行隔开，这样如果在函数内，使用函数.__doc__就会显示出函数三个点之间的文档流</p>

<h3>demo6.py</h3>

>  - 如果你想要在其他程序中重用很多函数,demo6就讲到了怎样使用模块

>  - demo6写了一个简单的函数，当作模块使用，在demo6_2中用模块的方式去调用import
>  - 在demo6_2中有两种方式，一种是import
>  - demo6直接引入，但是要使用demo6中的函数的时候需要，demo6.sayhi()的方式 第二种是fromm demo6 import
>  - sayhi，在demo6中引入sayhi函数，fromm demo6 import
>  - sayhi，version就是引入这两个，如果需要引入全部，import *

# Data_structure

> 在这个文件夹中主要讲解Python的数据结构：Python中有三种内建的数据结构——列表、元组和字典

<h3>demo1.py</h3>

> 在程序demo1中的注释讲解了列表的使用

<h3>demo2.py</h3>

> 一个元组用括号()表示，一个空的括号代表一个空的元组，如果含有单个元组的情况下，必须在第一个（唯一一个）项目后跟一个逗号。
> 元组类似于其他语言中的数组，但是又不是，列表更像一种数组，Python中的元组主要用于print中，
> 在之前的demo中讲过%s的作用，在这里多个%s类似的做法就可以使用元组，元组随着print有定制的功能，%s表示字符串；%d表示整数。如果存在多个%s字符串，是根据后边的元组顺序来的；后面跟着%符号后的单个项目——没有圆括号的情况下。这只在字符串中只有一个定制的时候有效。

<h3>demo3.py</h3>

> 字典是dict类的实例/对象。字典就类似于一个对象，键值对就类似于一个对象中的key:value 键值对在字典中的标记：`d = {key1 : value1, key2 : value2}`。键/值对用冒号分割，而各个对用逗号分割，所有这些都包括在花括号中。
> 他们是没有顺序的，随机排序的，赋值：ab['Guido']；获取：ab['Swaroop']。都是同样的一种方法。

<h3>demo4.py</h3>
>列表、元组和字符串都是序列的一种。
>序列最重要的是：“索引操作符”和“切片操作符”。
>索引操作符：从序列中获取一个特定项目。
>切片操作符：从序列中获取一部分项目。
>Python从0开始计数；[1:3]输出的序列是1，2不包括第三个。[2:]包括2以后的所有序列项目。[1:-1]输出包括从第2个到倒数第二个，不包括最后一个；[:]显示所有序列
>[:]类似的操作符不只支持序列，还支持字符串的使用。你可以用相同的方法访问元组、列表和字符串。
<h3>demo5.py</h3>
>对象和与参考，程序中的第二种方法，删除这一个序列中的项目，另外一个不受影响的方法就是对象与参考。
>对于这样的形式，多个对象参考一个对象，就必须使用拷贝的形式将那个对象中的项目拷贝到这个项目，他们内容相同的，实质上是不同的，这样删除了这个，另外一个才不会受到影响。


#Simple-code

<h3>demo1.py</h3>
>类的使用

<h3>init.py</h3>
>__init__方法可以用来对你的对象做一些初始化 。
>__init__名称的开始和结尾都是双下划线。
>__init__方法会在类的一个对象被建立时立即运行

<h3>inherit.py</h3>
>一个函数可以没有参数的调用，但是在类之下定义的函数必须有一个参数，不然： sayHi() takes no arguments (1 given)，如果在没有参数的情况下，写self

<h3>using_file.py</h3>
>使用file函数创建一个文件，然后用创建的文件的write方式写入一个文本在创建的文件内

<h3>read_fileText.py</h3>
>这里同样用到了using_file.py文件中创建文件的file函数，但是没有指定参数方式，file如果没有指定参数方式就是默认的读取方式，读取这个文件，如果是ture就使用readline函数读取这个文件的每一行，然后进行判断，如果为空酒break返回，否则打印出文件的内容

<h3>pickling.py</h3>
>这个文件里面讲解了，储存器和pickle模块的使用，还有import...as...的使用。
