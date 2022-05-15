# 답지
import heapq
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 K가 큰 경우
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    print(q)

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        print("sum_value : " + str(sum_value) + " q[0][0] : " + str(q[0][0]) + " previous : " + str(previous) + " length : " + str(length))
        now = heapq.heappop(q)[0]
        print("now : " + str(now))
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정


    result = sorted(q, key=lambda x: x[1])
    print("result : ", end='')
    print(result)

    print(result[(k-sum_value) % length][1])
    return result[(k-sum_value) % length][1]


food_times = [4,2,3,6,7,1,5,8]
k = 27
solution(food_times, k)
# k = 3

