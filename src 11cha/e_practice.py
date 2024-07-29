import sys

print(sys.argv)

gene: str = sys.argv[1]
"""1번 인덱스의 무언가를 입력받음, 0번은 이 파일,
뒤에 입력하는거 부터 리스트로 들어감
python e_practice.py MEN1 AAA BBB CC
>>> [e_practice, MEN1, AAA, BBB, CC] 가 리스트가 됨
"""
print(f"GENE: {gene}")
