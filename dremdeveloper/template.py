# DESCRIPTION

def solution(b: bool) -> bool:
    return ~b

if __name__ == "__main__":
    assert solution(True) == False
    assert solution(False) == True
