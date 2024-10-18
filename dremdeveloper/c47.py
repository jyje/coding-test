# 정수 N을 입력받아 1부터 N까지의 숫자 중에서 합이 10이 되는 조합을 리스트로 반환하는 solution 함수를 작성하라.
# 출력 배열의 모든 요소는 오름차순으로 정렬.
# 같은 숫자는 한 번만 선택할 수 있다.
# N은 1이상 10이하의 정수.

TARGET = 10

def search(sum, start, answer, visited, N):
    if sum == TARGET:
        answer.append(visited)
        return
    
    for next in range(start, N+1):
        if sum + next <= TARGET:
            search(sum + next, next+1, answer, visited + [next], N)


def solution(N: int):
    assert 1 <= N <= TARGET
    answer = []
    search(0, 1, answer, [], N)
    print(f"{N}: {answer}")
    return answer
    

if __name__ == "__main__":
    assert solution(2) == []
    assert solution(4) == [[1,2,3,4]]
    assert solution(5) == [[1,2,3,4],[1,4,5],[2,3,5]]
    assert solution(7) == [[1,2,3,4],[1,2,7],[1,3,6],[1,4,5],[2,3,5],[3,7],[4,6]]
