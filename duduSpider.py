import requests

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

if __name__=='__main__':
    url='http://dudu.nongjibang.com/'
    downloadPage(url)
