#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import re

from Define import Utility
from Define import Global


class WeiboMonitor:

    """ 代码修改自：https://github.com/naiquann/WBMonitor/ """

    def __init__(self):

        self.session = requests.session()
        self.reqHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://passport.weibo.cn/signin/login',
            'Connection': 'close',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        }
        self.targetID = '5611537367'
        self.userIndex = 'https://m.weibo.cn/api/container/getIndex?uid=%s&type=uid&value=%s' % (self.targetID, self.targetID)
        self.userInfo = 'https://m.weibo.cn/api/container/getIndex?uid=%s&type=uid&value=%s&containerid=' % (self.targetID, self.targetID)

        self.recordFilename = Global.database_path + 'gf_weibo_records'

        self.records = list()

    def get_record(self):

        records = Utility.read_file(self.recordFilename)
        if len(records) > 0:
            self.records = records

    def login(self):

        login_api = 'https://passport.weibo.cn/sso/login'
        login_post_data = {
            'username': '',
            'password': '',
            'savestate': 1,
            'r': '',
            'ec': '0',
            'pagerefer': '',
            'entry': 'mweibo',
            'wentry': '',
            'loginfrom': '',
            'client_id': '',
            'code': '',
            'qq': '',
            'mainpageflag': 1,
            'hff': '',
            'hfp': ''
        }

        # 登录并获取 Session
        try:
            r = self.session.post(login_api, data=login_post_data, headers=self.reqHeaders)
            if r.status_code == 200 and json.loads(r.text)['retcode'] == 20000000:
                print('MONITOR_LOGIN_OK USER_ID: ' + json.loads(r.text)['data']['uid'])
        except Exception as e:
            print('[ERROR] GF_MONITOR_LOGIN:' + str(e))
            return

    def get_list_url(self):

        """ 获取微博列表请求地址 Index """

        # 获得 ContainerID
        container_id = ''
        try:
            r = self.session.get(self.userIndex, headers=self.reqHeaders)
            for i in r.json()['tabsInfo']['tabs']:
                if i['tab_type'] == 'weibo':
                    container_id = i['containerid']

            # 获得 ContainerID，组成完整请求地址
            self.userInfo = self.userInfo + container_id

        except Exception as e:
            print('[ERROR] GF_MONITOR_GET_CONTAINER_ID:' + str(e))
            return

    def get_content(self):

        """ 获取微博内容正文并返回 """

        try:

            r = self.session.get(self.userInfo, headers=self.reqHeaders)

            # 获得微博列表
            for i in r.json()['cards']:

                # 只获取原创微博，且不在记录中
                if i['card_type'] == 9 and 'retweeted_status' not in i['mblog'] and i['mblog']['id'] not in self.records:

                    # 获得目标微博相关信息
                    # data = dict()
                    # data['created_at'] = i['mblog']['created_at']
                    # data['text'] = i['mblog']['text']
                    # data['source'] = i['mblog']['source']
                    # data['nickName'] = i['mblog']['user']['screen_name']

                    text = str(i['mblog']['text'])
                    # print(text)

                    # 替换换行符
                    text.replace('<br/>', '\n')

                    # 去掉 HTML 标签
                    re_text = re.compile(r'<[^>]+>', re.S)
                    text = re_text.sub('', text)

                    # 去掉模板
                    text = text.replace('少女前线官网地址：网页链接', '')

                    # 添加源地址
                    text += '\nhttps://m.weibo.cn/status/' + str(i['mblog']['id'])

                    # 写入记录
                    Utility.save_file(self.recordFilename, str(i['mblog']['id']) + '\n', 'a+')

                    return text

            print('[INFO] GF_MONITOR_NO_NEW_WB')
            return ''

        except Exception as e:
            print('[ERROR] GF_MONITOR_GET_CONTENT:' + str(e))
            return
