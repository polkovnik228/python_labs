from typing import Any, Iterator, Optional


class Node:

    __slots__ = ("value", "next")

    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class SinglyLinkedList:
    """Односвязный список.

    Методы:
        append(value)       — O(1)
        prepend(value)      — O(1)
        insert(idx, value)  — O(n)
        remove(value)       — O(n)
        __iter__(), __len__(), __repr__()
    """

    __slots__ = ("head", "tail", "_size")

    def __init__(self, iterable=None) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
        if iterable:
            for v in iterable:
                self.append(v)

    def append(self, value: Any) -> None:
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self._size += 1

    def prepend(self, value: Any) -> None:
        node = Node(value, next=self.head)
        self.head = node
        if self._size == 0:
            self.tail = node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return

        prev = self.head
        for _ in range(idx - 1):
            assert prev is not None
            prev = prev.next
        node = Node(value, next=prev.next)
        prev.next = node
        self._size += 1

    def remove(self, value: Any) -> None:
        prev: Optional[Node] = None
        cur = self.head
        while cur:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                self._size -= 1
                return
            prev, cur = cur, cur.next
        raise ValueError

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(repr(x) for x in self)}])"

if __name__ == "__main__":
    sll = SinglyLinkedList()
    print(f"Длина нашего односвязного списка: {len(sll)}")

    sll.append(1)
    sll.append(2)
    sll.prepend(0)
    print(f"Наша нынешняя длина списка после добавления элементов: {len(sll)}")
    print(f"Односвязанный список: {list(sll)}")

    sll.insert(1, 0.5)
    print(f"Длина списка после добавления на индекс 1 числа 0.5: {len(sll)}")
    print(f"Односвязанный список: {list(sll)}")

    sll.append(3)
    print(f"Односвязанный список после добавления числа в конец: {list(sll)}")

    print("Красивый вывод списка через __repr__:")
    print(sll)
