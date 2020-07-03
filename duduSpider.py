import requests
from bs4 import BeautifulSoup
import InformClass

# http://dudu.nongjibang.com/?p=1

def download_page(url):
    # 下载页面方法，用requests模块，使用代理，避免重复请求次数过多；多开几个进程，加快下载速度
    headers = {
        'Connection': 'close',
        'Content-Type': 'text/html; charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.87 Safari/537.36'}

    try:
        data = requests.get(url, headers=headers).text
        return data
    except BaseException as args:
        print('连接失败'+args)


def get_page_size(url):
    # 获取表格的分页总数
    content = download_page(url)
    soup = BeautifulSoup(content, 'html.parser')
    li = soup.find('div', attrs={"id": "id_page_def"}).findAll("a")
    pageNum = int(li[-1].attrs['page'])
    return pageNum


def get_data(url):
    # 获取表格中的数据，找到有用的几个信息，品种、面积、单价、时间、地点
    content = download_page(url)
    soup = BeautifulSoup(content, 'html.parser')
    tag_list = soup.findAll("div", attrs={"class": "list_box"})
    pageDatas = []
    for i in tag_list:

        inf_str = i.text.replace('\r', ' ').replace('\n', ' ').replace('\t', '') \
            .replace('立即抢单', '').replace('作业时间：', '').replace('至', '') \
            .replace('作业地点：', '').replace('作业热线：', '').replace('一亩', '') \
            .split(' ')
        # 用replace函数替换掉文本中不需要的内容
        inf_str = list(filter(None, inf_str))  # 去掉列表中的空字符
        name = inf_str.pop(0)  # 移动“姓名”属性
        inf_str.insert(5, name)
        try:
            inf_str[7], inf_str[6] = inf_str[6], inf_str[7]  # 调换属性顺序，顺便验证参数是否完整
            inf = InformClass.SupplyInform(inf_str)  # 将得到的字符串列表导入SupplyInform类

        except (IndexError, ValueError):
            continue
        pageDatas.append(inf)  # 添加SupplyInform类对象，得到对象列表
    return pageDatas


def download_data(url):
    # 获取所有数据
    data = []
    pageSize = get_page_size(url)
    for i in range(pageSize):
        durl = url + "?p=" + str(i + 1)
        pageDatas = get_data(durl)
        data.extend(pageDatas)

    return data


def web_spider(url):
    download_page(url)
    return download_data(url)
