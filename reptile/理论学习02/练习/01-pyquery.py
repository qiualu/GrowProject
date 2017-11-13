from pyquery import PyQuery as pq

def shilihua():
    path = 'C:/Users/nirvana/Desktop/xdxx.html'
    with open(path,'r+',encoding='utf-8') as f:
        html = f.read()
        doc = pq(html)
        # print(doc('h4'))
        # for i in doc('h4'):
        #     print('******* :',i)
        #     t = i.text()
        #     print(t)
        h4 = doc('h4')[0]
        print(type(h4))
        for i in h4:
            print(i)

def tiqu():
    doc = pq('http://www.baidu.com')
    print(doc('head').html())
    print('head+-=-=-=-=-=-=-=-0-0-0-+_+_+_=_+_+_+_+_+_+_+_')
    print(doc('title').text())


if __name__ == '__main__':
    tiqu()


