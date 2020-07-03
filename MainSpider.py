import njzySpider
import duduSpider
import InformClass

njzy_url = 'http://njzy.njztc.com/find_taskWorkList.jspx'
dudu_url = 'http://dudu.nongjibang.com/?p=1'

n_list = njzySpider.web_spider(njzy_url)    #返回的是SupplyInform类的列表
d_list = duduSpider.web_spider(dudu_url)

supply_list = n_list + d_list

print(supply_list)