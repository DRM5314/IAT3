from RobotClean.RobotClean import RobotClean
from States.Rules import Rules
from States.Perception import Perception
from States.States import States
from Controller.Controller import Controller

machine = RobotClean()
rules = Rules()
perceptions = Perception()
states = States()
machineController = Controller(machine, perceptions, rules, states)

while(True):
    machineController.run()