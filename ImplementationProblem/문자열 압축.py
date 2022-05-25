def solution(s):
    answer = int(1e9)
    l = len(s)
    a = l // 2
    if l == 1:
        return 1

    for i in range(1, a+1):
        arr = []
        count = 0
        result_str = ''
        previous = ''
        for j in range(0, l, i):
            arr.append(s[j:j+i])


        for x in arr:
            if previous == '':
                previous = x
                count += 1
                continue
            if previous == x:
                count += 1
            else:
                result_str += str(count) + previous if count > 1 else previous
                count = 1
                previous = x
        result_str += str(count) + previous if count > 1 else previous

        answer = min(answer, len(result_str))

    return answer