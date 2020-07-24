#  哔哩哔哩视频批量下载

## 依赖&运行说明
**Python3.7**+**pip**

安装依赖
```python
pip install 
```


## 1.simple.py
批量下载space中某页全部视频，也可修改代码使`json_str`参数为获取的所有页面视频返回内容

1.浏览器打开某用户空间
```python
https://space.bilibili.com/***/video
```
2.F12查看请求中如下请求
```python
Request URL: https://api.bilibili.com/x/space/arc/
```
3.复制返回json数据结果，进行赋值
```python
json_str = '{"code":0,"message":"0","ttl":1,"data":{"list":{"tlist":{......}}'
```
4.设置下载路径，如
```python
directory=r'D:\bilibili'
```
5.运行代码