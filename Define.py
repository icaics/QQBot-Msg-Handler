#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
import datetime


class Global:

    plug_path = '~/usr/download/qqbot'

    fate_today_path = '/usr/download/qqbot/today.json'

    fate_astro_list = ['摩羯座运势', '水瓶座运势', '双鱼座运势', '白羊座运势',
                       '金牛座运势', '双子座运势', '巨蟹座运势', '狮子座运势',
                       '处女座运势', '天秤座运势', '天蝎座运势', '射手座运势']


class Default:

    group_name = ''
    group_nickname = ''
    group_trigger = ''

    help = '''- 机器人还在测试中，可能发生错误或暴走，请多担待\n- 如有问题请 @菜酱 反馈'''


class Test:

    group_name = 'QQBot'
    group_nickname = '测试酱'
    group_trigger = '测试酱测试酱'

    help = '''- 机器人还在测试中，可能发生错误或暴走，请多担待\n- 如有问题请 @菜酱 反馈'''


class Standard:

    group_name = '可说呢！'
    group_nickname = '菜菜酱'
    group_trigger = '菜菜酱菜菜酱'

    help = '''- 菜菜酱还在测试中，可能发生错误或暴走，请多担待\n- 如有问题请 @菜酱 反馈'''


class IMocca:

    group_name = '摩卡星座'
    group_nickname = '摩卡酱'
    group_trigger = '摩卡酱摩卡酱'

    help = '''- 摩卡酱还在测试中，可能发生错误或暴走，请多担待
- 如有问题请 @菜酱 反馈
- 直接在群内发送以下对应文字使用相关功能
    1、生成星盘：
        摩卡酱摩卡酱 生成星盘
    2、星座匹配：
        摩卡酱摩卡酱 星座匹配
    3、星盘匹配：
        摩卡酱摩卡酱 星盘匹配
    4、今日运势（自行替换星座）：
        摩卡酱摩卡酱 白羊座运势
- 更多功能正在开发中'''


class Kalina:

    group_name = ''
    group_nickname = ''
    group_trigger = ''

    help = '''- 机器人还在测试中，可能发生错误或暴走，请多担待\n- 如有问题请 @菜酱 反馈'''


class Utility:

    @staticmethod
    def getfate(bot, contact, member_name, message):

        """ 读取今日运势 """

        try:
            # 初始化日期和运势数据文件
            date = str(datetime.date.today())
            fate = Utility.load_json(Global.fate_today_path)

            # 获取当天运势内容
            fate_today = fate[date]

            # 根据需要的星座返回内容
            if fate_today is not None and len(fate_today) != 0:
                # 获得星座编号
                i = str(Global.fate_astro_list.index(message))
                # 提取对应星座运势
                for astro in fate_today:
                    if astro['xingzuo'] == i:
                        score = '爱情：' + astro['LoveScore'] + ' 分, ' + \
                                '工作：' + astro['JobScore'] + ' 分, ' + \
                                '财富：' + astro['MoneyScore'] + ' 分, ' + \
                                '健康：' + astro['HealthScore'] + ' 分'
                        return '@' + member_name + ' 今天的 ' + message + '：\n' + astro['content'] + '\n' + score

            # 当天运势未更新
            return '@' + member_name + ' 今天的 ' + message + ' 还没有更新'

        except Exception as e:
            print(e)
            return '@' + member_name + ' 今天的 ' + message + ' 出现错误'

    @staticmethod
    def roll(bot, contact, member_name, message):

        """ ROLL 点 """

        try:
            message = str(message)

            # 去掉 []
            message = message.replace('[', '')
            message = message.replace(']', '')

            # 分隔数组
            num = message.split(',')

            result = '@' + member_name + ' ROLL 参数错误，roll[1,100] 可得到包含 1 和 100 之间的随机数'
            if len(num) == 2:
                a = int(num[0])
                b = int(num[1])
                result = '@' + member_name + ' ROLL 出 ' + str(random.randint(a, b)) + ' 点'

            return result

        except Exception as e:
            print(e)
            return '@' + member_name + ' ROLL 参数错误，roll[1,100] 可得到包含 1 和 100 的随机数'

    @staticmethod
    def qindian(bot, contact, member_name, message, group_name, group_nickname):

        """ 钦点一人 """

        try:
            # 获得当前群组对象
            group = bot.List('group', group_name)[0]
            # 获得群组内成员
            group_members = bot.List(group)
            # 得到昵称列表
            group_members = [str(m)[3:-1] for m in group_members]

            # print(group_members)

            # 尝试 10 次
            you = '[群主]'
            for i in range(10):
                # 随机一人
                you = random.choice(group_members)
                # 是自己
                if you != group_nickname:
                    break

            return '@' + member_name + ' 通过 ' + group_nickname + ' 钦点了 @' + you + ' ' + message

        except Exception as e:
            print(e)
            return '@' + member_name + ' 通过 ' + group_nickname + ' 钦点失败 -1s'

    @staticmethod
    def readfile(filename):

        """ 读取文件 """

        try:
            with open(filename, 'r') as file:

                contents = list()
                while True:
                    content = file.readline()
                    if content and len(content) > 0 and content != '\n':
                        content = content.replace('\n', '')
                        contents.append(content)
                    else:
                        break

                file.close()
                return contents

        except Exception as e:
            print(e)
            return None

    @staticmethod
    def load_json(filename):

        """ 读取 JSON 文件 """

        try:
            file = open(filename, encoding='utf-8')
            content = json.load(file)
            return content

        except Exception as e:
            print(e)
            return None
