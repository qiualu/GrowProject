import time
# -------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
# -------------------------------------------
from lxml import etree
print('示例1')
# -------  示例1  ---------------------------------------------
# driver = webdriver.Chrome()  # 打开浏览器
# # driver = webdriver.Firefox()
# # driver = webdriver.PhantomJS('D:\program\Python\phantomjs.exe') # 无界面浏览器
#
# driver.get("https://www.baidu.com/")  # 打开网址
# time.sleep(5)
# print( driver.title )  # 打印标题
# kw = driver.find_element_by_id('kw')  # 获得id 对象
# kw.send_keys("十九大")  # 输入 id 对象
# -------------------------------------------------------------
print('元素的定位')
# # --  元素的定位  ------------------------------------------------
# from selenium import webdriver
#
# obj = webdriver.PhantomJS(executable_path="D:\program\Python\phantomjs.exe")
# obj.set_page_load_timeout(5)  # 设置超时
# 对象的定位是通过属性定位来实现的，这种属性就像人的身份证信息一样，或是其他的一些信息来找到这个对象，
# 那我们下面就介绍下Webdriver提供的几个常用的定位方法
# 上面这个是百度的输入框，我们可以发现我们可以用id来定位这个标签，然后就可以进行后面的操作了
# try:   #<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
#     obj.get('http://www.baidu.com')
#     # obj.find_element_by_id('kw')  # 通过ID定位
#     # obj.find_element_by_class_name('s_ipt')  # 通过class属性定位
#     # obj.find_element_by_name('wd')  # 通过标签name属性定位
#     # obj.find_element_by_tag_name('input')  # 通过标签属性定位
#     # obj.find_element_by_css_selector('#kw')  # 通过css方式定位
#     # obj.find_element_by_xpath("//input[@id='kw']")  # 通过xpath方式定位
#     # obj.find_element_by_link_text("贴吧")  # 通过xpath方式定位
#
#     print(obj.find_element_by_id('kw').tag_name) # 获取标签的类型
# except Exception as e:
#     print(e)
# # ----------------------------------------------------------------
print('浏览器的操作')
# --  浏览器的操作  -------------------------------------------------
# from selenium import webdriver
# obj = webdriver.PhantomJS(executable_path="D:\program\Python\phantomjs.exe")
# obj.set_page_load_timeout(5)  # 超时
# obj.maximize_window()  #设置全屏   # 调用启动的浏览器不是全屏的，有时候会影响我们的某些操作，所以我们可以设置全屏   <---------
# # obj.set_window_size('480','800') #设置浏览器宽480，高800   <---------
# try:
#     obj.get('http://www.baidu.com')
#     obj.save_screenshot('11.png')  # 截取全屏，并保存
# except Exception as e:
#     print(e)
# 操作浏览器前进、后退
# obj.back()#回退到百度首页            <---------
# obj.forward()#前进到新浪首页         <---------
# from selenium import webdriver           # 示例
# obj = webdriver.PhantomJS(executable_path="D:\program\Python\phantomjs.exe")
# try:
#     obj.get('http://www.baidu.com')   #访问百度首页
#     obj.save_screenshot('1.png')
#     obj.get('http://www.sina.com.cn') #访问新浪首页
#     obj.save_screenshot('2.png')
#     obj.back()                           #回退到百度首页
#     obj.save_screenshot('3.png')
#     obj.forward()                        #前进到新浪首页
#     obj.save_screenshot('4.png')
# except Exception as e:
#     print(e)
#--------------------------------------------------------------------
print('操作测试对象')
# --  操作测试对象  -------------------------------------------------
# 定位到元素以后，我们就应该对相应的对象进行某些操作，以达到我们某些特定的目的，那我们下面就介绍下Webdriver提供的几个常用的操作方法
# print(obj.find_element_by_id("cp").text)  # 获取元素的文本信息
# obj.find_element_by_id('kw').clear()              #用于清除输入框的内容
# obj.find_element_by_id('kw').send_keys('Hello')  #在输入框内输入Hello
# obj.find_element_by_id('su').click()              #用于点击按钮
# obj.find_element_by_id('su').submit()             #用于提交表单内容

# from selenium import webdriver   # 示例
#
# obj = webdriver.PhantomJS(executable_path="D:\program\Python\phantomjs.exe")
# obj.set_page_load_timeout(5)
# try:
#     obj.get('http://www.baidu.com')
#     print(obj.find_element_by_id("cp").text)  # 获取元素的文本信息
#     obj.find_element_by_id('kw').clear()              #用于清除输入框的内容
#     obj.find_element_by_id('kw').send_keys('Hello')  #在输入框内输入Hello
#     obj.find_element_by_id('su').click()              #用于点击按钮
#     obj.find_element_by_id('su').submit()             #用于提交表单内容
#
# except Exception as e:
#     print(e)
#--------------------------------------------------------------------
print('键盘事件')
# --  键盘事件  -------------------------------------------------
# 键盘按键用法  +++++++++++++
# obj.find_element_by_id('kw').send_keys(Keys.TAB)   #用于清除输入框的内容,相当于clear()
# obj.find_element_by_id('kw').send_keys('Hello')   #在输入框内输入Hello
# obj.find_element_by_id('su').send_keys(Keys.ENTER) #通过定位按钮，通过enter（回车）代替click()

# from selenium.webdriver.common.keys import Keys
# obj = webdriver.PhantomJS(executable_path="D:\Python27\Scripts\phantomjs.exe")
# obj.set_page_load_timeout(5)
# try:
#     obj.get('http://www.baidu.com')
#     obj.find_element_by_id('kw').send_keys(Keys.TAB)  # 用于清除输入框的内容,相当于clear()
#     obj.find_element_by_id('kw').send_keys('Hello')  # 在输入框内输入Hello
#     obj.find_element_by_id('su').send_keys(Keys.ENTER)  # 通过定位按钮，通过enter（回车）代替click()
#
# except Exception as e:
#     print(e)

# 键盘组合键使用  +++++++++++++
# obj.find_element_by_id('kw').send_keys(Keys.TAB)   #用于清除输入框的内容,相当于clear()
# obj.find_element_by_id('kw').send_keys('Hello')   #在输入框内输入Hello
# obj.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')   #ctrl + a 全选输入框内容
# obj.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')   #ctrl + x 剪切输入框内容

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# obj = webdriver.PhantomJS(executable_path="D:\Python27\Scripts\phantomjs.exe")
# obj.set_page_load_timeout(5)
# try:
#     obj.get('http://www.baidu.com')
#     obj.find_element_by_id('kw').send_keys(Keys.TAB)  # 用于清除输入框的内容,相当于clear()
#     obj.find_element_by_id('kw').send_keys('Hello')  # 在输入框内输入Hello
#     obj.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')  # ctrl + a 全选输入框内容
#     obj.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')  # ctrl + x 剪切输入框内容
#
# except Exception as e:
#     print(e)

# ------------------------------------------------------------------------------------
print('中文乱码问题')
# 中文乱码问题
# selenium2 在python的send_keys（）中输入中文会报错，其实在中文前面加一个u变成unicode就能搞定了
print('鼠标事件')
# # --  鼠标事件  ------------------------------------------------ActionChains 鼠标操作
from selenium import webdriver
#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
# click(self, on_element=None): 点击  参数: -onelement:要单击的元素。 如果没有，点击当前鼠标位置。
# click_and_hold(self, on_element=None):  左击
# context_click() 右击
# double_click() 双击
# drag_and_drop() 拖动
# move_to_element() 鼠标悬停
#使用方法
brower = webdriver.Firefox()
brower.get("http://www.baidu.com")
#定位到需要右击的元素并赋值给rigth_click
right_click = brower.find_element_by_id("xx")
#对定位到的元素进行右击操作。
ActionChains(brower).context_click(right_click).perform()  # perform()执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作。
# # ----------------------------------------------------------------

# 区域截图 ---------------------------------------------------------
# a = driver.find_element_by_tag_name('table')
# a.screenshot('a.jpg')


