import datetime
import jieba


def str2date(dt):
    date = datetime.datetime.strptime(dt, "%Y-%m-%d")
    date = datetime.date(date.year, date.month, date.day)
    return date

class SupplyInform:

    informCount = 0

    type = ''
    area = 0
    price = 0
    date_from = ''
    date_to = ''
    name = ''
    tele_num = ''
    place = ''

    def __init__(self,t,a,pr,df,dt,n,tn,pl):
        self.type = t
        self.area = a
        self.price = pr
        self.date_from = str2date(df)
        self.date_to = str2date(dt)
        self.name = n
        self.tele_num = tn
        self.place = pl
        SupplyInform.informCount += 1

    def if_valid(self):       #判断今天是否超过要求时间。如果任务仍然有效，返回True
        return self.date_to.__gt__(datetime.date.today())