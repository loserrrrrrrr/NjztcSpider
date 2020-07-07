
import pyqtgraph as pg
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from scipy import stats


class Ui_Graph(QTabWidget):


    def __init__(self,elementList, parent=None):
        self.area_list = [elementList[i].area for i in range(len(elementList))]
        self.price_list = [elementList[i].price for i in range(len(elementList))]

        super(Ui_Graph, self).__init__(parent)
        self.resize(720, 520)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")


        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.setWindowTitle("图表")

    def tab1UI(self):

        pg.setConfigOptions(leftButtonPan=False)
        pg.setConfigOption('background', 'k')
        pg.setConfigOption('foreground', 'w')

        self.pw = pg.PlotWidget(self)

        print(self.area_list)
        print(self.price_list)

        self.pw.plot(self.area_list, self.price_list, pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))

        self.pw.setLabel('left', "价格", units='，亩/元')
        self.pw.setLabel('bottom', "作业面积", units='亩')

        #self.pw.setLogMode(x=False, y=True)

        #为这个tab命名显示出来，第一个参数是哪个标签，第二个参数是标签的名字
        self.setTabText(0, "二维散点图")

        # 帧布局
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pw)
        # 在标签1中添加这个帧布局
        self.tab1.setLayout(self.layout)
    # 同理如上
    def tab2UI(self):
        pg.setConfigOptions(leftButtonPan=False)
        pg.setConfigOption('background', 'k')
        pg.setConfigOption('foreground', 'w')

        self.pw = pg.PlotWidget(self)

        self.pw.plot(self.area_list, pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')

        self.setTabText(1, "历年农作面积分布")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pw)
        self.tab2.setLayout(self.layout)

    def tab3UI(self):
        pg.setConfigOptions(leftButtonPan=False)
        pg.setConfigOption('background', 'k')
        pg.setConfigOption('foreground', 'w')

        self.pw = pg.PlotWidget(self)

        self.pw.plot(self.price_list, pen=(200, 200, 200), symbolBrush=(255, 0, 0), symbolPen='w')

        self.setTabText(2, "历年价格分布")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pw)
        self.tab3.setLayout(self.layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Ui_Graph()
    demo.show()
    sys.exit(app.exec_())