from selenium import webdriver
from lxml import etree


driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com')
data = driver.page_source
print(type(driver))

# html = etree.HTML(driver)
# title = html.xpath('/html/head/title/text()')
# print(title)