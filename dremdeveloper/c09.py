# 10진수를 2진수로 변환하는 함수를 작성하라

from collections import deque

def solution(input: int) -> str:
    remain = input
    stack = deque()

    while remain > 0:
        stack.append(str(remain % 2))
        remain //= 2
    stack.reverse()

    return "".join(stack)

if __name__ == "__main__":
    assert solution(10) == "1010"
    assert solution(27) == "11011"
    assert solution(12345) == "11000000111001"
