# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/04/05 <https://www.soo9s.com>
"""
import requests

"""
GET

字典只是其中一个  {}
query_data ?data=xx&xxx
req = requests.get(url='', params='')
---
POST
字典 {}
form_data
res = requests.post(url='', data='')
---
关闭证书认证

默认情况下是认证ca证书的 就是我们常说的ssl
res = requests.post(url='', verify=False) verify 不认证

---
代理  -> 目标网站能一眼识别的代理
高速代理 -> 优质的一些代理,目标网站也能识别到
高匿代理 -> 目标网站识别不出来的代理.

网站 https://center.abuyun.com/register#/bind-mobile


---
认证登录

auth = {
    "user":"xxx",
    "pwd":"xxx"
}
res = requests.post(url='', auth=auth)

---
任务: 并且把页面用with open的形式 存储下来 格式是 ".html"

cookies 登录

res = requests.post(url='',cookies='')

cookie_dict = {
    "rpdid": "omqsmwwmwkdosiqxsompw",
    "fts": "1528651876",
    "buvid3": "4F83294A-E846-491C-8DE8-E5F7BDF5AD791343infoc",
    "im_notify_type_16375408": "0",
    "sid": "i58rzpfw",
    "stardustvideo": "1",
    "CURRENT_QUALITY": "112",
    "_uuid": "E40EC099-0EA5-6958-BCFA-984291ACD01437290infoc",
    "CURRENT_FNVAL": "16",
    "UM_distinctid": "168561ec9ce7aa-07cf249943562e-10306653-1fa400-168561ec9cfa1d",
    "LIVE_BUVID": "c64a75a2326713a0ee0d98269408e0c6",
    "LIVE_BUVID__ckMd5": "df875f7314bb2e15",
    "DedeUserID": "16375408",
    "DedeUserID__ckMd5": "e4222f52c608108b",
    "SESSDATA": "3d3aebb0%2C1556116052%2C5505f431",
    "bili_jct": "b3f086d84740e66ebc5c922d6a6d8bc3",
    "stardustpgcv": "0606",
    "bp_t_offset_16375408": "238918331917082560",
}

---

"""
