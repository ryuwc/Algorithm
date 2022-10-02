import heapq

class Solution(object):
    def reconstructQueue(self, people):
        # people = [[사람의 키, 앞에 줄 서 있는 사람들 중 자신의 키 이상인 사람들의 수],...]
        # people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        H = []
        for person in people:
            heapq.heappush(H, (-person[0], person[1]))

        rst = []
        while H:
            person = heapq.heappop(H)
            rst.insert(person[-1], [-person[0], person[1]])

        return rst
