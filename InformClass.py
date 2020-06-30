import datetime
import jieba


def str2date(dt):       #将xxxx-xx-xx的日期字符串转化成date类型
    date = datetime.datetime.strptime(dt, "%Y-%m-%d")
    date = datetime.date(date.year, date.month, date.day)
    return date

class SupplyInform:

    informCount = 0

    type = ''       #作业内容
    area = ''       #作业面积：xx亩
    price = ''      #价格
    date_from = ''  #起始时间
    date_to = ''    #结束时间
    name = ''       #发布人称呼
    tele_num = ''   #联系方式
    place = ''      #地址

    def __init__(self,t,a,pr,df,dt,n,tn,pl):    #初始函数
        self.type = t
        self.area = a
        self.price = pr
        self.date_from = str2date(df)   #输入字符串，转化为date类型
        self.date_to = str2date(dt)
        self.name = n
        self.tele_num = tn
        self.place = pl
        SupplyInform.informCount += 1

    def if_valid(self):       #判断今天是否超过要求时间。如果任务仍然有效，返回True
        return self.date_to.__gt__(datetime.date.today())