import json
import statistics

with open("test1.json") as handle:
    data = json.load(handle)

# print(data)
# print(type(data))

for elem in data:
    print(elem["GENE"])
# 리스트에 딕셔너리가 있는거라 GENE만 꺼낼 수 있음

""" 직접 평균 구하기
s_sum = 0.0
for elem in data:
    s_sum += float(elem["VALUE"])
print(s_sum / len(data))
"""

# 내장함수 임포트해서 statistics 사용하여 구하기
values = []
for elem in data:
    values.append(float(elem["VALUE"]))

print(values)
print(f"mean: {statistics.mean(values)}")
print(f"stdev: {statistics.stdev(values)}")
