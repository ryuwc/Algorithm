import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        # {*ot:[hot, dot], h*t:[hot, hit]....}
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        Q = collections.deque([beginWord])
        rst = 1
        # BFS탐색
        while Q:
            for i in range(len(Q)):
                word = Q.popleft()
                # Q에서 pop한 단어가 endword와 같으면 rst return
                if word == endWord:
                    return rst
                # word를 다시 *을 포함한 패턴으로 바꿔주고 nei딕셔너리에서 탐색
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neiWord in nei[pattern]:
                        # 같은 패턴의 단어가 있고, 아직 방문 안했다면 Q에 추가
                        if neiWord not in visit:
                            visit.add(neiWord)
                            Q.append(neiWord)
            rst += 1
        return 0
