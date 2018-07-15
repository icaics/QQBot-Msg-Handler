#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Define import Global
from Define import Utility
import KalinaData
import KalinaCD

import time
import random
import math
import operator


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
    5.随机组队（60）
    6.活动期间离线
    7.活动期间离线
    8.活动期间离线
    9.活动期间离线'''

    help = '''- 发送「格林娜格林娜」加命令使用对应功能
    1.查看数据库
    2.(誓约)人形经验 a-b
    3.妖精经验 a-b
    4.〇〇妖精
    5.随机组队（60）
    6.来一发普建/枪种建造 (10)
    7.来一发人形/装备重建〇档 (10)
    8.ROLL (10)
    9.钦点一人〇〇 (30)'''

    welcome = '欢迎新 dalao\n1、请改群名片为「游戏昵称 + UID」\n2、置顶公告「本群须知」一定看一下\n3、萌新可以发 UID 互加好友\n4、禁贴仓库队伍图鉴，萌新可先文字提问后找群内 dalao 私聊贴图'

    tool_website = '指挥官！请查看\n' + \
                   '出货：http://gfdb.baka.pw/\n' + \
                   '阵型：https://ynntk4815.github.io/gf/main2.html\n' + \
                   '后勤：https://ynntk4815.github.io/gf/main.html\n' + \
                   '练级：https://jyying.cn/snqxap/calclevel.html\n' \
                   '敌方：http://underseaworld.net/gf\n' \
                   '资料库：https://gf.fws.tw/db/guns/alist'

    tdoll_build_heavy_keyword_1 = ['重建一级', '重建一档', '重建一挡', '人形重建一级', '人形重建一档', '人形重建一挡']
    tdoll_build_heavy_keyword_2 = ['重建二级', '重建二档', '重建二挡', '人形重建二级', '人形重建二档', '人形重建二挡']
    tdoll_build_heavy_keyword_3 = ['重建三级', '重建三档', '重建三挡', '人形重建三级', '人形重建三档', '人形重建三挡']

    build_error = '指挥官！建造姿势错误，资源大破！\n请使用「来一发」加上：\n' \
                  '普建、手枪建造、冲锋枪建造\n突击步枪建造、步枪建造、机枪建造\n人形、装备重建一二三档'


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

            elif message in Kalina.tdoll_build_heavy_keyword_1:
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(KalinaUtility.get_datebase_path() + 'gf_b_c_6264_1.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：6K, 2K, 6K, 4K, 1/3' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message in Kalina.tdoll_build_heavy_keyword_2:
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_T_DOLL_CD, 600):
                    return ''
                results = Utility.load_json(KalinaUtility.get_datebase_path() + 'gf_b_c_6264_2.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n' + '使用公式：6K, 2K, 6K, 4K, 20/5' + '\n建造结果：' + data[0] + ' ' + data[1]

            elif message in Kalina.tdoll_build_heavy_keyword_3:
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
                return '@' + member.name + '\n' + Kalina.build_error
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
    def gf_random_group(bot, contact, member, message):

        """ 随机组一队 """

        result = '@' + member.name + '\n' + '指挥官！您被随机分配到的人形为：'

        dolls = random.sample(KalinaData.t_doll_name_list, 5)
        dolls.sort(key=operator.itemgetter(2), reverse=True)
        
        for d in dolls:
            result += '\n' + d[2] + '：' + d[1] + '，编号 ' + d[0]

        return result

    @staticmethod
    def gf_exp_book(bot, contact, member, message, cal_type):

        """ 计算人形 / 妖精所需经验书数量 """

        try:
            message = str(message)

            data = [KalinaData.t_doll_exp, KalinaData.t_doll_exp_oath, KalinaData.fairy_exp]
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
            for fairy in KalinaData.fairy_info:

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
                        result += '\n回避加成：' + fairy[5]
                    if fairy[6] != '0 %':
                        result += '\n护甲加成：' + fairy[6]
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
