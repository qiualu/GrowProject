#coding = utf-8

import requests

headers_base = {
    'GET https':'//www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1',
    'User-Agent': 'Fiddler/4.6.20171.26113 (.NET 4.6.2; WinNT 10.0.15063.0; zh-CN; 4xAMD64; Auto Update; Full Instance; Extensions: APITesting, AutoSaveExt, EventLog, Geoedge, HostsFile, RulesTab2, SAZClipboardFactory, SimpleFilter,Timeline)',
    'Pragma': 'no-cache',
    'Host': 'www.fiddler2.com',
    'Accept-Language': 'zh-CN',
    'Referer': 'http://fiddler2.com/client/TELE/4.6.20171.26113',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close'
}

tran_data = '[{"id":65258,"text":"你好" }]'.encode('utf-8')
response = requests.post('http://fanyi.youdao.com/',headers = headers_base)

print(response.text)
