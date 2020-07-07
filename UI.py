from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import duduSpider
import njzySpider
import time
from ui.SpiderUI import Ui_NjztcSpider
from pyGraph import Ui_Graph


class mywindow(QWidget, Ui_NjztcSpider):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.model = QStandardItemModel(0, 8)
        self.model.setHorizontalHeaderLabels(
            ['作业内容', '作业面积（亩）', '价格（元/亩）', '起始时间', '结束时间', '发布人', '联系方式', '地址'])  # 设置每列标题

        self.SupplyInform.setModel(self.model)

        # 新建图表子窗口，并传输数据
        self.dia = Ui_Graph(supply_list)
        #self.dia.setupUi()

        self.spiderButton.clicked.connect(lambda: self.spiderOn())
        self.graphButton.clicked.connect(lambda:self.dia.show())


    def spiderOn(self):
        self.spiderButton.setDisabled(True)
        self.SpiderInform.setText("正在载入数据")
        print("正在导入数据")
        for li in supply_list:
            QApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
            if li.if_valid():
                self.model.appendRow(
                    [QStandardItem(str(li.type)), QStandardItem(str(li.area)), QStandardItem(str(li.price)),
                     QStandardItem(str(li.date_from)), QStandardItem(str(li.date_to)), QStandardItem(str(li.name)),
                     QStandardItem(str(li.tele_num)), QStandardItem(str(li.place))])
            else:
                continue

def abnormalValue(data=[]):
    area = [data[i].area for i in range(len(data))]
    price = [data[i].price for i in range(len(data))]

    area_u = np.mean(area)
    price_u = np.mean(price)

    area_std = np.std(area)
    price_std = np.std(price)

    for e in data:
        if e.area<1e-4 or e.price<1e-4 or e.price>1e5 or np.abs(e.area - area_u) > 3*area_std or np.abs(e.price - price_u) > 3*price_std:
            data.remove(e)

    return data

if __name__ == "__main__":
    import sys

    njzy_url = 'http://njzy.njztc.com/find_taskWorkList.jspx'
    dudu_url = 'http://dudu.nongjibang.com'
    print('开始爬取' + njzy_url)
    # self.SpiderInform.setText("正在爬取" + njzy_url + "，请稍后")
    n_list = njzySpider.web_spider(njzy_url)  # 返回的是SupplyInform类的列表
    print(njzy_url + "爬取完毕")
    print('开始爬取' + dudu_url)
    # self.SpiderInform.setText("正在爬取" + dudu_url + "，请稍后")
    d_list = duduSpider.web_spider(dudu_url)
    print(dudu_url + "爬取完毕")
    supply_list = abnormalValue(n_list + d_list)

    app = QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
