#pass语句在Python中表示一个空的语句块。
#没有返回值的return语句等价于return None,如果没有return就相当于pass

def fn(x, y):
    if x > y:
        return x
    else:
        return y

print fn(12, 3)