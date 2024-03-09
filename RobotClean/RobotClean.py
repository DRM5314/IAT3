import time


class RobotClean:
    cuadrant = None
    def move(self,cuadrant):
        print("\n Moving... wait 1 second")
        time.sleep(1)
        self.cuadrant = cuadrant
        print(" I move to: "+self.cuadrant.getId()+"!")
        time.sleep(5)

    def clean(self):
        print("\n Cleaning...  wait 3 seconds!")
        time.sleep(3)
        self.cuadrant.clean()
        print(" Floor clean! ")
        time.sleep(5)

    def analizeCudrant(self):
        print("\nAnalize please wait!!!")
        time.sleep(2)
        print("This cuadrant is dirty?: "+self.cuadrant.getDirty())
        time.sleep(5)
        return self.cuadrant.getDirty()


    def whereIam(self):
        print("\nI am in cuadrant: "+self.cuadrant.getId())
        return self.cuadrant

    def notDoingAnything(self):
        print("\n Im not doing anything...'")

    def setCuadrant(self,cuadrant):
        self.cuadrant = cuadrant