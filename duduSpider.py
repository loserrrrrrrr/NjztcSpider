import requests
from bs4 import BeautifulSoup

def downloadPage(url):
    # 下载页面方法，用requests模块，使用代理，避免重复请求次数过多；多开几个进程，加快下载速度
    headers = {
        'Connection': 'close',
        'Content-Type':'text/html; charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36' }

    try:
        data = requests.get(url, headers=headers).text
        return data
    except BaseException:
        if(url in errordic):
            errordic[url] = errordic[url]+1
        else:
            errordic[url] =1
        if(errordic[url]<4):
            print(url + '【第】'+str(errordic[url])+'次重试】')
            return downloadPage(url)
        else:
            print(url + '【下载页面失败】')
            return ''

def getPageSize(url):
    # 获取表格的分页总数
    content = downloadPage(url)
    soup = BeautifulSoup(content, 'html.parser')
    list = soup.find('div', attrs={"id": "id_page_def"}).findAll("a")
    pageNum = int(list[-1].attrs['page'])
    return pageNum

def getData(url):
    # 获取表格中的数据，找到有用的几个信息，品种、面积、单价、时间、地点
    content = downloadPage(url)
    soup = BeautifulSoup(content, 'html.parser')
    list = soup.findAll("div",attrs={"class":"list_box"})
    pageDatas = []
    res = {}

    for i in list:
        h1s = i.find("div",attrs={"class":"js_right"}).find("div",attrs={"class":"list_name"}).findAll("h1")
        dts = i.find("div",attrs={"class":"js_right"}).find("dl").findAll("dt")
        pageDatas.append(h1s)
        pageDatas.append(dts)
        print(pageDatas)
        #res[dts[0].get_text()] = dts[1].get_text()
    return pageDatas

def downloadData(url):
    #获取所有数据
    Data = []
    pageSize = getPageSize(url)

    for i in range(pageSize):
        print("[当前页数]" + str(i+1))
        durl = url + "?p=" + str(i + 1)
        pageDatas = getData(durl)
        Data.extend(pageDatas)
        #print(Data)
    return 'success'

if __name__=='__main__':
    url='http://dudu.nongjibang.com/'
    downloadPage(url)
    getPageSize(url)
    downloadData(url)
