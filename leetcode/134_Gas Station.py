class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        # 만약 gas의 총 합이 cost의 총 합보다 작다는 것은, 어느 칸에서든 한 바퀴를 못돈다는 것이다.
        if sum(gas) < sum(cost):
            return -1

        # start는 인덱스 번호, fuel은 누적된 가스의 양
        start, fuel = 0, 0
        for i in range(len(gas)):
            # 현재 인덱스에서 다음 인덱스로 가지 못하면,
            # start를 다음 인덱스로 지정해주고 fuel은 0으로 초기화
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            # 갈 수 있는 경우, fuel에 값을 저장
            else:
                fuel += gas[i] - cost[i]

        return start