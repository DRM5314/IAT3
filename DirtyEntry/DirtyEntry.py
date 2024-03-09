import threading
import time

import keyboard
class DirtyEntry(threading.Thread):
    cuadrantA = None
    cuadrantB = None

    def __init__(self,cuadrantA,cuadrantB):
        super().__init__()
        self.cuadrantA = cuadrantA
        self.cuadrantB = cuadrantB

    def run(self):
        while True:
            a = keyboard.read_key()
            if a == "1":
                self.cuadrantA.dirtying()
                print("\n\nYou dirty: cuadrantA\n\n")
                time.sleep(3)
            elif a == "2":
                self.cuadrantB.dirtying()
                print("\n\nYou dirty: cuadrantB\n\n")
                time.sleep(3)