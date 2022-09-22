import sys; sys.stdin = open('sample_input_컨테이너.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())    # N컨테이너 개수, M트럭 개수
    container_weight = map(int, input().split())
    truck_weight = map(int, input().split())
    container_weight = sorted(container_weight, reverse=True)
    truck_weight = sorted(truck_weight, reverse=True)

    result = 0
    for i in range(M):
        for j in range(len(container_weight)):
            truck = truck_weight[i]
            container = container_weight[j]
            if truck >= container:
                result += container
                container_weight.pop(j)
                break
    print(f'#{tc+1}', result)
    # print(truck_weight)      # [8, 3]
    # print(container_weight)  # [5, 3, 1]
    # break
