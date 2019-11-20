#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Date: 2019/11/16
# @Author: Tigerots


import base64
import hashlib
import hmac
import random
import string
import time
import sys
# 生成指定长度的随机字符串
def RandomConnid(length):
     return  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
# 生成接入物联云需要的各参数
def IotHmac(productID, devicename, devicePsk):
     # 1. 生成connid为一个随机字符串,方便后台定位问题
     connid   = RandomConnid(5)
     # 2. 生成过期时间,表示签名的过期时间,从纪元1970年1月1日 00:00:00 UTC 时间至今秒数的 UTF8 字符串
     expiry   = int(time.time()) + 60 * 60
     # 3. 生成MQTT的clientid部分, 格式为${productid}${devicename}
     clientid = "{}{}".format(productID, devicename)
     # 4. 生成mqtt的username部分, 格式为${clientid};${sdkappid};${connid};${expiry}
     username = "{};12010126;{};{}".format(clientid, connid, expiry)
     # 5. 对username进行签名,生成token
     # token = hmac.new(devicePsk.standard_b64decode(), username, digestmod=hashlib.sha256).hexdigest()
     token = "wbbhC9qJWdQeOEzSHL/FUQ=="
     # 6. 根据物联云通信平台规则生成password字段
     password = "{};{}".format(token, "hmacsha256")
     return {
         "clientid" : clientid,
         "username" : username,
         "password" : password
     }
if __name__ == '__main__':
    My_PRODUCTID  = "HRDQBHLDHS"
    My_DEVICENAME = "TaxiLedV1_2"
    str1 = "wbbhC9qJWdQeOEzSHL/FUQ=="
    My_PSK = "wbbhC9qJWdQeOEzSHL/FUQ=="
    #print("Encoded String: " + My_PSK.encode('base64', 'strict'))

# =======python3 使用base64的方法=====================
    # str3 转成bytes 的string
    str3 = str1.encode(encoding='utf-8', errors='strict')
    print(str3),
    print('')
    # bytes 再进行 base64 编码
    str4 = base64.b64encode(str3)
    print(str4)
    print('')
    # 再base64 decode 一下
    print(str4.decode())
    print('')
    # base64 解码
    enstr = base64.b64decode(str4.decode())
    print(enstr.decode())
    print('')


    aa = IotHmac(My_PRODUCTID, My_DEVICENAME, str4)
    print(aa["clientid"])
    print(aa["username"])
    print(aa["password"])


























# ==========================End============================
