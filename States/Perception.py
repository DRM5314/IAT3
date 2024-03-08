class Perception:
    perception = {
        "limpio":"limpio",
        "sucio":"sucio",
    }

    def getPerception(self,perception):
        try:
            return self.perception[perception]
        except KeyError:
            print("\n Perception input not valid!")
            return "limpio"

    def showPerception(self):
        print("\n Perceptions available: limpio, sucio")