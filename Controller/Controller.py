import threading
class Controller(threading.Thread):
    robot = None
    cuadrantA = None
    cuadrantB = None
    perception = None
    rules = None
    states = None
    state = "donde-estoy"
    action = "preguntar-cuadrante"
    perceptionAct = "A"
    complete = False

    def __init__(self, robot, perceptions, rules, states,cuadrantA, cuadrantB):
        super().__init__()
        self.robot = robot
        self.perception = perceptions
        self.rules = rules
        self.states = states
        self.cuadrantA = cuadrantA
        self.cuadrantB = cuadrantB
        self.robot.cuadrant = cuadrantA

    def run(self):
        while(True):
            self.perceptionAct = self.perception.getPerception(self.perceptionAct)
            self.state = self.updateState(self.perceptionAct)
            rule = self.rules.getRule(self.state)
            self.action = rule
            self.perceptionAct = self.task(self.action)
            print ("-----------------------------------------------------------")

    def updateState(self, perception):
        return self.states.getStates(self.state, self.action, perception)

    def task(self,action):
        print("\n I machine, response with action: "+action)
        if action == "preguntar-cuadrante":
            return self.robot.whereIam().getId()
        elif action == "preguntar-esta-limpio":
            return self.robot.analizeCudrant()
        elif action == "cambiando-cuadrante":
            cuadrante = self.robot.whereIam()
            if cuadrante.getId() == "A":
                self.robot.move(self.cuadrantB)
            else:
                self.robot.move(self.cuadrantA)
            return "termine"
        elif action == "limpiando-cuadrante-esperar":
            self.robot.clean()
            return "termine"