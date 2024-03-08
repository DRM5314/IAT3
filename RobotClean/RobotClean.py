import time


class RobotClean:
    cuadrante = "A"
    def move(self,cuadrante):
        print("\n Moving... wait 1 second")
        time.sleep(1)
        self.cuadrante = cuadrante
        print(" I move to: ",self.cuadrante)

    def clean(self, cleanArea):
        print("\n Cleaning...: "+cleanArea+"  wait 3 seconds!")
        time.sleep(3)
        print(" Floor clean! ")