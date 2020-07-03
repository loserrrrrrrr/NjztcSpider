import re
import InformClass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# http://njzy.njztc.com/find_taskWorkList.jspx

# 因为是动态网页，网站中想爬取的数据是通过js传输的，网站的源码也不是静态的，所以requests行不通
# 所以选择selenium库，达到模拟键鼠的效果

def web_spider(url):
    chrome_options: Options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 让chrome用无界面形式打开
    data = []
    try:
        driver = webdriver.Chrome(chrome_options=chrome_options)  # 这里选择的是Chrome浏览器驱动chromedriver
        driver.implicitly_wait(5)  # 设置等待5秒页面加载完成
        print("正在连接"+url)
        driver.get(url)

        for li in driver.find_elements_by_class_name('znh_list'):  # 找到“class='znh_list'”的标签，获取文本信息
            # 对网站源码分析发现联系人信息在标签中，例如<span class="lianxi" name="杨雪峰\xa018352282619">
            contact_str = li.find_element_by_class_name('lianxi').get_attribute('name')
            # 用get_attribute()函数获取class="lianxi"的标签下name的属性值
            contact_li = contact_str.split('\xa0')  # 将信息拆分成姓名和联系方式
            str_li = li.text.replace('作业内容：', '').replace('作业规模：', '').replace('作业单价：', '') \
                .replace('拟引入农机量：', '').replace('作业时间：', '').replace('发布单位：', '') \
                .replace('联系方式：', '').replace('作业地点：', '').replace('备注信息：', '') \
                .replace('查看位置', '')  # 删去不必要内容
            inform_list = re.split('/|\n', str_li)  # 多个分隔符
            del inform_list[3:5]  # 删去不必要内容
            del inform_list[5:7]
            del inform_list[6:8]
            inform_list.insert(5, contact_li[0])  # 插入联系人信息
            inform_list.insert(6, contact_li[1])
            inform_list[4] = inform_list[4].replace(' ', '')  # 去掉空格（土方法）
            '''
            分割效果例如
            ['机收水稻', '5000 亩', '150 元', '2020-08-01', ' 2020-09-10', 
            '合江县农业局', '13980251146', ' 四川省, 泸州市, 合江县']
            '''
            inf = InformClass.SupplyInform(inform_list)
            data.append(inf)

    except BaseException as args:
        print("出现异常"+args)

    finally:
        driver.quit()

    return data