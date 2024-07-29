import argparse  # 아그파스 가져오기
import sys

parser = argparse.ArgumentParser()  # class에 지정
parser.add_argument("--gene1", required=True, type=str)
parser.add_argument("--gene2", required=True)
# 입력할 때 꼭 --gene1 을 입력받아야함
# 타입을 정해도 됨

args = parser.parse_args()  # 실행하겠다.
print(f"Gene1: {args.gene1}")
print(f"Gene2: {args.gene2}")

# python g_practice.py --gene1 AAA --gene2 BBBB
