def isPossible(answer):
    for i in answer:
        x, y, a = i
        if a == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        else:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False

    return True

def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:  # 설치
            answer.append([x,y,a])
            if not isPossible(answer):
                answer.remove([x,y,a])

        else:  # 삭제
            answer.remove([x, y, a])
            if not isPossible(answer):
                answer.append([x, y, a])
    print(sorted(answer))
    return answer

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

solution(n, build_frame)