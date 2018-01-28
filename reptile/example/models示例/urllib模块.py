import urllib3

http = urllib3.PoolManager()
# r = http.request('GET','http://www.baidu.com')  # request()方法返回一个HTTPResponse对象。

# 你还可以通过request()方法向请求(request)中添加一些其他信息，如：
# r = http.request(
#     'POST',
#     'http://www.baidu.com',
#     fields = {'hello':'world'}
# )

# 请求(request)中的数据项(request data)可包括：
# Headers:
# 在request()方法中，可以定义一个字典类型(dictionary),并作为headers参数传入：
# r = http.request(
#     'GET',
#     'http://www.baidu.com',
#     headers = {'X-Something':'value'}
# )

# Query parameters:
# 对于GET、HEAD和DELETE请求，可以简单的通过定义一个字典类型作为fields参数传入即可：
# r = http.request(
#     'GET',
#     'http://www.baidu.com',
#     fields = {'hello':'world'}
# )
# 对于POST和PUT请求(request),需要手动对传入数据进行编码，然后加在URL之后：
# from urllib.parse import urlencode
# encoded_args = urlencode({'are':'value'})
# url = 'http:''httpbin.org/post?' + encoded_args
# r = http.request('POST',url)

# JSON:
# 	在发起请求时,可以通过定义body 参数并定义headers的Content-Type参数来发送一个已经过编译的JSON数据：
# import json
# data = {'attribute':'value'}
# encoded_data = json.dumps(data).encode('utf-8')
# r = http.request(
#     'POST',
#     'http://httpbin.org/post',
#     body = encoded_data,
#     headers={'Content-Type':'application/json'}
# )

# Files & binary data:
# 使用multipart/form-data编码方式上传文件,可以使用和传入Form data数据一样的方法进行,并将文件定义为一个元组的形式(file_name,file_data):
# with open('example.txt') as fp:
#     file_data = fp.read()
# r = http.request(
#     'POST',
#     'http://httpbin.org/post',
#     field = {
#         'filefield':('example.txt',file_data),
#     }
# )


# 数据
# r.status
# r.data



