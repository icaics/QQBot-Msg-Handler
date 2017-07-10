#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Define import Global
from Define import Utility
from Define import Kalina
import KalinaCD

import time
import random
import math


class KalinaUtility:

    @staticmethod
    def kalina_can_reply(member, list_cd_counter, seconds):

        """ 判断 Kalina 是否响应当前成员消息 """

        # 遍历发言记录
        for m in list_cd_counter:
            # 获得当前成员记录
            if m['uin'] == member.uin:
                # 不在限制内
                if time.time() - m['time'] > seconds:
                    # 冷却超过 10 分钟，可以响应，更新数据
                    m['time'] = time.time()
                    return True
                # 在限制内
                return False

        # 未找到当前成员，可以响应，更新数据
        data = dict()
        data['uin'] = member.uin
        data['time'] = time.time()
        list_cd_counter.append(data)

        return True

    @staticmethod
    def gf_build(bot, contact, member, message):

        """ 少女前线 战术少女建造模拟 """

        try:
            if message == '普建':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_4442.json')
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n指挥官！建造结果如下：\n公式：430, 430, 430, 230' + '\n结果：' + data[1] + ' ' + data[0]
            elif message == '手枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_1111.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n指挥官！建造结果如下：\n公式：130, 130, 130, 130' + '\n结果：' + data[1] + ' ' + data[0]
            elif message == '冲锋枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_4412.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n指挥官！建造结果如下：\n公式：430, 430, 130, 230' + '\n结果：' + data[1] + ' ' + data[0]
            elif message == '突击步枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_1442.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n指挥官！建造结果如下：\n公式：130, 430, 430, 230' + '\n结果：' + data[1] + ' ' + data[0]
            elif message == '步枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_4142.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n指挥官！建造结果如下：\n公式：430, 130, 430, 230' + '\n结果：' + data[1] + ' ' + data[0]
            elif message == '机枪建造':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_7614.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n指挥官！建造结果如下：\n公式：730, 630, 130, 430' + '\n结果：' + data[1] + ' ' + data[0]
            elif message == '重建一级' or message == '重建一档' or message == '重建一挡':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_6264_1_3.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n指挥官！建造结果如下：\n公式：6K, 2K, 6K, 4K, 1/3' + '\n结果：' + data[1] + ' ' + data[0]
            elif message == '重建二级' or message == '重建二档' or message == '重建二挡':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_6264_20_5.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n指挥官！建造结果如下：\n公式：6K, 2K, 6K, 4K, 20/5' + '\n结果：' + data[1] + ' ' + data[0]
            elif message == '重建三级' or message == '重建三档' or message == '重建三挡':
                # 此功能需要参与发言 CD 计算
                if not KalinaUtility.kalina_can_reply(member, KalinaCD.BUILD_CD, 600):
                    return ''
                results = Utility.load_json(Global.database_path + 'gf_b_c_6264_50_10.json')
                # 建造
                data = KalinaUtility.gf_build_calculate(results)
                return '@' + member.name + '\n指挥官！建造结果如下：\n公式：6K, 2K, 6K, 4K, 50/10' + '\n结果：' + data[1] + ' ' + data[0]
            else:
                # 建造方式错误不再触发发言 CD
                return '@' + member.name + '\n' + '建造姿势错误，资源大破！\n请使用「来一发」加上：\n普建、手枪建造、冲锋枪建造\n突击步枪建造、' \
                                                  '步枪建造、机枪建造\n重建一档、重建二档、重建三档'
        except Exception as e:
            print('GF_BUILD_E: ' + str(e))
            return '@' + member.name + '\n' + message + ' 建造系统出现错误，资源大破！'

    @staticmethod
    def gf_build_calculate(results):

        """ 少女前线 战术少女建造模拟 按几率生成结果 """

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
    def gf_exp_book(bot, contact, member, message):

        """ 计算等级所需经验书数量 """

        try:
            message = str(message)

            # 如果无参数
            if len(message) == 0:
                return '@' + member.name + '\n等级参数错误，[a-b] 可计算从等级 a 到等级 b 所需的经验书数量'

            # 去掉 []
            message = message.replace('[', '')
            message = message.replace(']', '')

            # 分隔数组
            num = message.split('-')

            result = '@' + member.name + '\n等级参数错误，[a-b] 可计算从等级 a 到等级 b 所需的经验书数量'
            if len(num) == 2:

                a = int(num[0])
                b = int(num[1])

                # 排除不合法参数
                if a < 1 or b < 2 or a > 99 or b > 100 or a >= b:
                    return result

                # 计算
                exp = sum(Kalina.exp[a - 1:b - 1])
                books = math.ceil(exp / 3000)

                result = '@' + member.name + '\n' + '指挥官！' + str(a) + '-' + str(b) + ' 级共需要经验书 ' + str(books) + ' 本\n计算结果仅供参考哦'

            return result

        except Exception as e:
            print('EXP_BOOK_E:' + str(e))
            return '@' + member.name + '\n计算出现错误，[a-b] 可计算从等级 a 到等级 b 所需的经验书数量'
