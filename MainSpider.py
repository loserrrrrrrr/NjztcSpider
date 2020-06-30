from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
#因为是动态网页，网站中想爬取的数据是通过js传输的，网站的源码也不是静态的，所以requests行不通
#所以选择selenium库，达到模拟键鼠的效果

driver = webdriver.Chrome()     #这里选择的是Chrome浏览器驱动chromedriver
driver.implicitly_wait(5)       #等待5秒页面加载完成
url = 'http://njzy.njztc.com/find_taskWorkList.jspx'
driver.get(url)

move_body = driver.find_element_by_tag_name('body')

for i in range(1,6):
    # 因为网站是动态读取信息需要页面下拉到一定页数才会显示全部信息。
    # 所以使用selenium的函数模拟按下PageDown键若干次
    move_body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

for li in driver.find_elements_by_class_name('znh_list'):
    inform_list = re.split('/|：|\n', li.text)   #多个分隔符

    '''
    分割效果例如
    ['作业内容', '喷药水稻', '作业规模', '1000 亩', '作业单价', '6 元', '拟引入农机量', '0 (台', '套)',
    '作业时间', '2020-07-22', ' 2020-07-25', '发布单位', '', '联系方式', '', '作业地点', ' 江苏省徐州市泉山区富国街',
    '备注信息', '专业植保团队，多年经验', '查看位置']
    '''

    print(inform_list)

driver.quit()
