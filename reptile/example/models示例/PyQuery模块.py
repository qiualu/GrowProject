from pyquery import PyQuery as pq

def main():

    # 初始化方式
    # d=pq("<html><title>hello</title></html>")
    # d=pq(filename=path_to_html_file)
    # d=pq(url='http://www.baidu.com')  #注意：此处url似乎必须写全

    # doc = pq('http://www.youdao.com')

    # print(doc('title')) # 获取 title 标签的源码
    # print(doc('title').text()) # 获取 title 标签的内容
    # print(doc('#margin3')) # 获取 id 为 margin3 的标签的内容

    # li = doc('li')        # 处理多个元素
    # for i in li:
    #     print(pq(i).text())

    # a_title = doc('#margin3')  #循环内部标签内容
    # a = pq(a_title)
    # a_href = a('a')
    # for a_href in a_href:
    #     print(pq(a_href).text())


    #2. html()和text() ——获取相应的HTML块或文本块# ***********************************************
    # print(doc('head').html())    # 返回<head>.之间.</head>
    # print(doc('head'))        #返回原码
    # print(doc('head').text())    #返回内容


    #3.  根据HTML标签来获取元素
    # d=pq('<div><p>test 1</p><p>test 2</p></div>')
    # d('p')  #返回[<p>,<p>]
    # print(d('p'))   #返回<p>test 1</p><p>test 2</p>
    # print(d('p').html())    #返回test 1

    #4..eq(index) ——根据给定的索引号得到指定元素        # *************************  eq(index)
    # print(d('p').eq(1).html()) #返回test 2

    #5. .filter() ——根据类名、id名得到指定元素，例：        # *************filter()
    # d=pq("<div><p id='a'>id为a 1</p><p class='b'>class为b 2</p></div>")
    # print(d('p').filter('#a'))  #返回[<p#1>]
    # print(d('p').filter('.b'))  #返回[<p.2>]

    #6. .find() ——查找嵌套元素，例： #  *************find()
    # d=pq("<div><p id='1'>test 1</p><p class='2'>test 2</p></div>")
    # print(d('div').find('p'))  #返回[<p#1>, <p.2>]
    # print(d('div').find('p').eq(0))  #返回[<p#1>]

    #7.直接根据类名、id名获取元素，例：
    # d=pq("<div><p id='a'>test 1</p><p class='a'>test 2</p></div>")
    # print(d('#a').html()) #返回test 1
    # print(d('.a').html()) #返回test 2

    # 8.获取属性值，例：                       #******************** attr('href')
    # d=pq("<p id='my_id'><a href='http://hello.com'>hello</a></p>")
    # print(d('a').attr('href'))  #返回http://hello.com
    # print(d('p').attr('id'))    #返回my_id
    # 9.修改属性值，例：         # **** *** ** * **
    # d('a').attr('href', 'http://baidu.com') #把href属性修改为了baidu
    # print(d)

    # 10.addClass(value) ——为元素添加类，例：
    # d=pq('<div></div>')
    # print(d.addClass('my_class'))  #返回[<div.my_class>]

    # 11.hasClass(name) #返回判断元素是否包含给定的类，例：
    # d=pq("<div class='my_class'></div>")
    # print(d.hasClass('my_class'))   #返回True

    # 12.children(selector=None) ——获取子元素，例：   # ****  children(selector=None)
    # d=pq("<span><p id='1'>hello</p><p id='2'>world</p></span>")
    # print(d.children())  #  返回[<p#1>, <p#2>]
    # print(d.children('#2'))  #返回[<p#2>]

    # 13.parents(selector=None)——获取父元素，例：       # ********  parents(selector=None)
    # d=pq("<span><p id='a'>hello</p><p id='b'>world</p></span>")
    # print(d('p').parents()) #返回[<span>]
    # print(d('#a').parents('span'))  #返回[<span>]
    # print(d('#a').parents('p')) #返回[]

    # 14.clone() ——返回一个节点的拷贝
    # d=pq("<span><p id='a'>hello</p><p id='b'>world</p></span>")
    # print(d('p').clone()) #返回[<span>]

    # 15.empty() ——移除节点内容
    # d=pq("<span><p id='a'>hello</p><p id='b'>world</p></span>")
    # print(d('p').empty()) #返回[<span>]

    # 16.nextAll(selector=None) ——返回后面全部的元素块，例：
    # d=pq("<p id='1'>hello</p><p id='2'>world</p><img scr='scr的内容' />")
    # print(d('p:first').nextAll())   #返回[<p#2>, <img>]
    # print(d('p:last').nextAll())    #返回[<img>]

    # 17.not_(selector) ——返回不匹配选择器的元素，例：
    d=pq("<p id='1'>test 1</p><p id='2'>test 2</p>")
    print(d('p').not_('#2'))   #返回[<p#1>]



if __name__ == '__main__':
    main()
