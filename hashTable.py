import collections
import sys
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    # 초기화
    def __init__(self):
        self.size = 10
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value : int) -> None:
        index = key % self.size

        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None :
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next





if __name__ == '__main__':
    # m, n = 16, 4
    # input = "noj.am IU\nacmicpc.net UAENA\nstartlink.io THEKINGOD\ngoogle.com ZEZE\nnate.com VOICEMAIL\nnaver.com REDQUEEN\ndaum.net MODERNTIMES\nutube.com BLACKOUT\nzum.com LASTFANTASY\ndreamwiz.com RAINDROP\nhanyang.ac.kr SOMEDAY\ndhlottery.co.kr BOO\nduksoo.hs.kr HAVANA\nhanyang-u.ms.kr OBLIVIATE\nyd.es.kr LOVEATTACK\nmcc.hanyang.ac.kr ADREAMER\nstartlink.io\nacmicpc.net\nnoj.am\nmcc.hanyang.ac.kr"
    # inputlen = input.split("\n")
    mh = MyHashMap()
    #
    mh.put(10, 15)
    mh.put(100, 30)
    print(mh.table[0].next.value)
    # print(mh.get(3).next)
    # mh.remove(3)
    # print(mh.get(3))



    #
    # for b in inputlen:
    #     a = b.split(" ")
    #     if len(a) == 2:
    #         mh.put(19, a[1])
    # input = sys.stdin.readline
    # N, M = map(int, input().split())
    # add = {}
    # for _ in range(N):
    #     site, ps = input().split()
    #     add[site] = ps
    #     print(site)
    #     print(ps)
    # for _ in range(M):
    #     print(add[input().rstrip()])
    # A, B = map(int, input().split())
    # print(A)
    # print(type(A))
    # a, b = map(int, input().split())
    # print(a+b)
