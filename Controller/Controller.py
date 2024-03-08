class Controller:
    robot = None
    perception = None
    rules = None
    states = None
    state = "analizando-a1"
    action = "mover-a1"

    def __init__(self,robot,perceptions,rules,states):
        self.robot = robot
        self.perception = perceptions
        self.rules = rules
        self.states = states

    def run(self):
        self.perception.showPerception()
        perception = input(" Enter a perception: ")
        perception = self.perception.getPerception(perception)

        self.state = self.updateState(perception)
        rule = self.rules.getRule(self.state)
        self.action = rule
        self.task(self.action)

    def updateState(self, perception):
        return self.states.getStates(self.state, self.action, perception)

    def task(self,action):
        print("\n I machine, response with action: "+action)
        if (action in ("mover-a1","mover-a2")):
            self.robot.move(action)
        elif (action in ("limpiar-a1","limpiar-a2")):
            self.robot.clean(action)