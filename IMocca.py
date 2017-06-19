#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Define import Global
from Define import IMocca
from Define import Utility


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
    if contact.ctype == 'group' and group_name == IMocca.group_name:

        # 获得消息内容
        message = str(content)

        # 只处理触发器开头的消息
        if message.startswith(IMocca.group_trigger):

            # 去掉触发器
            message = message.replace(IMocca.group_trigger, '')

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
        return '@' + member_name + ' 需要我为您做什么？\n直接发言「' + IMocca.group_trigger + ' 你能干什么」查看相关帮助'

    if message == '你能干什么':
        bot.SendTo(contact, IMocca.help)
        return

    if message == '生成星盘':
        return '点击链接生成星盘：\nhttp://www.i-mocca.com/wap/astrolog/'

    if message == '星座匹配':
        return '点击链接进行星座匹配：\nhttp://www.i-mocca.com/wap/astromatchlite/'

    if message == '星盘匹配':
        return '点击链接进行星盘匹配：\nhttp://www.i-mocca.com/wap/astromatch/'

    if message in Global.fate_astro_list:
        # 获取指定星座运势
        return Utility.getfate(bot, contact, member_name, message)

    if message.startswith('钦点一人'):
        # 获得钦点的目的用于反馈
        return Utility.qindian(bot, contact, member_name, message.replace('钦点一人', ''), IMocca.group_name, IMocca.group_nickname)

    return ''
