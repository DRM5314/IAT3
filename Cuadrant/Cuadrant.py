class Cuadrant:
    id = "A"
    dirty = "limpio"
    def __init__(self,id):
        self.id = id

    def dirtying(self):
        self.dirty = "sucio"

    def clean(self):
        self.dirty = "limpio"

    def getId(self):
        return self.id

    def getDirty(self):
        return self.dirty