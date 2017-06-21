#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Define import Kalina
from Define import Utility

from qqbot import qqbotsched
import random
import time


def onQQMessage(bot, contact, member, content):

    """ QQBot 全局调用入口 """

    # print(bot)
    # print(contact)
    # print(member)
    # print(content)

    # 获取群名称
    group_name = str(contact)
    group_name = group_name[2:-1]
    # print(group_name)

    # 只接收指定群消息
    if contact.ctype == 'group' and group_name == Kalina.group_name:

        # 获得消息内容
        message = str(content)

        # 只处理触发器开头的消息
        if message.startswith(Kalina.group_trigger):

            # 去掉触发器
            message = message.replace(Kalina.group_trigger, '')

            # 去掉 空格 及 @ 符号
            message = message.replace(' ', '')
            message = message.replace('[@ME]', '')

            # 获得处理完成后，等待发送的消息
            result = handle_msg(bot, contact, member, message)

            # 消息非空则回复
            if len(result) > 0:
                bot.SendTo(contact, result)


def handle_msg(bot, contact, member, message):

    """ 处理消息程序 """

    member_name = member.name

    # 处理空消息
    if len(message) == 0:
        return '@' + member_name + '\n' + '指挥官！叫了人家又不说话！哼！\n诶？还不太了解我？嘿嘿嘿\n直接发言「' + Kalina.group_trigger + ' 你能做什么」查看我能帮您做什么吧'

    if message == '你能做什么':
        return '@' + member_name + '\n' + Kalina.help

    # 以下功能需要参与发言 CD 计算
    if not Utility.kalina_can_reply(member_name):
        return ''

    if message == '卖个萌':
        return '@' + member_name + '\n' + random.sample(Kalina.script_moe, 1)[0]

    if message == '建造数据库':
        return '@' + member_name + '\n' + '指挥官！请查阅「IOP 制造公司出货统计」：\n' + 'http://gfdb.baka.pw/statistician.html'

    if message.startswith('来一发'):
        # 只在 22 - 23 点之间允许建造
        if time.strftime('%H') != '22':
            return '@' + member_name + '\n' + '指挥官！建造模拟只在 22 - 23 点之间开放，请不要刷屏建造哦！'
        return Utility.gf_build(bot, contact, member_name, message.replace('来一发', ''))

    if message.startswith('roll') or message.startswith('Roll') or message.startswith('ROLL'):
        # ROLL
        m = message.replace('roll', '')
        m = m.replace('Roll', '')
        m = m.replace('ROLL', '')
        return Utility.roll(bot, contact, member_name, m)

    if message.startswith('钦点一人'):
        # 获得钦点的目的用于反馈
        return Utility.qin_dian(bot, contact, member_name, message.replace('钦点一人', ''), Kalina.group_name, Kalina.group_nickname)

    return ''


@qqbotsched(hour='7')
def battery(bot):

    """ 电池刷新提醒 1500 , 0300 不提醒 """

    try:
        group = bot.List('group', Kalina.group_name)[0]
        bot.SendTo(group, '各位指挥官！各位指挥官！\n好友宿舍电池刷新啦！\n快去找 10 宿舍 dalao 抱大腿！')
    except Exception as e:
        print('QQBOT_TASK_BATTERY_E: ' + str(e))


@qqbotsched(day_of_week='3', hour='1', minute='30')
def maintenance(bot):

    """ 例行维护时间提醒 0930 """

    try:
        group = bot.List('group', Kalina.group_name)[0]
        bot.SendTo(group, '各位指挥官！各位指挥官！\n还有半个小时就是例行维护的时间了，\n记得安排好后勤，同时注意模拟点数不要溢出哦！')
    except Exception as e:
        print('QQBOT_TASK_MAINTENANCE_E: ' + str(e))


@qqbotsched(hour='14')
def build_open(bot):

    """ 提醒可以开始建造模拟 """

    try:
        group = bot.List('group', Kalina.group_name)[0]
        bot.SendTo(group, '各位指挥官！各位指挥官！\n模拟建造已开放，持续到 23:00！'
                          '\n请各位指挥官协商好，不要大量刷屏建造！\n请各位指挥官协商好，不要大量刷屏建造！\n请各位指挥官协商好，不要大量刷屏建造！'
                          '\n建造结果根据「IOP制造公司出货统计」推算：\nhttp://gfdb.baka.pw/statistician.html\n结果仅供参考，请指挥官珍惜资源')
    except Exception as e:
        print('QQBOT_TASK_BUILD_OPEN_E: ' + str(e))
