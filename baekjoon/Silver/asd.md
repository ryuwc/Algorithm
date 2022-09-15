# N과 M (1)

---

### 재귀 , 백트래킹

- ans에는 stack처럼 for문을 사용해 값을 넣어준다.

- 넣어주고, 재귀를 돌린다.

- depth가 m과 같아질 때 리턴을 건다.

- 리턴이 되면, pop()이 실행되어 ans의 맨 뒤의 요소가 빠진다.

- 또한, for문이 끝나도, pop()이 실행된다. 이때, i는 맨 처음 넣어논 1이 된다.

- 그 다음은 2가 쌓일 것이다.

- for문안에 for문이 돌아가는 구조로 복잡하다.

---

### 

### 트리로 표현

- 재귀를 구현하기 전 트리의 형태로 작성하여 코드를 짜본다.

- 이 경우, N이 3이고, M도 3일 때, 아래 그림과 같이 순회한다.

![이미지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcJmTRj%2FbtrMd2K609V%2F8PKdv8gk1NITGv2dbcul00%2Fimg.jpg)

- 리턴(pop)이 돌며, 다음 숫자로 계속 순회한다.


