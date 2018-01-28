from lxml import etree

# html 文件或文本
page_text = '''
<html>
<title> This is Title </title>
<body>
	<h1> This is h1 </h1>
	<div> This is fisrt div </div>
	<div id="divid">
		<img src="1111.png"/>
		<span id="sp1"> desc 1111.png </span>
		<img src="2222.png"/>
		<span id="sp2"> desc 2222.png </span>
		<p>
			<a href="http://www.xxxxx.com/"> link-of-xxxxxx </a>
		</p>
		<a href="http://www.yyyyyyy.com/"> link-of-yyyyyyyyy </a>
		<br/>
		<a href="http://www.zzzzzzz.com/"> link-of-zzzzzzzzz </a>
	</div>
	<p class="p_classname"> This is p with class name </p>
	<div class="div_classname"> This is div with class name </div>
</body>
</html>
'''

# 创建html 对象
html = etree.fromstring(page_text)   # class 'lxml.etree._Element'

print(type(html))

def printEleListTxt(elelist):
	for e in elelist :
		print('text = ' + e.text)

#  *****************  xpath   ************************

# # 所有 div 元素集合列表 ------------------------------
div_list = html.xpath('//div')  # 列表 对象
print(div_list)
print(div_list[0].text)  # 对象内容

# # 所有拥有id属性的 div 元素集合列表 -------------------
# div_list = html.xpath('//div[@id]')
# print(div_list)
# printEleListTxt(div_list)

# 所有 class 属性为 div_classname 的 div 元素集合列表----
# div_list = html.xpath('//div[@class="div_classname"]')
# print(div_list)
# printEleListTxt(div_list)

# 所有属性 非空 的 div 元素集合列表-----------------------
# div_list = html.xpath('//div[@*]')
# print(div_list)
# printEleListTxt(div_list)

# 所有属性为 空 的 div 元素集合列表------------------------
# div_list = html.xpath('//div[not(@*)]')
# print(div_list)
# printEleListTxt(div_list)

# 第一个 div 元素列表，注意下标不是 0，而且类型依然是 列表----
# div_list = html.xpath('//div[1]')
# print(div_list)
# printEleListTxt(div_list)

# 最后一个 div 元素，类型列表--------------------------------
# div_list = html.xpath('//div[last()]')
# print(div_list)
# printEleListTxt(div_list)

# 倒数第2个 div 元素，类型列表--------------------------------
# div_list = html.xpath('//div[last()-1]')
# print(div_list)
# printEleListTxt(div_list)
# print(type(div_list))
# 位置为最前面 2 个的div元素-----------------------------------
# div_list = html.xpath('//div[position() < 3]')
# print(div_list)
# printEleListTxt(div_list)
# print(type(div_list))

# 所有 标签a 的 href属性值，列表------------------------------------
# div_list = html.xpath('//a/@href')
# print(div_list)


# 第 2 个 div 标签下一层所有 a 的 href 属性值------------------------
# 注意 p 中的 a 没拿到
# div_list = html.xpath('//div[2]/a/@href')
# print(div_list)



# 第 2 个 div 标签以下以下所有层面 a 的 href 属性值
# div_list = html.xpath('//div[2]//a/@href')
# print(div_list)

# 第 2 个 div 标签下第1个 span 的 id 属性值
# div_list = html.xpath('//div[2]/span[1]/@id')
# print(div_list)

# 查找 div 和 p 的集合
div_list = html.xpath('//div | //p')
print(div_list)
















