from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#因为是动态网页，网站中想爬取的数据是通过js传输的，网站的源码也不是静态的，所以requests行不通
#所以选择selenium库，达到模拟键鼠的效果

driver = webdriver.Chrome()     #这里选择的是Chrome浏览器驱动chromedriver
driver.implicitly_wait(5)       #等待5秒页面加载完成
url = 'http://www.njztc.com/emc_TaskWorkSd_list.jspx?count=15&mark=1'
driver.get(url)

move_body = driver.find_element_by_tag_name('body')
result=[]

for i in range(1,6):
    # 因为网站是动态读取信息需要页面下拉到一定页数才会显示全部信息。
    # 所以使用selenium的函数模拟按下PageDown键若干次
    move_body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

for list in driver.find_elements_by_class_name('znh_list'):
    print('--------------------------------------------')
    print(list.text)
driver.quit()
