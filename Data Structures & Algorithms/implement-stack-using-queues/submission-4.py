class Node:
    def __init__(self, x: int):
        self.podatak = x
        self.sledeci = None

class MyStack:

    def __init__(self):
        self.glava = None

    def push(self, x: int) -> None:
        if self.glava is None:
            self.glava = Node(x)
        else:
            tmp = self.glava
            while tmp.sledeci is not None:
                tmp = tmp.sledeci
            tmp.sledeci = Node(x)

    def pop(self) -> int:
        if self.glava.sledeci is None:
            x = self.glava.podatak
            self.glava = None
            return x
        tmp = self.glava.sledeci
        pret = self.glava
        while tmp.sledeci is not None:
            pret = tmp
            tmp = tmp.sledeci
        pret.sledeci = None
        x = tmp.podatak
        del(tmp)
        return x

    def top(self) -> int:
        tmp = self.glava
        while tmp.sledeci is not None:
            tmp = tmp.sledeci
        return tmp.podatak

    def empty(self) -> bool:
        if self.glava is None:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()