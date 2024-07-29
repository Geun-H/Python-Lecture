import sys


# 함수 1 예제
def run_pipeline_1():
    print("Analysis1")


# 함수 2 예제
def run_pipeline_2():
    return "Analysis2"


# 함수 3 예제
def run_pipeline_3(num1, num2) -> None:
    print(f"Analysis3 :: {num1 + num2}")


# 함수 4 예제, 아래처럼 타입 및 설명을 적어주는 것이 좋다
def run_pipeline_4(num1: int, num2: int) -> str:
    """Add given two numbers and return result.

    Args:
        num1 (int): input number 1
        num2 (int): input number 2

    Returns:
        int: sum result of num1 and num2

    Example:
        >>> run_pipelin_4(2,3)
        5
    """
    return f"Analysis4 :: {num1+num2}"


run_pipeline_1()

ret = run_pipeline_2()
print(ret)

run_pipeline_3(2, 3)

ret4 = run_pipeline_4(2, 3)
print(ret4)
