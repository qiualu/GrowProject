#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


# IE浏览器，IE浏览器和chrome比较相似，也需要我们自己去找到Driver，名字是IEDriverServer.exe，这个随便一百度也能找到，就不放连接了，下载后跟chrome那里一样，也是放到ieexplore.exe的同级目录下

def main():
    chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver)
    url = "http://www.baidu.com"
    browser.get(url)
    print(browser.title)

    time.sleep(5)
    browser.quit()  #关闭

'''
driver = webdriver.Chrome()  # 打开浏览器
# driver = webdriver.Firefox()
# driver = webdriver.PhantomJS('D:\program\Python\phantomjs.exe') # 无界面浏览器

driver.get("https://www.baidu.com/")  # 打开网址
time.sleep(5)
print( driver.title )  # 打印标题
kw = driver.find_element_by_id('kw')  # 获得id 对象
kw.send_keys("十九大")  # 输入 id 对象
'''

if __name__ == '__main__':
    main()