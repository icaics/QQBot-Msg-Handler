# -*- coding: utf-8 -*-

from Define import Utility

# 可以独立运行，用作数据校验

results = Utility.load_json('./normal_data/gf_build_6264_2.json')
sum = 0
for r in results:
    sum += float(r[2]) * 1000
print(sum)

results = Utility.load_json('./up_data/gf_build_6264_2.json')
sum = 0
for r in results:
    sum += float(r[2]) * 1000
print(sum)

results = Utility.load_json('./normal_data/gf_build_2222_2.json')
sum = 0
for r in results:
    sum += float(r[2]) * 1000
print(sum)

results = Utility.load_json('./normal_data/gf_build_2222_2.json')
sum = 0
for r in results:
    sum += float(r[2]) * 1000
print(sum)
