# 0 Python 基础语法

在算法开发中，理解数据在内存中的存储形式及其转换方式是编写高效代码的基础。Python 作为动态强类型语言，其处理数据的方式非常灵活。

---
# 1 数据类型及转换
## 1.1 基础数据类型 (Basic Data Types)

Python 中的基础数据类型主要分为以下几类：

### 1.1.1 数值型 (Numeric)
* **整型 (`int`)**: Python 3 的整型是**动态长度**的，意味着它不会像 C++/Java 那样出现溢出（Overflow）问题，可以处理任意大小的整数。
* **浮点型 (`float`)**: 对应 C 语言中的 `double`，采用双精度浮点数标准（IEEE 754）。
* **布尔型 (`bool`)**: 只有 `True` 和 `False` 两个值，在底层逻辑中分别对应 `1` 和 `0`。

### 1.1.2 序列型 (Sequence)
* **字符串 (`str`)**: 不可变的字符序列，支持强大的切片（Slicing）操作。



| 类型 | 关键字 | 示例 | 备注 |
| :--- | :--- | :--- | :--- |
| 整型 | `int` | `1024`, `-5` | 无限精度 |
| 浮点型 | `float` | `3.14`, `2e-3` | 支持科学计数法 |
| 布尔型 | `bool` | `True`, `False` | 逻辑判断核心 |
| 字符串 | `str` | `"Hello"`, `'Python'` | 单双引号通用 |

## 1.2 类型检查

在算法调试时，我们经常需要确认变量的类型。

```python
x = 10
y = 3.14
z = "Algo"

print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(isinstance(z, str)) # True (更推荐的检查方式)
```

## 1.3 数据类型转换 (Type Conversion)
类型转换分为隐式转换和显式转换。

### 1.3.1 隐式类型转换 (Implicit)
Python 会在算术运算中自动进行转换，以防止精度丢失。

整数 + 浮点数 = 浮点数

```
a = 10    # int
b = 2.5   # float
c = a + b 
print(c, type(c)) # 12.5 <class 'float'>
```

### 1.3.2 显式类型转换 (Explicit / Casting)
通过 Python 内置函数强制转换类型：

int(x): 将 x 转换为整数。如果是浮点数，会向零取整（丢弃小数部分）。

float(x): 将 x 转换为浮点数。

str(x): 将对象 x 转换为字符串形式。

bool(x): 将 x 转换为布尔值。

```
# 字符串转数值 (常用于处理输入)
x = int(1)   # x 输出结果为 1
y = int(2.8) # y 输出结果为 2
z = int("3") # z 输出结果为 3

# 浮点数/整数 (注意：不是四舍五入)
print(int(3.9))  # 输出: 3
print(int(-3.9)) # 输出: -3

x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2

# 转换为字符串 (常用于拼接输出)
x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'

# 逻辑转换
print(bool(1))    # True
print(bool(0))    # False
print(bool(""))   # False (空字符串为假)
print(bool([]))   # False (空列表为假)
```

## 1.4 算法常见避坑指南
注意：除法运算符 / 与 //

在 Python 3 中，单斜杠 / 的结果永远是 float（例如 4 / 2 结果是 2.0）。

在算法中求下标或需要整数结果时，务必使用双斜杠 //（整除）。
```
print(9 / 3)  # 3.0
print(9 // 3) # 3
```

---

# 2 注释
## 2.1 单行注释
```
# 这是一个注释
print("Hello, World!")
```

## 2.2 多行注释
多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来
```
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''
print("Hello, World!")

"""
这是多行注释（字符串），用三个双引号
这是多行注释（字符串），用三个双引号 
这是多行注释（字符串），用三个双引号
"""
print("Hello, World!")
```
在 Python 中，多行注释是由三个单引号 ''' 或三个双引号 """ 来定义的，而且这种注释方式并不能嵌套使用。当你开始一个多行注释块时，Python 会一直将后续的行都当作注释，直到遇到另一组三个单引号或三个双引号。
嵌套多行注释会导致语法错误。

```
'''
这是外部的多行注释
可以包含一些描述性的内容

    '''
    这是尝试嵌套的多行注释
    会导致语法错误
    '''
'''
```

---

# 3 运算符
## 3.1 算术运算符
![1769661687716](image/Python-Basis/1769661687716.png)

## 3.2 比较运算符
![1769661778315](image/Python-Basis/1769661778315.png)

## 3.3 赋值运算符
![1769661808387](image/Python-Basis/1769661808387.png)

## 3.4 位运算符
按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：

下表中变量 a 为 60，b 为 13二进制格式如下：
```
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011
```

![1769661893807](image/Python-Basis/1769661893807.png)

## 3.5 逻辑运算符
![1769661978985](image/Python-Basis/1769661978985.png)

---

# 4 字符串
## 4.1 访问字符串中的值
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

Python 访问子字符串，可以使用方括号 [] 来截取字符串。
![1769662199034](image/Python-Basis/1769662199034.png)

## 4.2 转义字符
![1769662294940](image/Python-Basis/1769662294940.png)
![1769662320045](image/Python-Basis/1769662320045.png)
![1769662333307](image/Python-Basis/1769662333307.png)

## 4.3 字符串运算符
![1769662365392](image/Python-Basis/1769662365392.png)


## 4.4 字符串格式化
![1769662433173](image/Python-Basis/1769662433173.png)
![1769662445153](image/Python-Basis/1769662445153.png)

## 4.5 三引号
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。实例如下
```

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)
```


## 4.6 f-string
f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去，实例如下：

```
>>> name = 'Runoob'
>>> f'Hello {name}'  # 替换变量
'Hello Runoob'
>>> f'{1+2}'         # 使用表达式
'3'

>>> w = {'name': 'Runoob', 'url': 'www.runoob.com'}
>>> f'{w["name"]}: {w["url"]}'
'Runoob: www.runoob.com'
```

---

# 5 列表
序列是 Python 中最基本的数据结构。

序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。

Python 有 6 个序列的内置类型，但最常见的是列表和元组。

列表都可以进行的操作包括索引，切片，加，乘，检查成员。

此外，Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
```
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
```

## 5.1 访问列表中的值
![1769662697733](image/Python-Basis/1769662697733.png)
![1769662715933](image/Python-Basis/1769662715933.png)
![1769662732327](image/Python-Basis/1769662732327.png)

## 5.2 列表操作
你可以对列表的数据项进行修改或更新，你也可以使用 append() 方法来添加列表项，如下所示：
```
list = ['Google', 'Runoob', 1997, 2000]

print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)

第三个元素为 :  1997
更新后的第三个元素为 :  2001
更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']

```

可以使用 del 语句来删除列表中的元素，如下实例：
```
list = ['Google', 'Runoob', 1997, 2000]
 
print ("原始列表 : ", list)
del list[2]
print ("删除第三个元素 : ", list)

原始列表 :  ['Google', 'Runoob', 1997, 2000]
删除第三个元素 :  ['Google', 'Runoob', 2000]

```

## 5.3 列表脚本操作符
![1769662910483](image/Python-Basis/1769662910483.png)

## 5.4 列表截取与拼接
![1769662937446](image/Python-Basis/1769662937446.png)

## 5.5 列表函数&方法
![1769662974540](image/Python-Basis/1769662974540.png)
![1769662992416](image/Python-Basis/1769662992416.png)

---

# 6 元组、字典、集合
## 6.1 元组
Python 的元组与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号 ( )，列表使用方括号 [ ]。

元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
![1769664421479](image/Python-Basis/1769664421479.png)

```
>>> tup1 = ('Google', 'Runoob', 1997, 2000)
>>> tup2 = (1, 2, 3, 4, 5 )
>>> tup3 = "a", "b", "c", "d"   #  不需要括号也可以
>>> type(tup3)
<class 'tuple'>
```
元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用。
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
```
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)
```

## 6.2 字典
![1769664606962](image/Python-Basis/1769664606962.png)
![1769664619901](image/Python-Basis/1769664619901.png)

### 6.2.1 创建空字典
```
# 使用大括号 {} 来创建空字典
emptyDict = {}
 
# 打印字典
print(emptyDict)
 
# 查看字典的数量
print("Length:", len(emptyDict))
 
# 查看类型
print(type(emptyDict))

# 使用内建函数 dict() 创建字典：
emptyDict = dict()
 
# 打印字典
print(emptyDict)
 
# 查看字典的数量
print("Length:",len(emptyDict))
 
# 查看类型
print(type(emptyDict))
```

### 6.2.2 访问字典里的值
```
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("tinydict['Name']: ", tinydict['Name'])
print ("tinydict['Age']: ", tinydict['Age'])

输出
tinydict['Name']:  Runoob
tinydict['Age']:  7

```

### 6.2.3 修改字典

```
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
tinydict['Age'] = 8               # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息
 
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])

输出
tinydict['Age']:  8
tinydict['School']:  菜鸟教程

```
### 6.2.4 删除字典元素
```
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del tinydict['Name'] # 删除键 'Name'
tinydict.clear()     # 清空字典
del tinydict         # 删除字典
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])

Traceback (most recent call last):
  File "/runoob-test/test.py", line 9, in <module>
    print ("tinydict['Age']: ", tinydict['Age'])
NameError: name 'tinydict' is not defined

```

### 6.2.5 字典键的特性
![1769664867421](image/Python-Basis/1769664867421.png)
![1769664878399](image/Python-Basis/1769664878399.png)

### 6.2.6 字典内置函数&方法
![1769664906932](image/Python-Basis/1769664906932.png)
![1769664924147](image/Python-Basis/1769664924147.png)
![1769664933461](image/Python-Basis/1769664933461.png)

## 6.3 集合
集合（set）是一个无序的不重复元素序列。

集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。
### 6.3.1 创建
![1769665025766](image/Python-Basis/1769665025766.png)
```
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # 这里演示的是去重功能
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # 快速判断元素是否在集合内
True
>>> 'crabgrass' in basket
False

>>> # 下面展示两个集合间的运算.
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # 集合a中包含而集合b中不包含的元素
{'r', 'd', 'b'}
>>> a | b                              # 集合a或b中包含的所有元素
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # 集合a和b中都包含了的元素
{'a', 'c'}
>>> a ^ b                              # 不同时包含于a和b的元素
{'r', 'd', 'b', 'm', 'z', 'l'}
```

### 6.3.2 集合的基本操作
![1769665125080](image/Python-Basis/1769665125080.png)
![1769665182579](image/Python-Basis/1769665182579.png)
![1769665195271](image/Python-Basis/1769665195271.png)
![1769665210698](image/Python-Basis/1769665210698.png)
![1769665238357](image/Python-Basis/1769665238357.png)

---

# 7 控制语句
## 7.1 条件控制
```
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3

```

## 7.2 循环语句
### 7.2.1 while 循环
```
while 判断条件(condition)：
    执行语句(statements)……

n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))

```
### 7.2.2 for 循环
```
for <variable> in <sequence>:
    <statements>
else:
    <statements>


word = 'runoob'
 
for letter in word:
    print(letter)
```

---

# 8 数据结构
## 8.1 内置容器型数据结构

### 列表 (List) —— 动态数组
* **特性**：支持随机访问，末尾添加/删除效率高。
* **常用操作**：`append()`, `pop()`, `sort()`, 切片 `[a:b]`。
* **算法用途**：实现栈（Stack）、存储邻接表、动态规划表格。

### 字典 (Dict) —— 哈希表
* **特性**：键值对存储，查找、插入、删除的平均复杂度均为 **O(1)**。
* **算法用途**：计数器、去重、缓存（Memoization）、建立映射关系。

### 集合 (Set) —— 哈希集合
* **特性**：无序且元素唯一，支持交集、并集、差集运算。
* **算法用途**：快速判定元素是否存在、数组去重。


## 8.2 collections 模块（标准库必备）

当内置容器无法满足性能需求时，`collections` 模块提供了更专业的数据结构。

### 双端队列 (`deque`)
* **导入**：`from collections import deque`
* **为什么用它**：在 `list` 的头部插入或删除元素复杂度是 $O(n)$，而 `deque` 在两端的 `append` 和 `pop` 都是 **O(1)**。
* **算法用途**：**广度优先搜索 (BFS)** 的核心队列、滑动窗口。

### 默认字典 (`defaultdict`)
* **导入**：`from collections import defaultdict`
* **为什么用它**：访问不存在的键时会自动初始化，避免繁琐的 `if key not in dict` 判断。
* **算法用途**：构建邻接表（例如 `defaultdict(list)`）。

### 计数器 (`Counter`)
* **导入**：`from collections import Counter`
* **算法用途**：快速统计词频，支持集合间的数学运算。

## 8.3 优先级队列与排序

### 堆 (`heapq`)
* **导入**：`import heapq`
* **特性**：Python 默认实现的是**小顶堆**（Min-heap）。
* **常用操作**：`heappush()`, `heappop()`, `heapify()`。
* **算法用途**：Dijkstra 最短路径算法、Top K 问题、合并 K 个有序链表。

### 二分查找 (`bisect`)
* **导入**：`import bisect`
* **特性**：在有序序列中快速查找插入点。
* **算法用途**：查找最左/最右插入位置，优化某些 $O(n^2)$ 算法至 $O(n \log n)$。


---

# 9 迭代器与生成器
## 9.1 迭代器

迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

### 9.1.1 创建一个迭代器
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。

如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。

更多内容查阅：Python3 面向对象

__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。

__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。

创建一个返回数字的迭代器，初始值为 1，逐步递增 1：

```
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

输出
1
2
3
4
5
```

### 9.1.2 StopIteration
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

在 20 次迭代后停止执行：

```
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)

```

## 9.2 生成器

在 Python 中，使用了 yield 的函数被称为生成器（generator）。

yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。

然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。

调用一个生成器函数，返回的是一个迭代器对象。

下面是一个简单的示例，展示了生成器函数的使用：

```
def countdown(n):
    while n > 0:
        yield n
        n -= 1
 
# 创建生成器对象
generator = countdown(5)
 
# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
 
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1
```
以上实例中，countdown 函数是一个生成器函数。它使用 yield 语句逐步产生从 n 到 1 的倒数数字。在每次调用 yield 语句时，函数会返回当前的倒数值，并在下一次调用时从上次暂停的地方继续执行。

通过创建生成器对象并使用 next() 函数或 for 循环迭代生成器，我们可以逐步获取生成器函数产生的值。在这个例子中，我们首先使用 next() 函数获取前三个倒数值，然后通过 for 循环获取剩下的两个倒数值。

生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。此外，生成器还可以与其他迭代工具（如for循环）无缝配合使用，提供简洁和高效的迭代方式。