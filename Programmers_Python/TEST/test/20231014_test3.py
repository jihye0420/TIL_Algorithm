from collections import deque

def solution(N, simulation_data):
    sum_val = 0
    q = deque()

    index = 0
    curTime = 0

    while index < len(simulation_data):
        if not q and curTime == simulation_data[index][0]:
            q.append(simulation_data[index][1] - 1)
            index += 1
            curTime += 1
            continue

        length = len(q)
        for s in range(length):
            temp = q.popleft()
            if temp == 0:  # 고객이 나감
                if curTime >= simulation_data[index][0]:
                    sum_val += curTime - simulation_data[index][0]
                    q.append(simulation_data[index][1] - 1)
                    index += 1
                    if index == len(simulation_data):
                        return sum_val
                continue
            q.append(temp - 1)

        if length < N and curTime >= simulation_data[index][0]:
            sum_val += curTime - simulation_data[index][0]
            q.append(simulation_data[index][1] - 1)
            index += 1

        curTime += 1

    return sum_val


if __name__ == '__main__':
    print(solution(2, [[0, 3], [2, 5], [4, 2], [5, 3]]))
