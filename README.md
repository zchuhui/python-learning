# Python 简介
Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。

- Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。
- Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
- Python 是交互式语言： 这意味着，您可以在一个 Python 提示符 >>> 后直接执行代码。
- Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
- Python 是初学者的语言：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

教程：https://www.runoob.com/python3/python3-tutorial.html

#### 基础操作

#### 查看 Python 版本
```
python -V
```

#### 命令行运算
咱命令行输入 `py`,即可开始敲代码。
```
> py
>>> 
```

#### 执行 Python 文件

将代码写在 `index.py`中，然后用命令行执行：
```
py index.py
```


# 基础语法



目录
[TOC]

# 一、注释
```
# this is a comment （注释）
print('hello world!')
```



# 二、变量
```
x = 5
y =  'this is yyyy!!!'

print(x)
print(y)


a, b, c = "A","B","C"
print(a,b,c)


a1 = a2 = a3 = "this is A"
print(a1,a2,a3)
```

## 2.1 合法的变量命名
```
myvar = "Gary"
my_var = "Gary"
_my_var = "Gary"
myVar = "Gary"
MYVAR = "Gary"
myvar2 = "Gary"

```

## 2.2 不合法的变量命名
```
2myvar = "Gary"
my-var = "Gary"
 my var = "Gary"
```

## 2.3 全局变量
全局的变量，是可以在局部的函数内进行修改的
```
t = "Tri"

def myfunc():
    global x
    t = "Tom!"
    print('t value:'+t)

myfunc()  
# t value: Tom!
```

函数里面，也可以定义全局变量，要使用`global`关键字
```
def myfunc():
    global t
    t = "Tom!"
    print('t value:'+t)

myfunc()    # t value: Tom!
print(t)    # Tom!
```



# 三、数据类型

- 字符类型：`str`
- 数字类型：`int`,`float`,`complex`
- 序列类型：`list`,`tuple`,`rangle`
- 映射类型：`dict`
- 集合类型：`set`,`frozenset`
- 布尔类型：`bool`
- 二进制类型：`bytes`,`bytearray`,`memoryview`

使用 `type()` 方法，可以获取变量的数据格式。
```
x = "this is str type"
print(type(x))   # <calss 'str'>
```


## 3.1  Str （字符串类型）

字符串类型用双引号或单引号是一样的：
```
print('hello')   # hello
print("hello")   # hello
```

多行字符串写法，用三个 `"""` 或者 `'''` :
```
x = """one,
two,
three
"""

print(x)

# 输出以下：
#one,
#two,
#three
```

字符串同时也可以当数组使用，操作如下：
```
x = "Hello！"

print(x[0])  # H
```

也可以指定范围切块，比如下面的从 0 开始，切 3 个字符
```
x = "Hello！"

print(x[0:3])  # Hel
```

也可以倒过来切块：
```python
x = "Hello, world"

print(x[-4:-1]) # orl
```

获取字符串的字符长度可以用 `len()`方法，使用如下：
```python
x = "Hello, world"

print(len(x))  # 12
```


字符串还有一些内置的方法可以使用

- strip()  去掉前后的空符号
```python
x = " Hello, world"
print(x.strip())   # returns "Hello, world"
```python

- lower()  转小写
```python
x = "Hello, World"
print(x.lower())  # hello, world
```

- upper() 转大写
```python
x = "Hello, World"
print(x.lower())  # HELLO, WORLD
```

- replace()  替换字符
```python
x = "Hello, world"
print(x.replace(',',":"))   # Hello: world
```

- split() 转数组
```python
x = "Hello, world"
print(x.split(','))  # ['Hello', ' world']
```

- format() 格式化
当变量的类型不一样时，是不能拼接的，比如数组+字符串就会报错，所以需要用到 `format()` 做一个格式化，如：
```python
# 错误的写法
n = 22
s = "my age is" + n
print(s)    # 报错


# 正确的写法 1
n = 22
s = "my age is {}" 
print(s.format(n))

# 正确的写法 2
n1,n2 = 22,"tom"
s = "my age is {} and {}" 
print(s.format(n1,n2))


```



检查某些值是否在字符串内时，可以使用 `in` 或 `not in`，如下：
```python
x = "Hello, world"
a = 'He' in x
print(a)  # true
```

[更多](https://www.w3schools.com/python/python_strings.asp)




## 3.2 Number 类型

number 类型有三种：
- int       整数
- float     浮点数
- complex   混合数

案例如下：
```python
x = 1   # int
y = 3.8 # float 
k = 1jk # comlex

# 用type() 检查类型
print(type(x))   # <class 'int'>
print(type(y))   # <class 'float'>
print(type(k))   # <class 'complex'>
```


### int
`int` 是整数，包括正数、负数，0

```python
x = 1
y = 0
z = -3255522

print(type(x),type(y),type(z))
# <class 'int'> <class 'int'> <class 'int'>
```

### float
`float` 是浮点数，必须有小数点，最少一位，当然也正数、负数。
```python
x = 1.10
y = 1.0
z = -35.59

print(type(x),type(y),type(z))
# <class 'float'> <class 'float'> <class 'float'>
```


### complex 
complex 是复杂类型，就是数值的尾部都有`j`字段。
```python
x = 3+5j
y = 5j
z = -5j

print(type(x),type(y),type(z))
# <class 'complex'>  <class 'complex'>  <class 'complex'>
```


### type Conversion (类型转换)
数字的三种类型 `int`,`float`, `complex` 是可以相互转换的，对应的方法是 `int()`, `float()`, `complex()`。
不过注意的一点是，`int`,`float`可以直接转成 `complex`, 而 `complex` 不能直接转成前者。

```python
x = 1
y = 1.2
z = 5j

print(int(y))      # 1
print(float(x))    # 1.0
print(complex(y))  # (1.2+j)
print(int(z))      # TypeError: can't convert complex to int
```
如代码所示，如果 `complex` 类型试图转成 `int` 或 `float`, 则会报错：`TypeError: can't convert complex to int`


### Random Number （随机数）
Python 并没有可以直接转换的 `random` 方法，需要自己导入 `random` 模块。

```python
import random
print(random.randrange(0,10))
```



## 3.3 Casting (定义变量类型)

在声明一个变量时，可以定义变量的类型。

```python
x = int(1.2)
y = float(9)
z = str('myname')

print(x,y,z)  # 1 9.0 myname
```

这点跟转换有点类似，`complex` 类型同样不能直接互转。



## 3.4 Boolean （布尔类型）

`Boolean` 类型看起来很简单，但它却是编写程序是最常用的类型之一。
`Boolean` 类型只有两个值：`True` and `False`

常用的判断：
```python
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False
```

语句判断：
```python
a,b = 1,2

if a > b :
    print('A')
else:
    print("B")

# output B
```

还可以使用 `bool()` 方法来判断值，但变量有值时，通常都会返回 `True`, 反之 返回 `False`。

值不为空时，返回True。
```python
print(bool("Hello"))  # True
print(bool(15))       # True
print(bool([1,2,3]))  # True
```

值为空时，返回 False。
```python
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```


## 3.5 可更改与不可更改的对象

在 python 中，string,tuple,number 属于不可更改的对象。而 list,dist 等则是可以修改的对象。

- 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
- 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。



## 4. 运算符

Python 的运算符，可以分为以下几种：
- 算术运算符
- 赋值运算符
- 比较运算符
- 逻辑运算符
- 身份运算符
- 成员运算符
- 位运算符
  
  
### 4.1 算术运算符 (Arithmetic operators)

算术运算符，即数值直接的计算。

| 符号 | 名称 | 案例 | 
|:--:|:--:|:--:|
| + | 加 | x + y | 
| - | 减 | x - y | 
| * | 乘 | x * y | 
| / | 除 | x / y | 
| % | 模数 | x % y | 
| ** | 幂 | x ** y | 
| // | 向下取整 | x // y | 


### 4.2 赋值运算符 （Assignment Operators）


### 4.3 比较运算符（Comparison Operators）


## 5. 数组

Python 中有四种集合数据类型：

- List（数组）`有序，可更改，允许重复`
- Tuple（元组） `有序，不可更改，允许重复`
- Set（集合） `无序、无索引，不可重复`
- Dictionary（字典）`无序，有索引，可更改，不可重复`

### 5.1 List

List 数组是最常用的集合，它的特点是：有序，有索引，可更改，可重复。

list 获取:

```python
myList = ['Monday','Tuesday',1,2]

print(myList)      # 输出数组 "['Monday', 'Tuesday', 1, 2]"

print(myList[0])   # 输出第一个 "Monday"

print(myList[-1])  # 负数输出最后一个 "2"

print(myList[1:3]) # 输出范围，从索引1开始，到索引3结束，不包括3，输出“【’Tuesday‘,1】”

print(myList[-4:-1])  # 负索引输出范围，倒过来输出  “【'Monday', 'Tuesday', 1]”

```

list 的新增，用 append() 与 insert() ，前者用于最后插入，后者用于指定位置插入，把其他的成员后推。

```python
myList = ['Monday','Tuesday',1,2]

myList.append('Sunday')
print(myList)   # ['Monday', 'Tuesday', 1, 2, 'Sunday']

myList.insert(0,'Good!')
print(myList)   # ['Good!', 'Monday', 'Tuesday', 1, 2, 'Sunday']

```

list 修改，只需指定序号：

```python
myList = ['Monday','Tuesday',1,2]
myList[0] = 0
print(myList)      # [0, 'Tuesday', 1, 2]
```

list 删除，用一下内置函数：

- remove()  `删除成员`
- pop()     `指定索引删除，没有索引则删除最后一项`
- del()   `指定索引删除，也能删除整个list`
- clear()  `清空数组`

```python
myList = ['Monday','Tuesday',1,2]
myList.remove('Monday')
print(myList) # ['Tuesday', 1, 2]

myList = ['Monday','Tuesday',1,2]
myList.pop(0)
print(myList)  # ['Tuesday', 1, 2]

myList = ['Monday','Tuesday',1,2]
del myList[0]
print(myList)  # ['Tuesday', 1, 2]

# del myList     # 删除后，这 个list 没了
# print(myList)  # NameError: name 'myList' is not defined

myList = ['Monday','Tuesday',1,2]
myList.clear()
print(myList)    # []

```


list 遍历：

```python
for x in myList:
  print(x)
```

检查是否存在：

```python
myList = ['Monday','Tuesday',1,2]

if 1 in myList :
  print('true')
else:
  print('false')

# true
```



### 5.2 Tuple 元组

元组与类似，不同之处在于元组的元素不能修改。还有，数组使用 `[]`,而元组使用 `()`。

#### 简单用法

简单的 Tuple 如下：
```
tup0 = ()   # 创建一个空 Tuple 
tup1 = (1,3,'name1','name2')
tup2 = (2100,300,5000)
tup3 = "a","b","c","d"  # 不用括号也可以 

print(tup0)  # ()
print(tup1)  # (1, 3, 'name1', 'name2')
print(tup2)  # (2100, 300, 5000)
print(tup3)  # ('a', 'b', 'c', 'd')
```

访问 Tuple 的方式基本与列表一致：
```
tup1 = (1,2,3,4,5,6)

print('tup1[0]',tup1[0])       # 1
print('tup1[1:3]',tup1[1:3])   # (2,3)
```

Tuple 的值不能修改的，只能拼接。
```
tup1 = (1,2,3,4,5,6)
tup2 = ('name1','name2')
tup3 = tup1 + tup2 

print(tup3) # (1, 2, 3, 4, 5, 6, 'name1', 'name2')
```

Tuple 的值也是不允许删除子元素的，只能整个删除。
```
tup1 = (1,2,3,4,5,6)
del tup1

print(tup1)   # NameError: name 'tup1' is not defined
```


#### 元组也有运算符

| 表达式 | 结果 | 描述 | 
|:--:|:--:|:--:|
| len((1,2,3)) | 3 | 计算元素个数 | 
| (1,2,3)+(4,5,6) | (1,2,3,4,5,6) | 连接 | 
| ('a')*3 | ('a','a','a') | 复制 | 
| 3 in (1,2,3) | True |  判断元素是否存在 |
| % | 模数 | x % y | 
| ** | 幂 | x ** y | 
| for x in (1, 2, 3):print (x) | 1 2 3  | 遍历 | 



#### 内置函数
| 方法 | 实例 | 描述 | 
|:--:|:--:|:--:|
| len(tuple) | len((1,3,4,5)) | 计算元素个数 | 
| max(tuple) | max((1,3,4,5)) | 取最大值 | 
| min(tuple) | min((1,3,4,5)) | 取最小值 | 
| tuple(array) | tuple([1,3,4,5]) | 将其他数组转为Tuple  | 



### 5.3 字典 

#### 创建
字典就是 JavaScript 的对象（Object），键值写法。
但要记住：
- 键是唯一的，如果一个键被赋值两次，则只会取后面的值
- 键可以用字符串、数字、或元组充当，缺是不可变的。


```
dict = {"name":"Geogle","sex":"男"}
print(dict)  # {'name': 'Geogle', 'sex': '男'}
```

不同的是，在 JavaScript 中，键只能是字符串，而在这里没有限制。
```
 d1 = {1:11,1.1:1.1}
 print(d1)   # {1: 11, 1.1: 1.1}
```


#### 访问

元素的访问，用键：
```
d1 = {1:11,1.1:1.1,'name':'Mock'}
print(d1[1])   # 11
```


#### 修改
元素的修改，也用键：
```
d1 = {1:11,1.1:1.1,'name':'Mock'}
d1[1]  1000
print(d1[1])   # 1000
```

#### 删除

删除有 2 种方式：
- del 
- clear 

del 即可删除子元素，也可以删除整个字典。
```
d1 = {1:100,'name':'Mock'}
del d1[1]
print(d1)   # {'name':"Mock"}


del d1  
print(d1)   # NameError: name 'd1' is not defined
```

clear 只是清除所有子元素：

```py
d1 = {1:11,1.1:1.1}
d1.clear()
print(d1)  # {}
```

#### 内置函数

| 方法 | 实例 | 描述 |
|:--:|:--:|:--:|
| len(dict) | len({1:1,2:222}) | 计算键的总数 |
| str(tuple) | str({1:1,2:222}) | 转字符串 |
| type(tuple) | type({1:1,2:222}) | 返回类型 |

### 5.3 Set（集合）

Set（集合）是另类的数组，跟 List 不一样，Set 是无序的、不重复的。

创建集合，可以使用 `{}` 跟 `set()`，但创建空的集合只能使用 `set()`。

```py
mySet = {'a','d','5',1,'a'}

# 打印
print(mySet)         # {'5', 1, 'a', 'd'}
# 判断元素是否在集合里面
print('a' in mySet)  # True


# 使用 set() 创建
mySet2 = set("abcdefg"),
mySet3 = set("cde")
mySet4 = set({'a','bb'})
print(mySet2) # {'g', 'c', 'b', 'f', 'e', 'd', 'a'}
print(mySet3) # {'e', 'd', 'c'}
print(mySet4) # {'bb', 'a'}
```

一些操作：

```py

# 操作
# 新增
s = set({'a','b','c'})
s.add('dd')
print(s)   # {'a', 'b', 'c', 'dd'}

s.update('ee')
print(s)   # {'a', 'dd', 'e', 'b', 'c'}

s.update({'x1','x2'})
print(s) # {'e', 'x2', 'c', 'a', 'x1', 'b', 'dd'}


# 移除 
s.remove('a')   # 如元素不存在会发生错误
print(s)  #{'c', 'b', 'x2', 'e', 'x1', 'dd'}

s.discard('a')  # 如元素不存在不会发生错误
print(s)

# 移除最后一位
s.pop()
print(s)


# 获取长度
print(len(s))   # 5

# 清空
print(s.clear())  # None
```

# 四、判断、循环语句

## 4.1 条件：if...elif...else

示例：

```py
if val == 10:
  print(10)
elif val == 50:
  print(50)
else:
  print('no')
```

## 4.2 white 循环

示例：

```py

val = 1

while(val < 10):
  print(val)
  val += 1
```

## 4.3 for...in 循环

示例1：

```py

list = ['a','b',4,5,6]

for x in list:
  print(x)
```

示例2：

```py
list = ['a','b',4,5,6]

for x in list:
  print(x)
  if(x == 'b'):
    break          # 跳出循环

```

## 4.4 range() 函数：遍历数字序列

示例1：

```py
for i in range(4):
  print(i)

>> 0
>> 1
>> 2
>> 3
```

## 4.5 迭代器与生成器

### 迭代器 `iter()` 与 `next()`

迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。

```py
list= [1,3,4,5,6]
it = iter(list)     # 创建一个迭代器

# 输出迭代器的下一个元素
print(next(it)) # 1
print(next(it)) # 3
print(next(it)) # 4
print(next(it)) # 5
print(next(it)) # 6
```

### 生成器 yield
.....


# 五、函数 

## 5.1 定义 函数

在python里定义一个函数的规则是：

- 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

函数格式如下：

```py
def funName ( params ):
  # ....
```

如：

```py
# 计算面积的函数
def getArea(w,h):
  return w*h

w = 100
h = 10
# 调用函数
print('area:',getArea(w,h))    # 1000

```

## 5.2 参数

python 参数有四种类型：

- 必须参数
- 关键字参数
- 默认参数
- 不定长参数

```py
# 必须传入一个参数，否则报错   
def printName(name):
  print('my name is ',name)

printName("gary")         


# 关键字参数，可以不按照顺序传入
def printInfo(name,age):
  print('my name is ',name)
  print('my age is ',age)

printInfo(age=19, name="Marry")


# 默认参数，可以不传
def printInfo2(name,age= 13):
  print('my name is ',name)
  print('my age is ',age)

printInfo2(name="Marry")


# 传入不定长参数
def printMoreInfo(arg1,*args):
  "打印传入的所有参数"
  print("input:")
  print(arg1)
  print(args)

printMoreInfo(10,45,6,7,7,8)

# input:
# 10
# (45, 6, 7, 7, 8)
```

## 5.3 匿名函数

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
匿名函数的定义如下：

```py
lambda [arg1 [,arg2,.....argn]]:expression
```

匿名函数的定义如下：

- lambda 只是一个表达式，函数体比 def 简单很多。
- lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
- lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
- 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

```py
# 写一个sum函数
sum = lambda arg1,arg2: arg1 + arg2

print('sum',sum(10,45))
```

# 六、模块



