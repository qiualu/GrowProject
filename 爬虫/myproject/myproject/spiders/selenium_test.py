# coding=utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from lxml import etree


driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.PhantomJS('D:/ProgramFiles/phantomjs-2.1.1-windows/bin/phantomjs.exe')


########################################################
########################################################

'''
driver.get("https://www.baidu.com/")
time.sleep(5)
print( driver.title )
kw = driver.find_element_by_id('kw')
kw.send_keys("十九大")

# 方案 
# 回车开始搜索
# kw.send_keys(Keys.ENTER)

# 方案 2
# 将鼠标移动到按钮上，再点击
# 注意：driver.find_element_by_id('su').click() 会报错
# 因为鼠标移动到按钮的时候，页面代码会发生变化
ele = driver.find_element_by_id('su')
ActionChains(driver).click(ele).perform()
time.sleep(8)

print( driver.save_screenshot('jietu.png') )
'''

########################################################
########################################################
'''
driver.get("http://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=")
time.sleep(2)
driver.find_element_by_id('loginName').send_keys("xxxxxxxxxxxxx")
driver.find_element_by_id('loginPassword').send_keys("yyyyyyyyyyy")
driver.find_element_by_id('loginAction').click()
time.sleep(1)
driver.find_element_by_id('loginAction').click()
time.sleep(5)
# print( driver.save_screenshot('jietu.png') )
'''

########################################################
########################################################
'''
driver.get("https://weibo.com")
time.sleep(15)
driver.find_element_by_id('loginname').send_keys("xxxxxxxxxxxxxxxx")
driver.find_element_by_name('password').send_keys("yyyyyyyyyyyyy")
print( driver.save_screenshot('jietu1.png') )

#with open('weibo.htm','w') as f:
#	f.write(driver.page_source)
#	f.close()

# 下面会报错:selenium.common.exceptions.WebDriverException: Message: u'Compound class names not permitted，因为名字有空格
# driver.find_element_by_class_name('W_btn_a btn_32px').click()
# driver.find_element_by_class_name('btn_32px').click()
# driver.find_element_by_class_name('btn_32px').click()
driver.find_element_by_link_text(u'登录').click()
# driver.find_element_by_xpath(".//*[@class='0 ou 6']").click()

# driver.find_element_by_css_selector('.W_btn_a.btn_32px').click()
# time.sleep(1)
# driver.find_element_by_css_selector('.W_btn_a.btn_32px').click()

# ele = driver.find_element_by_css_selector('.W_btn_a.btn_32px')
# ActionChains(driver).click(ele).perform()
# ele = driver.find_element_by_css_selector('.info_list.login_btn')
# ActionChains(driver).click(ele).perform()
# ele.click()

time.sleep(6)
print( driver.save_screenshot('jietu2.png') )
'''


########################################################
########################################################
'''
driver.get("https://www.zhihu.com/#signin")
time.sleep(4)
# print( driver.save_screenshot('zhihu_page.png') )

# 进入用户密码输入页面
driver.find_element_by_class_name('signin-switch-password').click()
time.sleep(1)

# 输入用户
driver.find_element_by_xpath("//input[@name='account']").send_keys('worio.hainan@163.com')
# 输入密码 
driver.find_element_by_xpath("//input[@name='password']").send_keys('zgl20053779')
# 找到提交按钮
submit_button = driver.find_element_by_xpath("//button[@class='sign-button submit']")
# 点击提交，弹出验证码
submit_button.click()
# 给时间输入验证码
time.sleep(6)
# 再次点击提交
submit_button.click()
# 给时间页面加载数据
time.sleep(4)

# cookie= driver.get_cookies()
# print(cookie)
# print(driver.page_source)

# 将页面滚动到最后，执行多次
#for i in range(5):
#	js="var q=document.documentElement.scrollTop=10000"
#	driver.execute_script(js)
#	time.sleep(7)

# link_list = driver.find_element_by_xpath("//h2[@class='ContentItem-title']/a")
link_list = driver.find_elements_by_tag_name("a")
print(link_list)

# 获取当前窗口句柄
now_handle = driver.current_window_handle

# 获取所有窗口句柄
# all_handles = driver.window_handles

file_name = 'D:/files/'
index = 1

for link in link_list:
	print('==================================')
	if 'Title' == link.get_attribute('data-za-detail-view-element_name') :
		# print(link)
		link.click()
		time.sleep(6)

		# all_handles = driver.window_handles
		driver.switch_to_window(driver.window_handles[1])
		print(driver.current_window_handle)
		# print(driver.page_source.encode('GB18030'))

		f = open(file_name+str(index),'wb')
		f.write(driver.page_source.encode('GB18030'))
		f.close()
		index += 1

		if index == 10 :
			break

		time.sleep(2)
		# 返回主窗口
		driver.close()
		driver.switch_to_window(now_handle)
		time.sleep(1)
		driver.execute_script("arguments[0].scrollIntoView();", link)
		time.sleep(1)
'''

##############################################################
##############################################################

# 唯品会女装图片链接无法直接获得
driver.get("https://category.vip.com/search-3-0-1.html?q=3|30036||&rp=30074|30063&ff=women|0|2|2&adidx=1&f=ad&adp=65001&adid=326630")
time.sleep(5)

# print( driver.save_screenshot('jietu.png') )

num = 500
for i in range(1, 22):
	# 谷歌 和 火狐
	# js = "var q=document.documentElement.scrollTop=" + str(num * i)

	# PhantomJS
	js = "var q=document.body.scrollTop=" + str(num * i)
	driver.execute_script(js)
	print('=====================================')
	time.sleep(3)
	# break

# print( driver.save_screenshot('jietu.png') )

html = etree.HTML(driver.page_source)

src_list = html.xpath("//img[contains(@id,'J_pic')]/@src")
for src in src_list:
	print(src)

all_img_list = []
# 模糊匹配
# img_group_list = html.xpath("//img[contains(@id,'J_pic')]")
# img_group_list = html.xpath("//img[starts-with(@id,'J_pic')]")
# 正则表达式
img_group_list = html.xpath(r'//img[re:match(@id, "J_pic*")]', namespaces={"re": "http://exslt.org/regular-expressions"})
for img_group in img_group_list:
	img_of_group = img_group.xpath(".//@data-original | .//@data-img-back | .//@data-img-side")
	print(img_of_group)
	all_img_list.append( '\n'.join(img_of_group)+'\n' )


f = open('vip.txt','w', encoding='utf-8')
f.write('\n'.join(all_img_list))
f.close()


###
driver.quit()

