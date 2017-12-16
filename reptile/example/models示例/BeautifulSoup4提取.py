from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 创建 beautifulsoup 对象
soup = BeautifulSoup(html,'lxml')

# 打印内容  获取内容
# print(soup.prettify())

# Tag --------------------------------------------------------
# 对于 Tag，它有两个重要的属性，是 name 和 attrs，下面我们分别来感受一下
print(soup.name)  # [document]  soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。
print(soup.head.name)  # head #标签名
print(soup.p.attrs)  # 属性内容 {'class': ['title'], 'name': 'dromouse'}
# 在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
# 如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么
print(soup.p.attrs['class']) # ['title'] soup.p.get('class')  # 还可以这样，利用get方法，传入属性的名称，二者是等价的
# 我们可以对这些属性和内容等等进行修改，例如
soup.p['class'] = 'newClass'
print(soup.p)

# NavigableString   -------------------------------------------
# 既然我们已经得到了标签的内容，那么问题来了，我们要想获取标签内部的文字怎么办呢？很简单，用 .string 即可，例如
print(soup.p.string) # p元素内容
print(soup.p) # 完整的p 元素
# 这样我们就轻松获取到了标签里面的内容，想想如果用正则表达式要多麻烦。它的类型是一个 NavigableString，翻译过来叫 可以遍历的字符串，不过我们最好还是称它英文名字吧。
print(type(soup.p.string)) # <class 'bs4.element.NavigableString'>

# BeautifulSoup  ----------------------------------------
# BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性来感受一下
print(type(soup)) # <class 'str'>
print(soup.name)  # [document]
print(soup.attrs)  # {} 空字典

# Comment  ----------------------------------------------
# Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。
print()














