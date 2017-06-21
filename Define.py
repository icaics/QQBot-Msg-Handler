#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
import datetime


class Global:

    plug_path = '~/.qqbot-tmp/plugins/'

    database_path = '/usr/download/qqbot/'

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

    group_name = '少女前线 IOS 11服 NTW-20'
    group_nickname = '后勤官格林娜'
    group_trigger = '格林娜格林娜'

    help = '''- 格林娜的傀儡人形还在测试中，可能发生错误或暴走，请多担待
- 直接在群内发送「格林娜格林娜」加上以下文字使用对应功能
    1、卖个萌
    2、建造数据库
    3、来一发普建
    4、来一发手枪/冲锋枪/突击步枪/步枪/机枪建造
    5、来一发重建一/二/三级
    6、ROLL[1-100]
    7、钦点一人 ***（*** 可以是做什么）
- 提醒各位指挥官好友电池刷新及例行维护时间
- 以上功能和提醒可能因为心智云图问题失效
- 如有问题请 @菜菜酱 反馈'''

    script_moe = ["指挥官，我好饿啊 ...",
                  "指挥官，用过餐点了吗",
                  "呜嘻嘻嘻嘻嘻 ...",
                  "指挥官，你要买东西吗？要就给你便宜点也不是不行哦 ~",
                  "指挥官，所谓的奇迹啊，就要靠我纯真的魔法，和一点点钞票啦",
                  "呵呵呵呵呵呵 ...",
                  "指挥官，今天又要买什么？都算你便宜哟！",
                  "嘻嘻嘻，又有好多小钱钱 ... 咦！指挥官你在啊！",
                  "不着急呢，请您慢慢来吧",
                  "Yeah！",
                  "最近物资挤压啊 ... 啊，指挥官！来得正好，现在特别算你便宜哦！",
                  "哼哼哼 ... 啊，指挥官，今天心情不错，都算你便宜点哦 ~",
                  "哈哈哈哈哈哈！",
                  "指挥官，在这样出手阔绰，我可要着迷了呢 ... 虽然是对钞票啦 ~",
                  "指挥官，你这么大方，人家 ... 也不会给你便宜哦！",
                  "呼呼呼 ...",
                  "其实 ... 也没有多喜欢钱啦，但是，也没出现更喜欢的东西呢",
                  "指挥官，不要忙得太过火哦，必要时请花点钱省心吧",
                  "除了这些、那些，和那边那些，基本都是进货价呢，并没有骗您哦",
                  "哇啊！",
                  "想更了解我 ... 吗，人家要不要把私密权限也卖给您呢，可惜没有那种东西啦",
                  "美好的一天呢，是不是该花点钱，让它更美好一点呢？",
                  "诶？没钱了？真是没办法今天就特别给你打点折好了",
                  "随便聊聊也是可以的哦，看在您是老主顾的份上，破例免费一次吧",
                  "咔哈哈哈哈哈",
                  "指挥官，要来点点心吗？",
                  "东西快堆不下了 ... 指挥官，快拿走一些吧，成本价卖你了",
                  "虽然有句名言“不要被金钱支配，要去支配金钱”，但我是不会支配您的，指挥官大人！",
                  "诶嘿嘿嘿嘿嘿 ...",
                  "稍稍做个游戏吧，您赢了，就打赏人家一点，输了的话，就买些东西，如何呢？",
                  "指挥官！再多买一些就给你特别的惊喜哦！",
                  "我为您破例打了那么多折扣，而我对您的爱慕之心，可从来没有打折过哦",
                  "别忘了我们的特殊契约哦，金钱只是付出的一部分呢"]


class Utility:

    @staticmethod
    def get_fate(bot, contact, member_name, message):

        """ 读取今日运势 """

        try:
            # 初始化日期和运势数据文件
            date = str(datetime.date.today())
            fate = Utility.load_json(Global.database_path + 'today.json')

            # 获取当天运势内容
            if fate:
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
            print('GET_FATE_E: ' + str(e))
            return '@' + member_name + ' 今天的 ' + message + ' 出现错误'

    @staticmethod
    def gf_build(bot, contact, member_name, message):

        """ 少女前线 战术少女建造模拟 """

        try:
            post_fix = '\n建造结果根据「IOP制造公司出货统计」推算：\nhttp://gfdb.baka.pw/statistician.html\n结果仅供参考，请指挥官珍惜资源'

            if message == '普建':
                results = Utility.load_json(Global.database_path + 'gf_b_c_4442.json')
                data = Utility.gf_build_calculate(results)
                return '@' + member_name + '\n指挥官！建造结果如下：\n公式：430, 430, 430, 230' + \
                       '\n时间：' + data[2] + '\n星级：' + data[0] + '\n人形：' + data[1] + post_fix
            elif message == '手枪建造':
                results = Utility.load_json(Global.database_path + 'gf_b_c_1111.json')
                data = Utility.gf_build_calculate(results)
                return '@' + member_name + '\n指挥官！建造结果如下：\n公式：130, 130, 130, 130' + \
                       '\n时间：' + data[2] + '\n星级：' + data[0] + '\n人形：' + data[1] + post_fix
            elif message == '冲锋枪建造':
                results = Utility.load_json(Global.database_path + 'gf_b_c_4412.json')
                data = Utility.gf_build_calculate(results)
                return '@' + member_name + '\n指挥官！建造结果如下：\n公式：430, 430, 130, 230' + \
                       '\n时间：' + data[2] + '\n星级：' + data[0] + '\n人形：' + data[1] + post_fix
            elif message == '突击步枪建造':
                results = Utility.load_json(Global.database_path + 'gf_b_c_1442.json')
                data = Utility.gf_build_calculate(results)
                return '@' + member_name + '\n指挥官！建造结果如下：\n公式：130, 430, 430, 230' + \
                       '\n时间：' + data[2] + '\n星级：' + data[0] + '\n人形：' + data[1] + post_fix
            elif message == '步枪建造':
                results = Utility.load_json(Global.database_path + 'gf_b_c_4142.json')
                data = Utility.gf_build_calculate(results)
                return '@' + member_name + '\n指挥官！建造结果如下：\n公式：430, 130, 430, 230' + \
                       '\n时间：' + data[2] + '\n星级：' + data[0] + '\n人形：' + data[1] + post_fix
            elif message == '机枪建造':
                results = Utility.load_json(Global.database_path + 'gf_b_c_7614.json')
                data = Utility.gf_build_calculate(results)
                return '@' + member_name + '\n指挥官！建造结果如下：\n公式：730, 630, 130, 430' + \
                       '\n时间：' + data[2] + '\n星级：' + data[0] + '\n人形：' + data[1] + post_fix
            elif message == '重建一级':
                results = Utility.load_json(Global.database_path + 'gf_b_c_6264_1_3.json')
                data = Utility.gf_build_calculate(results)
                return '@' + member_name + '\n指挥官！建造结果如下：\n公式：6K, 2K, 6K, 4K, 1/3' + \
                       '\n时间：' + data[2] + '\n星级：' + data[0] + '\n人形：' + data[1] + post_fix
            elif message == '重建二级':
                results = Utility.load_json(Global.database_path + 'gf_b_c_6264_20_5.json')
                data = Utility.gf_build_calculate(results)
                return '@' + member_name + '\n指挥官！建造结果如下：\n公式：6K, 2K, 6K, 4K, 20/5' + \
                       '\n时间：' + data[2] + '\n星级：' + data[0] + '\n人形：' + data[1] + post_fix
            elif message == '重建三级':
                results = Utility.load_json(Global.database_path + 'gf_b_c_6264_50_10.json')
                data = Utility.gf_build_calculate(results)
                return '@' + member_name + '\n指挥官！建造结果如下：\n公式：6K, 2K, 6K, 4K, 50/10' + \
                       '\n时间：' + data[2] + '\n星级：' + data[0] + '\n人形：' + data[1] + post_fix
            else:
                return '@' + member_name + '\n' + '建造姿势错误，请使用「来一发」加以下关键字进行建造：\n普建、手枪建造、冲锋枪建造\n突击步枪建造、' \
                                                  '步枪建造、机枪建造\n重建一级、重建二级、重建三级'
        except Exception as e:
            print('GF_BUILD_E: ' + str(e))
            return '@' + member_name + '\n' + message + ' 出现错误，资源大破！'

    @staticmethod
    def gf_build_calculate(results):

        # 当前已遍历总概率（低 - 高）
        rate = 0
        # 随机本次建造概率
        rand = random.randint(0, 100000)

        # 遍历建造几率数据库
        for data in results:
            rate += float(data[3]) * 1000
            if rand < rate:
                # 符合当前概率
                return data
        # print(rate)
        return None

    @staticmethod
    def roll(bot, contact, member_name, message):

        """ ROLL 点 """

        try:
            message = str(message)

            # 去掉 []
            message = message.replace('[', '')
            message = message.replace(']', '')

            # 分隔数组
            num = message.split('-')

            result = '@' + member_name + ' ROLL 参数错误，ROLL[1-100] 可得到包含 1 和 100 之间的随机数'
            if len(num) == 2:
                a = int(num[0])
                b = int(num[1])
                result = '@' + member_name + ' ROLL 出 ' + str(random.randint(a, b)) + ' 点'

            return result

        except Exception as e:
            print('ROLL_E:' + str(e))
            return '@' + member_name + ' ROLL 参数错误，ROLL[1-100] 可得到包含 1 和 100 的随机数'

    @staticmethod
    def qin_dian(bot, contact, member_name, message, group_name, group_nickname):

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
            print('QINDIAN_E: ' + str(e))
            return '@' + member_name + ' 通过 ' + group_nickname + ' 钦点失败'

    @staticmethod
    def read_file(filename):

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
            print('READFILE_E:' + str(e))
            return None

    @staticmethod
    def load_json(filename):

        """ 读取 JSON 文件 """

        try:
            file = open(filename, encoding='utf-8')
            content = json.load(file)
            return content

        except Exception as e:
            print('LOADJSON_E:' + str(e))
            return None
