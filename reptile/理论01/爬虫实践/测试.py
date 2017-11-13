import os
#当前目录
print(os.getcwd())
print(os.path.abspath(os.getcwd()))
path = os.path.abspath('段子.txt')
# print(path)
# with open(path,'r') as f:
#     duanzi = f.readlines()
#     print(duanzi)
#     print(len(duanzi))


for i in range(1,10):
    url = 'https://tieba.baidu.com/p/4772107111?pn=' + str(i)
    print(url)
    print('完成第%s页:' % i)

