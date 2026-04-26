class cvor:
        def __init__(self, vrednost):
            self.vrednost = vrednost
            self.sledeci = None

class MyHashSet:
    def __init__(self):
        self.glava = None

    def add(self, key: int) -> None:
        novi_cvor = cvor(key)
        if self.glava is None:
             self.glava = novi_cvor
             return
        
        tmp = self.glava

        while tmp.sledeci is not None:
             if tmp.vrednost == novi_cvor.vrednost:
                  return
             tmp = tmp.sledeci
        if tmp.vrednost == novi_cvor.vrednost:
             return
        tmp.sledeci = novi_cvor

    def remove(self, key: int) -> None:
        if self.glava is None:
             return
        if self.glava.vrednost == key:
             self.glava = self.glava.sledeci
             return
        
        tmp = self.glava

        while tmp is not None:
            if tmp.sledeci is not None:
                if tmp.sledeci.vrednost == key:
                     p = tmp.sledeci
                     tmp.sledeci = tmp.sledeci.sledeci
                     del p
                     return
            tmp = tmp.sledeci

    def contains(self, key: int) -> bool:
        tmp = self.glava
        
        while tmp is not None:
             if tmp.vrednost == key:
                  return True
             tmp = tmp.sledeci
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
