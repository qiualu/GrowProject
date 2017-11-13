
from bs4 import BeautifulSoup

soup = BeautifulSoup(
    'html_doc',   #HTML文档字符串
    'html.parser',  #HTML解析器
    from_encoding = 'utf8' #HTML文档的编码
)


