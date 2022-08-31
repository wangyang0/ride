# -*- coding: UTF-8 -*-
import time
from http import cookiejar
from urllib import request
import json
import random

import jsonpath as jsonpath
import requests as requests


class common(object):
    @staticmethod
    def Get_Cookie(url, companyname, username, password):
        """获取cookie
           参数1 公司名
           参数2 用户名
           参数3 密码
           return cookie"""
        '''
        #举个栗子
        url = "https://puberp.superboss.cc/account/login"
        companyname = "咖啡测试3"
        username = "admin"
        password = "55A86C51427E48F486272A465CE15D73"
        '''
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        data = {
            "companyName": companyname,
            "userName": username,
            "password": password
        }
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            print("登录成功！" + '\n' + "接口返回: %d" % response.status_code)
            dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
            return dict_cookies
        else:
            error_status_code = response.status_code
            print("登录失败！" + '\n' + "接口返回: %d" % error_status_code)

    @staticmethod
    def other_request(url, cookie, data=None):
        """
        发送http请求
        :param req_body: 请求时需手动把\改为\\\
        :return: response的string形式

        Example:
        | *Keywords*           |  *Parameters*  |
post请求 | Send Http Request    |cookie          |url            |req_body
get请求  | Send Http Request    |cookie          |url
        """

        headers = {
            'cache-control': "no-cache"
        }
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        s = requests.session()
        s.keep_alive = False
        # 发送get请求
        if data is None:
            resp = requests.get(url, cookie, headers=headers)
            print("发送get请求，url为：" + url)

        else:
            # 发送post请求,请求参数是json类型
            if data.startswith("{") or data.startswith("["):
                headers["Content-Type"] = "application/json;charset=UTF-8; charset=UTF-8"
                data = data.replace('false', 'False').replace('true', 'True')
                dict_pay = eval(data)
                print("发送post请求，url为：" + url + "；请求参数为：" + data)
                resp = requests.request("POST", url, data=json.dumps(dict_pay), headers=headers)

            else:
                # 发送post请求,请求参数是Form_Data类型
                if data is not None:
                    data = data.encode("utf-8").decode("latin1")
                headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
                print("发送post请求，url为：" + url)
                print("请求参数为：" + data)
                resp = requests.post(url, data=data, headers=headers)

        if str(resp.status_code) != "200":
            raise Exception("请求发送错误，status code:" + str(resp.status_code) + "；错误内容：" + resp.text)
            return False
        else:
            context = resp.text
            print("请求结果为" + context)
            return resp.text

    @staticmethod
    def my_request(method, url, data, cookie):
        '''
        :param mothod: 请求方法
        :param params: 字典或bytes，作为参数增加到url中
        :param data: data类型传参，字典、字节序列或文件对象，作为Request的内容
        :param json: json传参，作为Request的内容
        :param headers: 请求头，字典
        :param cookie: cookie
        :return:
        '''
        print(url)
        try:
            if data == 'None':
                response = requests.request(method, url=url, cookies=cookie, verify=False)
                return response.text
            else:
                response = requests.request(method, url=url, data=eval(data), cookies=cookie)
                return response.text
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

    @staticmethod
    def GetResonseValue(response, path):
        response = response.replace("false", "False").replace("true", "True")
        res = eval(response)
        path1 = "$." + path
        result = jsonpath.jsonpath(res, path1)[0]
        if result is False:
            return False
        elif result is True:
            return True
        else:
            print("获取的结果" + path + "为：" + str(result))
            return str(result)

    def getrandom(self):
        list1 = ['pay', 'end', 'consign']
        sysStatus = random.choice(list1)
        return sysStatus

# if __name__ == "__main__":
#     com=common()
#     url = "https://puberp.superboss.cc/account/login"
#     companyname = "咖啡测试3"
#     username = "yytest"
#     password = "E80A4CCAB76648EC13AE0891B8053D90"
#     cookie = {"_censeid": "fbbfabe0693757e0caa2da648ca9ce0119ff07ab","acw_tc": "3ccdc15216595057319243387e554659268c110e5478aab4bf8a3b821a3c19"}    #cookie = {"acw_tc": "3ccdc16716594968867153960e186adcc42f57a277704755161eceb1bfeebe","_censeid": "bf0bcf1ae548d579f642724aaec5094903158702"}
#     cookie = com.Get_Cookie(url,companyname,username,password)
#     print(cookie)
#     data = 'None'
#     url = "https://puberp.superboss.cc/kmzk/profit/report/shop?api_name=kmzk_profit_report_shop&sysStatus=1&startTime=1658851200000&endTime=1659455999000&shopUniIds=10438_84864&timeOrderType=asc&showDimension=0&ruleId=204987643321253888&showSuit=1&refundSumType=0&consignBeforeRate=&consignAfterRate=&isTrusted=true"
#     url="https://puberp.superboss.cc/kmzk/categoryValuePlan/list/concise?api_name=kmzk_categoryValuePlan_list_concise"
#     result = com.my_request('GET',url,data,cookie)
#     response = '{"code": 0,"data": [],"msg": True}'
#     com.GetResonseValue(response,'msg')
