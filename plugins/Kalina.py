#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from KalinaUtility import Kalina
from Define import Utility
from KalinaUtility import KalinaUtility
# from KalinaWBMonitor import WeiboMonitor
import KalinaCD
import KalinaData

from qqbot import qqbotsched
import random
import time


def onStartupComplete(bot):

    """
    # 启动完成时被调用
    # bot : QQBot 对象，提供 List/SendTo/GroupXXX/Stop/Restart 等接口，详见文档第五节
    """

    group = bot.List('group', Kalina.group_name)[0]
    bot.SendTo(group, '各位指挥官，格林娜摸鱼回来了，我、格林娜、上班！')


def onExit(bot, code, reason, error):

    """
    # MainLoop（主循环）终止时被调用， Mainloop 是一个无限循环，QQBot 登录成功后便开始运
    # 行，当且仅当以下事件发生时 Mainloop 终止：
    #     1） 调用了 bot.Stop() ，此时：
    #         code = 0, reason = 'stop', error = None
    #     2） 调用了 bot.Restart() ，此时：
    #         code = 201, reason = 'restart', error = None
    #     3） 调用了 bot.FreshRestart() ，此时：
    #         code = 202, reason = 'fresh-restart', error = None
    #     4） 调用了 sys.exit(x) （ x 不等于 0,201,202,203 ），此时：
    #         code = x, reason = 'system-exit', error = None
    #     5） 登录的 cookie 已过期，此时：
    #         code = 203, reason = 'login-expire', error = None
    #     6） 发生未知错误 e （暂未出现过，出现则表明 qqbot 程序内部可能存在错误），此时：
    #         code = 1, reason = 'unknown-error', error = e
    #
    # 一般情况下：
    #     发生 1/2/3/4 时，可以安全的调用 bot.List/SendTo/GroupXXX 等接口
    #     发生 5/6 时，调用 bot.List/SendTo/GroupXXX 等接口将出错
    #
    # 一般情况下，用户插件内的代码和运行错误会被捕捉并忽略，不会引起 MainLoop 的退出
    #
    # 本函数被调用后，会执行 sys.exit(code) 退出本次进程并返回到父进程，父进程会根据
    # “ code 的数值” 以及 “是否配置为自动重启模式” 来决定是否重启 QQBot 。
    """

    group = bot.List('group', Kalina.group_name)[0]
    bot.SendTo(group, '各位指挥官，格林娜去摸鱼了，告辞.png')


def onQQMessage(bot, contact, member, content):

    """
    # 当收到 QQ 消息时被调用
    # bot     : QQBot 对象，提供 List/SendTo/GroupXXX/Stop/Restart 等接口，详见文档第五节
    # contact : QContact 对象，消息的发送者
    # member  : QContact 对象，仅当本消息为 群或讨论组 消息时有效，代表实际发消息的成员
    # content : str 对象，消息内容
    """

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

        # 过滤空消息
        if len(message) == 0:
            return

        # 处理触发器开头的消息
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

            return

        # 处理欢迎新人复读
        msg = message.replace(' ', '')
        if KalinaCD.WELCOME_COUNTER == 0 and (msg == '欢迎新大佬' or msg == '欢迎新dalao'):

            # 发出欢迎信息并开启计数器
            KalinaCD.WELCOME_COUNTER += 1
            bot.SendTo(contact, Kalina.welcome)

        # 重置欢迎计数器
        if KalinaCD.WELCOME_COUNTER != 0:
            KalinaCD.WELCOME_COUNTER += 1

            # 50 条消息后可以再次欢迎
            if KalinaCD.WELCOME_COUNTER >= 50:
                KalinaCD.WELCOME_COUNTER = 0

        # 其他消息处理复读机
        if message == KalinaCD.LAST_MESSAGE:

            # 与上一条消息相同
            KalinaCD.LAST_REPEAT_COUNTER += 1

            # 重复 3 次视为复读
            if KalinaCD.LAST_REPEAT_COUNTER > 2:

                # 重置计数器，发送消息
                KalinaCD.LAST_REPEAT_COUNTER = 0
                # bot.SendTo(contact, KalinaCD.LAST_MESSAGE)
                bot.SendTo(contact, Kalina.repeater)

            return

        # 重置复读计数器
        KalinaCD.LAST_REPEAT_COUNTER = 0
        # 更新上一条消息
        KalinaCD.LAST_MESSAGE = message


def handle_msg(bot, contact, member, message):

    """ 处理消息程序 """

    # 处理空消息
    if len(message) == 0:
        return '@' + member.name + '\n' + random.sample(KalinaData.script_moe, 1)[0]

    if message == '查看数据库':
        return '@' + member.name + '\n' + Kalina.tool_website

    if message.startswith('人形经验') or message.startswith('人型经验'):
        m = message.replace('人形经验', '')
        m = m.replace('人型经验', '')
        return KalinaUtility.gf_exp_book(bot, contact, member, m, 0)

    if message.startswith('誓约人形经验') or message.startswith('誓约人型经验'):
        m = message.replace('誓约人形经验', '')
        m = m.replace('誓约人型经验', '')
        return KalinaUtility.gf_exp_book(bot, contact, member, m, 1)

    if message.startswith('妖精经验'):
        m = message.replace('妖精经验', '')
        return KalinaUtility.gf_exp_book(bot, contact, member, m, 2)

    if message.startswith('重装部队经验'):
        m = message.replace('重装部队经验', '')
        return KalinaUtility.gf_exp_book(bot, contact, member, m, 3)

    if message.endswith('妖精信息') or message.endswith('妖精'):
        m = message.replace('信息', '')
        # 仅处理只含妖精名称的信息
        if len(m) == 4 or len(m) == 5 or len(m) == 6 or len(m) == 9:
            return KalinaUtility.gf_fairy_info(bot, contact, member, m)

    if message.startswith('来一发'):
        # 活动期间离线
        if Kalina.during_event:
            return '@' + member.name + '\n' + Kalina.during_event_tip
        # 只在指定时间段内允许建造
        if time.strftime('%H') != '14':
            return '@' + member.name + '\n' + '指挥官！建造模拟只在 22 - 23 点之间开放哦'
        return KalinaUtility.gf_build(bot, contact, member, message.replace('来一发', ''))

    if message.startswith('随机组队'):
        # 此功能需要参与发言 CD 计算
        if not KalinaUtility.kalina_can_reply(member, KalinaCD.RANDOM_GROUP_CD, 3600):
            return ''
        # 随机组队
        return KalinaUtility.gf_random_group(bot, contact, member, message)

    if message.startswith('roll') or message.startswith('Roll') or message.startswith('ROLL'):
        # 活动期间离线
        if Kalina.during_event:
            return '@' + member.name + '\n' + Kalina.during_event_tip
        # 此功能需要参与发言 CD 计算
        if not KalinaUtility.kalina_can_reply(member, KalinaCD.ROLL_CD, 600):
            return ''
        # ROLL
        m = message.replace('roll', '')
        m = m.replace('Roll', '')
        m = m.replace('ROLL', '')
        return Utility.roll(bot, contact, member, m)

    if message.startswith('钦点一人'):
        # 活动期间离线
        if Kalina.during_event:
            return '@' + member.name + '\n' + Kalina.during_event_tip
        # 此功能需要参与发言 CD 计算
        if not KalinaUtility.kalina_can_reply(member, KalinaCD.QINDIAN_CD, 1800):
            return ''
        # 获得钦点的目的用于反馈
        return Utility.qin_dian(bot, contact, member, message.replace('钦点一人', ''), Kalina.group_name, Kalina.group_nickname)

    if Kalina.during_event:
        return '@' + member.name + '\n' + Kalina.help_event
    return '@' + member.name + '\n' + Kalina.help


# @qqbotsched(hour='0', minute='0')
# def morning_call(bot):
#
#     """ 每天早上问候语 """
#
#     try:
#         group = bot.List('group', Kalina.group_name)[0]
#         bot.SendTo(group, '各位指挥官早上好！\n格林娜可没有摸鱼哦~\n新的一天一起努力吧！')
#     except Exception as e:
#         print('[ERROR] GF_TASK_MORNING_CALL: ' + str(e))


@qqbotsched(hour='7', minute='0')
def battery(bot):

    """ 电池刷新提醒 15:00 , 03:00 不提醒 """

    try:
        group = bot.List('group', Kalina.group_name)[0]
        bot.SendTo(group, '各位指挥官！各位指挥官！\n好友宿舍电池刷新啦！\n快去找 10 宿舍 dalao 抱大腿！')
    except Exception as e:
        print('[ERROR] GF_TASK_BATTERY: ' + str(e))


@qqbotsched(day_of_week='3', hour='1', minute='30,45')
def maintenance(bot):

    """ 例行维护时间提醒 """

    try:
        group = bot.List('group', Kalina.group_name)[0]
        bot.SendTo(group, '各位指挥官！各位指挥官！\n10:00 就是例行维护的时间了，\n记得安排好后勤，同时注意样本解析进度、模拟点数不要溢出！\n谎报开服会受到管理制裁！')
    except Exception as e:
        print('[ERROR] GF_TASK_MAINTENANCE: ' + str(e))


# @qqbotsched(day_of_week='0-4', hour='5-11', minute='5,20,35,50')
# def weibo_monitor_weekday(bot):
#
#     """ 官方微博监控 13:05-19:50 每 15 分钟一次 """
#
#     try:
#         w = WeiboMonitor()
#         w.get_record()
#         w.login()
#         w.get_list_url()
#
#         wb_content = w.get_content()
#
#         if len(wb_content) > 0:
#             group = bot.List('group', Kalina.group_name)[0]
#             bot.SendTo(group, '各位指挥官！官方微博有新的动态：\n' + wb_content)
#
#     except Exception as e:
#         print('[ERROR] GF_TASK_WB_MONITOR: ' + str(e))
#
#
# @qqbotsched(day_of_week='5-6', hour='11', minute='0')
# def weibo_monitor_weekend(bot):
#
#     """ 官方微博监控 周六日 19:00 """
#
#     try:
#         w = WeiboMonitor()
#         w.get_record()
#         w.login()
#         w.get_list_url()
#
#         wb_content = w.get_content()
#
#         if len(wb_content) > 0:
#             group = bot.List('group', Kalina.group_name)[0]
#             bot.SendTo(group, '各位指挥官！官方微博有新的动态：\n' + wb_content)
#
#     except Exception as e:
#         print('[ERROR] GF_TASK_WB_MONITOR: ' + str(e))


@qqbotsched(hour='14')
def build_open(bot):

    """ 提醒可以开始建造模拟 """

    try:
        if Kalina.during_event:
            return
        if Kalina.build_up:
            group = bot.List('group', Kalina.group_name)[0]
            bot.SendTo(group, '各位指挥官！各位指挥官！\n模拟建造已开放，持续到 23:00！\n人形和装备可以同时建造了'
                              '\n注意：当前为模拟建造 UP 模式\n祝各位指挥官建造愉快')
        else:
            group = bot.List('group', Kalina.group_name)[0]
            bot.SendTo(group, '各位指挥官！各位指挥官！\n模拟建造已开放，持续到 23:00！\n人形和装备可以同时建造了'
                              '\n建造结果根据「IOP制造公司出货统计」推算\n仅供参考，请指挥官珍惜资源')
    except Exception as e:
        print('[ERROR] QQBOT_TASK_BUILD_OPEN: ' + str(e))
