#!usr/bin/env python3.7
# coding:utf-8
"""
@author: zgw
@file: simple.py
@date: 2020/07/24 10:50
@description 简易版bilibili视频下载
"""
import json
import sys
from you_get import common as you_get  # 导入you-get库

if __name__ == '__main__':

    # 获取的json数据
    json_str=''
    directory = r''  # 设置下载目录
    obj = json.loads(json_str)
    for v in obj['data']['list']['vlist']:
        url = 'https://www.bilibili.com/video/' + v['bvid']
        # sys.argv = ['you-get','-l','-o',directory,url]       #‘-l’是指对于每一个链接中的视频存在多P时按列表下载
        sys.argv = ['you-get', '-o', directory, url]  # sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录。
        you_get.main()
