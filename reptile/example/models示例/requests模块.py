import requests
from lxml import etree

def main():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')  #设置cookie
    r = s.get("http://httpbin.org/cookies")   #获得cookie
    print(r.text)

    # 超时配置 requests.get('http://github.com', timeout=0.001)

headers_base = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'BIDUPSID=C97D5C700EEF8D4D4DBE015434F673E4; PSTM=1500297086; __cfduid=d9d3af6aa6f3841d47d542786eff6b69a1500540126; BAIDUID=CF6479142EDEA5DB5CCA0C070BD23213;FG=1; MSA_WH=414_736; ispeed_lsm=2; BDUSS=1RaXk2ZFRsR2VyRldteldvYlFxdE90TkhsaGlQSXVFVnpESi10R2x2b2lJQlZhSVFBQUFBJCQAAAAAAAAAAAEAAADyRVMWcWl1YWx1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACKT7Vkik-1ZRG; H_WISE_SIDS=102568_100808_119590_119019_114745_119481_119046_103569_119894_120167_120029_119024_118882_118868_118847_118836_118787_107312_119044_118970_119884_117582_117332_117236_117436_120231_119597_118965_118103_117554_116146_120075_119962_119928_115136_119382_116408_119208_119981_110085; BDSFRCVID=jUCsJeC62Zphd56A3dx7hF_RQmKKSaJTH6aoSaviD9bqnE9HxdYqEG0PqU8g0Ku-dAM-ogKK0mOTHvOP; H_BDCLCKID_SF=fRKJoD_MtKvDj6rl-DTMbt00qxbXq-TP057Z0l8Ktfc2jb-GjxL5bbvWM-jdQqoLW23g3lcmWIQHDUOp54rUetDLh4_8Bnvby664KKJx-xKWeIJo5DcfLfrDhUJiB5OLBan7Lq7xfJOKHICmj5tK3H; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[x4e6higC8W6]=mk3SLVN4HKm; SessionIDKey=3062249358%093062249376kg3x2p; bdkkqt=74b2071c32d019b431d2fe32a9ddaaba; _uck_page=1510488548894659214; _uck_from=10000; ck_refer=baidu; BD_CK_SAM=1; PSINO=2; H_PS_645EC=6d3cHGYIYaaBOO6vVI8QW4sIwNc2uXXnv21jiem5wpqKL9c1zO2jdFPw3xc; BD_HOME=1; H_PS_PSSID=1448_21121_24880_22157; BD_UPN=19314753',
    'DNT':'1',
    'Host':'www.baidu.com',
    'Referer':'https://www.baidu.com/link?url=maPQRtjJV4MSd4UQudCaCBzP9oPlhnTI4nkzdZxDv-3&wd=&eqid=9656f10b0007da40000000025a084d7a',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
}

def xpath_use():
    response = requests.get('http://www.baidu.com',headers=headers_base)
    html = etree.HTML(response.text)
    baidu = html.xpath('//*[@id="su"]/@value')
    print(baidu)


if __name__ == '__main__':
    # main()
    xpath_use()