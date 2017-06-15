#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


# 全局定义
class Define:

    group_name = 'QQBot'
    group_nickname = '摩卡酱'
    group_trigger = '摩卡酱摩卡酱'

    help = '''- 摩卡酱还在测试中，可能发生错误或暴走，请多担待
- 如有问题请 @菜酱 反馈
- 直接在群内发言以下对应文字使用相关功能
    1、生成星盘：
        摩卡酱摩卡酱 生成星盘
    2、星座匹配：
        摩卡酱摩卡酱 星座匹配
    3、星盘匹配：
        摩卡酱摩卡酱 星盘匹配
- 更多功能正在开发中'''

    file_path = ''


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
    if contact.ctype == 'group' and group_name == Define.group_name:

        # 获得消息内容
        message = str(content)

        # 只处理触发器开头的消息
        if message.startswith(Define.group_trigger):

            # 去掉触发器
            message = message.replace(Define.group_trigger, '')

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

    list_astro = ['摩羯座', '水瓶座', '双鱼座', '白羊座',
                  '金牛座', '双子座', '巨蟹座', '狮子座',
                  '处女座', '天秤座', '天蝎座', '射手座']

    member_name = member.name

    # 处理空消息
    if len(message) == 0:
        return '@' + member_name + ' 需要我为您做什么？\n直接发言「' + Define.group_trigger + ' 你能干什么」查看相关帮助'

    if message == '你能干什么':
        bot.SendTo(contact, Define.help)
        return

    if message == '生成星盘':
        return '点击链接生成星盘：\nhttp://www.i-mocca.com/wap/astrolog/'

    if message == '星座匹配':
        return '点击链接进行星座匹配：\nhttp://www.i-mocca.com/wap/astromatchlite/'

    if message == '星盘匹配':
        return '点击链接进行星盘匹配：\nhttp://www.i-mocca.com/wap/astromatch/'

    if message.startswith('钦点一人'):
        # 获得钦点的目的用于反馈
        return qindian(bot, contact, member_name, message.replace('钦点一人', ''))

    return ''


def qindian(bot, contact, member_name, message):

    # 获得当前群组对象
    group = bot.List('group', Define.group_name)[0]
    # 获得群组内成员
    group_members = bot.List(group)
    # 得到昵称列表
    group_members = [str(m)[3:-1] for m in group_members]

    print(group_members)

    # 尝试 10 次
    you = '[群主]'
    for i in range(10):
        # 随机一人
        you = random.choice(group_members)
        # 是自己
        if you != Define.group_nickname:
            break

    return '@' + member_name + ' 通过 ' + Define.group_nickname + ' 钦点了 @' + you + ' ' + message


def readfile(filename):
    """ 读取文件 """
    filename = '%s%s' % (Define.file_path, filename)
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
