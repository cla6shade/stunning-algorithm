## Link
[문제링크](https://leetcode.com/problems/reverse-linked-list/)

## Topic
- Linked List

## Approach
처음에 LinkedList가 뭔지 몰라서 좀 헤맸던것 같다.
문제에서는 LinkedList가 root Node(head)를 줬는데, 루트 노드에 다른 노드들이 순차적으로 연결되어 있는 구조였다.

### 맨 처음에 생각한 방식
처음에는 Bubble sort처럼 O(N^2)로 순회를 돌면서, 안에 존재하는 원소들을 순차적으로 바꿔줄 계획이었다.
500^2==250000이라 할만 한 것처럼 보였지만, 기존에 알던 list와는 다른 구조라서 생각해내기가 어려웠다.

그래서 좀 오랫동안 고민하다가 답지를 살짝 봤는데, 처음에는 답조차 이해가 안됐다.
답에서는 prev를 None으로 초기화하고 current를 head로 초기화한 후,
while문으로 current와 prev를 갱신한다는 아이디어만 얻어서 풀이했다.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        newln = None
        while current:
            newln = ListNode(current.val, newln)
            current = current.next
            print(newln.val)
        return newln
```
내가 풀이한 방식은 newln을 next로 갖는 새로운 ListNode를 만드는 방식이었다.
while루프에서 newln과 current를 업데이트하는 아이디어 자체는 답지와 동일했지만,

새로운 ListNode를 만들어서 초기화하지 않더라도 head의 데이터를 그대로 이용하여 뒤집을 수도 있었다.

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = None
        prev = None
        while head:
            current = head.next
            head.next = prev
            prev = head
            head = current
        return prev
```
1. head와 next의 연결을 끊어서 current에 저장.(current는 temp변수처럼 사용) (current: 2->3>...)
2. head.next = prev로 head가 prev값을 나타내도록 지정 (head->None). 다음 루프에서는 (head2->head->None)
3. 아까 current에 저장한 head.next를 head로 업데이트 (head: 2->3->4->5)
4. 업데이트된 head에 대해 다음 루프 반복


## Note
일단 연결을 끊고 이전의 것과 연결한다는 점이 신박했다. 처음에는 이해가 안 됐는데 연결을 끊고 이전 것과 연결한다는 것에 초점을 맞추면
조금 더 이해가 쉬웠던것 같다. 다음에 할 때 할 수 있을지 잘 모르겠다..