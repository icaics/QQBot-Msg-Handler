#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Define import Global
from Define import Utility
import KalinaCD

import time
import random
import math


class Kalina:

    during_event = False
    during_event_tip = '指挥官！活动期间功能离线，请专心攻略活动'

    build_up = False

    group_name = '少女前线-水果茶水间'
    group_nickname = '后勤官格林娜'
    group_trigger = '格林娜格林娜'

    # group_name = 'QQBot'
    # group_nickname = '测试酱'
    # group_trigger = '测试酱测试酱'

    help_event = '''- 发送「格林娜格林娜」加命令使用对应功能
    1.查看数据库
    2.(誓约)人形经验 a-b
    3.妖精经验 a-b
    4.〇〇妖精
    5.活动期间离线
    6.活动期间离线
    7.活动期间离线
    8.活动期间离线
- 发现问题请 @菜菜酱'''

    help = '''- 发送「格林娜格林娜」加命令使用对应功能
    1.查看数据库
    2.(誓约)人形经验 a-b
    3.妖精经验 a-b
    4.〇〇妖精
    5.来一发普建/枪种建造 (10)
    6.来一发人形/装备重建〇档 (10)
    7.ROLL (10)
    8.钦点一人〇〇 (30)
- 发现问题请 @菜菜酱'''

    t_doll_exp = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                  1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
                  2100, 2200, 2300, 2400, 2500, 2600, 2800, 3100, 3400, 4200,
                  4600, 5000, 5400, 5800, 6200, 6700, 7200, 7700, 8200, 8800,
                  9300, 9900, 10500, 11100, 11800, 12500, 13100, 13900, 14600, 15400,
                  16100, 16900, 17700, 18600, 19500, 20400, 21300, 22300, 23300, 24300,
                  25300, 26300, 27400, 28500, 29600, 30800, 32000, 33200, 34400, 45100,
                  46800, 48600, 50400, 52200, 54000, 55900, 57900, 59800, 61800, 63900,
                  66000, 68100, 70300, 72600, 74800, 77100, 79500, 81900, 84300, 112600,
                  116100, 119500, 123100, 126700, 130400, 134100, 137900, 141800, 145700,
                  100000, 120000, 140000, 160000, 180000, 200000, 220000, 240000, 280000, 360000,
                  480000, 640000, 900000, 1200000, 1600000, 2200000, 3000000, 4000000, 5000000, 6000000]

    t_doll_exp_oath = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                       1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
                       2100, 2200, 2300, 2400, 2500, 2600, 2800, 3100, 3400, 4200,
                       4600, 5000, 5400, 5800, 6200, 6700, 7200, 7700, 8200, 8800,
                       9300, 9900, 10500, 11100, 11800, 12500, 13100, 13900, 14600, 15400,
                       16100, 16900, 17700, 18600, 19500, 20400, 21300, 22300, 23300, 24300,
                       25300, 26300, 27400, 28500, 29600, 30800, 32000, 33200, 34400, 45100,
                       46800, 48600, 50400, 52200, 54000, 55900, 57900, 59800, 61800, 63900,
                       66000, 68100, 70300, 72600, 74800, 77100, 79500, 81900, 84300, 112600,
                       116100, 119500, 123100, 126700, 130400, 134100, 137900, 141800, 145700,
                       50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 140000, 180000,
                       240000, 320000, 450000, 600000, 800000, 1100000, 1500000, 2000000, 2500000, 3000000]

    fairy_exp = [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000,
                 3300, 3600, 3900, 4200, 4500, 4800, 5100, 5500, 6000, 6500,
                 7100, 8000, 9000, 10000, 11000, 12200, 13400, 14700, 16000, 17500,
                 18900, 20500, 22200, 23900, 25700, 27600, 29500, 31600, 33700, 35900,
                 38200, 40500, 43000, 45500, 48200, 50900, 53700, 56600, 59600, 62700,
                 65900, 69200, 72600, 76000, 79600, 83300, 87000, 90900, 94900, 99000,
                 103100, 107400, 111800, 116300, 120900, 125600, 130400, 135300, 140400, 145500,
                 150800, 156100, 161600, 167200, 172900, 178700, 184700, 190700, 196900, 203200,
                 209600, 216100, 222800, 229600, 236500, 243500, 250600, 257900, 265300, 272800,
                 280400, 288200, 296100, 304100, 312300, 320600, 329000, 337500, 357000]

    fairy_info = [['勇士妖精', '04:30:00', '战斗', '25 %', '80 %', '40 %', '10 %', '0 %', '0'],
                  ['暴怒妖精', '04:35:00', '战斗', '15 %', '0 %', '40 %', '10 %', '40 %', '0'],
                  ['盾甲妖精', '03:00:00', '战斗', '22 %', '0 %', '0 %', '25 %', '22 %', '0'],
                  ['护盾妖精', '03:05:00', '战斗', '20 %', '60 %', '80 %', '0 %', '0 %', '0'],
                  ['防御妖精', '04:10:00', '策略', '22 %', '0 %', '80 %', '20 %', '0 %', '1'],
                  ['嘲讽妖精', '03:10:00', '战斗', '18 %', '58 %', '28 %', '8 %', '25 %', '0'],
                  ['狙击妖精', '03:30:00', '战斗', '0 %', '88 %', '28 %', '15 %', '36 %', '0'],
                  ['炮击妖精', '03:35:00', '战斗', '55 %', '0 %', '56 %', '6 %', '0 %', '0'],
                  ['空袭妖精', '03:40:00', '战斗', '30 %', '50 %', '40 %', '10 %', '0 %', '0'],
                  ['增援妖精', '04:00:00', '策略', '12 %', '0 %', '88 %', '12 %', '15 %', '1'],
                  ['空降妖精', '04:05:00', '策略', '36 %', '0 %', '32 %', '8 %', '40 %', '5'],
                  ['布雷妖精', '05:30:00', '策略', '25 %', '44 %', '85 %', '0 %', '0 %', '3'],
                  ['火箭妖精', '05:35:00', '策略', '0 %', '44 %', '0 %', '22 %', '35 %', '3'],
                  ['工事妖精', '05:40:00', '策略', '15 %', '50 %', '40 %', '10 %', '20 %', '3'],
                  ['指挥妖精', '05:00:00', '策略', '36 %', '0 %', '32 %', '8 %', '36 %', '1'],
                  ['搜救妖精', '05:05:00', '策略', '32 %', '80 %', '64 %', '0 %', '0 %', '1'],
                  ['照明妖精', '05:10:00', '策略', '0 %', '90 %', '32 %', '8 %', '38 %', '5'],
                  ['黄金妖精', '05:10:00', '战斗', '20 %', '62 %', '50 %', '12 %', '25 %', '0']]

    script_moe = ["指挥官，我好饿啊 ...",
                  "指挥官，用过餐点了吗",
                  "指挥官，你要买东西吗？要就给你便宜点也不是不行哦 ~",
                  "指挥官，所谓的奇迹啊，就要靠我纯真的魔法，和一点点钞票啦",
                  "指挥官，今天又要买什么？都算你便宜哟！",
                  "嘻嘻嘻，又有好多小钱钱 ... 咦！指挥官你在啊！",
                  "最近物资挤压啊 ... 啊，指挥官！来得正好，现在特别算你便宜哦！",
                  "哼哼哼 ... 啊，指挥官，今天心情不错，都算你便宜点哦 ~",
                  "指挥官，在这样出手阔绰，我可要着迷了呢 ... 虽然是对钞票啦 ~",
                  "指挥官，你这么大方，人家 ... 也不会给你便宜哦！",
                  "其实 ... 也没有多喜欢钱啦，但是，也没出现更喜欢的东西呢",
                  "指挥官，不要忙得太过火哦，必要时请花点钱省心吧",
                  "除了这些、那些，和那边那些，基本都是进货价呢，并没有骗您哦",
                  "想更了解我 ... 吗，人家要不要把私密权限也卖给您呢，可惜没有那种东西啦",
                  "美好的一天呢，是不是该花点钱，让它更美好一点呢？",
                  "诶？没钱了？真是没办法今天就特别给你打点折好了",
                  "随便聊聊也是可以的哦，看在您是老主顾的份上，破例免费一次吧",
                  "指挥官，要来点点心吗？",
                  "东西快堆不下了 ... 指挥官，快拿走一些吧，成本价卖你了",
                  "虽然有句名言“不要被金钱支配，要去支配金钱”，但我是不会支配您的，指挥官大人！",
                  "稍稍做个游戏吧，您赢了，就打赏人家一点，输了的话，就买些东西，如何呢？",
                  "指挥官！再多买一些就给你特别的惊喜哦！",
                  "我为您破例打了那么多折扣，而我对您的爱慕之心，可从来没有打折过哦",
                  "别忘了我们的特殊契约哦，金钱只是付出的一部分呢"]


class KalinaUtility:

    @staticmethod
    def kalina_can_reply(member, list_cd_counter, seconds):

        """ 判断是否响应当前成员消息 """

        # 遍历发言记录
        for m in list_cd_counter:
            # 获得当前成员记录
            if m['name'] == member.name:
                # 不在限制内
                if time.time() - m['time'] > seconds:
                    # 冷却超过 10 分钟，可以响应，更新数据
                    m['time'] = time.time()
                    return True
                # 在限制内
                return False

        # 未找到当前成员，可以响应，更新数据
        data = dict()
        data['name'] = member.name
        data['time'] = time.time()
        list_cd_counter.append(data)

        return True

    @staticmethod
    def gf_build(bot, contact, member, message):

        """ 人形建造模拟 """

        try:
            if message == '普建':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_4442.json')
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：430, 430, 430, 230' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '手枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_1111.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：130, 130, 130, 130' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '冲锋枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_4412.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：430, 430, 130, 230' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '突击步枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_1442.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：130, 430, 430, 230' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '步枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_4142.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：430, 130, 430, 230' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '机枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_7614.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：730, 630, 130, 430' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '重建一级' or message == '重建一档' or message == '重建一挡' or message == '人形重建一级' or message == '人形重建一档' or message == '人形重建一挡':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(KalinaUtility.get_datebase_path() + 'gf_b_c_6264_1.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：6K, 2K, 6K, 4K, 1/3' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '重建二级' or message == '重建二档' or message == '重建二挡' or message == '人形重建二级' or message == '人形重建二档' or message == '人形重建二挡':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(KalinaUtility.get_datebase_path() + 'gf_b_c_6264_2.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：6K, 2K, 6K, 4K, 20/5' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '重建三级' or message == '重建三档' or message == '重建三挡' or message == '人形重建三级' or message == '人形重建三档' or message == '人形重建三挡':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(KalinaUtility.get_datebase_path() + 'gf_b_c_6264_3.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：6K, 2K, 6K, 4K, 50/10' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '装备重建一级' or message == '装备重建一档' or message == '装备重建一挡':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_EQUIP_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_e_2222_1.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：2K5, 2K5, 2K5, 2K5, 1/2' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '装备重建二级' or message == '装备重建二档' or message == '装备重建二挡':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_EQUIP_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_e_2222_2.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：2K5, 2K5, 2K5, 2K5, 20/4' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message == '装备重建三级' or message == '装备重建三档' or message == '装备重建三挡':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_EQUIP_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_e_2222_3.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：2K5, 2K5, 2K5, 2K5, 50/6' + '\n建造结果：' + data[0] + ' ' + data[1]

            else:
                # 建造方式错误不触发发言 CD
                return '@' + member.name + '\n' + '指挥官！建造姿势错误，资源大破！\n请使用「来一发」加上：\n普建、手枪建造、冲锋枪建造\n突击步枪建造、' \
                                                  '步枪建造、机枪建造\n人形、装备重建一二三档'
        except Exception as e:
            print('[ERROR] GF_BUILD: ' + str(e))
            return '@' + member.name + '\n' + '人形建造模拟出现错误'

    @staticmethod
    def gf_build_calculate(results):

        """ 建造模拟 按几率生成结果 """

        # 当前已遍历总概率（低 - 高）
        rate = 0
        # 随机本次建造概率
        rand = random.randint(0, 99000)

        # 遍历建造几率数据库
        for data in results:
            rate += float(data[3]) * 1000
            if rand < rate:
                # 符合当前概率
                return data
        # print(rate)
        return None

    @staticmethod
    def gf_exp_book(bot, contact, member, message, cal_type):

        """ 计算人形 / 妖精所需经验书数量 """

        try:
            message = str(message)

            data = [Kalina.t_doll_exp, Kalina.t_doll_exp_oath, Kalina.fairy_exp]
            name = ['人形', '誓约人形', '妖精']

            # 如果无参数
            if len(message) == 0:
                return '@' + member.name + '\n' + '指挥官！等级参数错误，a-b 可计算从等级 a 到等级 b 所需的经验书数量'

            # 去掉 []
            message = message.replace('[', '')
            message = message.replace(']', '')

            # 分隔数组
            num = message.split('-')

            result = '@' + member.name + '\n' + '指挥官！等级参数错误，a-b 可计算从等级 a 到等级 b 所需的经验书数量'
            if len(num) == 2:

                a = int(num[0])
                b = int(num[1])

                # 排除不合法参数
                if (cal_type == 0 or cal_type == 1) and (a < 1 or b < 2 or a > 119 or b > 120 or a >= b):
                    return result
                if cal_type == 2 and (a < 1 or b < 2 or a > 99 or b > 100 or a >= b):
                    return result

                # 计算
                exp = sum(data[cal_type][a - 1:b - 1])
                books = math.ceil(exp / 3000)

                result = '@' + member.name + '\n' + '指挥官！' + name[cal_type] + '从 ' + str(a) + '-' + str(b) + ' 级\n' + \
                         '共需要经验 ' + str(exp) + ' \n共需要经验书 ' + str(books) + ' 本'

            return result

        except Exception as e:
            print('[ERROR] GF_EXP_BOOK:' + str(e))
            return '@' + member.name + '\n' + '计算经验书消耗出现错误'

    @staticmethod
    def gf_fairy_info(bot, contact, member, message):

        """ 查询妖精信息 """

        try:
            message = str(message)

            result = '@' + member.name + '\n' + '指挥官！未找到指定妖精信息...'
            for fairy in Kalina.fairy_info:

                # 返回对应妖精信息 0 %
                if message == fairy[0]:
                    result = '@' + member.name + '\n' + '指挥官！' + message + ' 信息如下：' + \
                             '\n建造时间：' + fairy[1] + '\n类型：' + fairy[2]
                    # 根据是否有加成 组成信息
                    if fairy[3] != '0 %':
                        result += '\n伤害加成：' + fairy[3]
                    if fairy[4] != '0 %':
                        result += '\n命中加成：' + fairy[4]
                    if fairy[5] != '0 %':
                        result += '\n闪避加成：' + fairy[5]
                    if fairy[6] != '0 %':
                        result += '\n装甲加成：' + fairy[6]
                    if fairy[7] != '0 %':
                        result += '\n暴伤加成：' + fairy[7]
                    # 添加 CD 回合信息
                    result += '\n主要技能 CD 回合：' + fairy[8]

            return result

        except Exception as e:
            print('[ERROR] GF_FAIRY_INFO:' + str(e))
            return '@' + member.name + '\n' + '查询妖精信息出现错误'

    @staticmethod
    def get_datebase_path():

        """ 仅人形重建三个档位参与建造 UP """

        if Kalina.build_up:
            return Global.database_up_path
        else:
            return Global.database_path
