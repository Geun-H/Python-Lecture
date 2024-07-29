import sys


def run_pipeline_1():
    print("Analysis1")


run_pipeline_1()


def run_pipeline_2():
    return "Analysis2"


ret = run_pipeline_2()
print(ret)


def run_pipeline_3(num1, num2):
    print(num1 + num2)


run_pipeline_3(2, 3)
