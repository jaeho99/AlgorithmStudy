from sort.insertionSort import ListNode

a = b = ListNode("영번째", ListNode("두번쨰"))

print(a.val)  #  같은 값이 나온다.
print(b.val)  #

a.val = "첫번째"   # a 만 변경 시킨다.

print(a.val)  #  값이 같이 변하기에
print(b.val)  #  같은 객체를 바라 보는 것을 알 수 있다.

a = a.next  # a의 바라보는곳 (포인터)를 변경

print(f"a는 next를 바라보기에 : {a.val}")
print(f"b는 포인터가 변경되지 않았기에 : {a.val}")

b.val = "나무"  # a의 바라보는곳 (포인터)를 변경어학

print(f"a는 next를 바라보기에 : {a.val}")
print(f"b는 포인터가 변경되지 않았기에 : {a.val}")

a = b

print(f"같은 곳(포인터)을 바라봄 : {a.val}")
print(f"같은 곳(포인터)을 바라봄 : {b.val}")