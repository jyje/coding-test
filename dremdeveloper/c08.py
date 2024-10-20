# 열린 괄호는 자신과 가장 가까운 닫힌 괄호를 만나면 상쇄된다.
# 상쇄 조건은 열린 괄호가 먼저 와야하고,
# 열린 괄호와 닫힌 괄호 사이에 아무것도 없어야 한다.
# 더 상쇄할 괄호가 없다면 참, 아니라면 거짓을 반환한다.

from collections import deque

def solution_1(s: str) -> bool:
    if s == "":
        return False

    data = list(s)

    stack = deque()
    for i,w in enumerate(s):
        if w == "(":
            stack.append(i)

    while len(stack) != 0:
        index_open = stack.pop()
        
        if index_open+1 == len(data) or data[index_open+1] != ")":
            return False

        del data[index_open]
        del data[index_open]

    return True

def solution(s: str) -> bool:
    if s == "":
        return False

    stack = deque()

    for w in s:
        if w == "(":
            stack.append(w)
        elif w == ")":
            if not stack or stack.pop() != "(":
                return False
        else:
            return False

    return len(stack) == 0

if __name__ == "__main__":
    assert solution("(())()") == True
    assert solution("((())()") == False
    assert solution("()()") == True
    assert solution("") == False
    assert solution("(1)") == False
    assert solution(")(") == False
