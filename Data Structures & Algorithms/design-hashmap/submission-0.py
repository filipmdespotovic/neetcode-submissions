class MyClass:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.sledeci = None

class MyHashMap:

    def __init__(self):
        self.glava: MyClass | None = None

    def put(self, key: int, value: int) -> None:
        novi = MyClass(key, value)
        if self.glava is None:
            self.glava = novi            
            return
        
        tmp = self.glava
        while tmp is not None:
            if tmp.key == key:
                tmp.value = value
                return
            pret = tmp
            tmp = tmp.sledeci
        pret.sledeci = novi
        
    def get(self, key: int) -> int:
        tmp = self.glava
        while tmp is not None:
            if tmp.key == key:
                return tmp.value
                
            tmp = tmp.sledeci
        return -1
    
    def remove(self, key: int) -> None:
        if self.glava is None:
            return
            
        if self.glava.key == key:
            self.glava = self.glava.sledeci            
            return
        
        tmp = self.glava
        
        while tmp.sledeci is not None:
            if tmp.sledeci.key == key:                
                tmp.sledeci = tmp.sledeci.sledeci
                return
                        
            tmp = tmp.sledeci


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)