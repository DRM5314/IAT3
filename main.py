from RobotClean.RobotClean import RobotClean
from States.Rules import Rules
from States.Perception import Perception
from States.States import States
from Controller.Controller import Controller
from Cuadrant.Cuadrant import Cuadrant
from DirtyEntry.DirtyEntry import DirtyEntry
machine = RobotClean()

rules = Rules()
perceptions = Perception()
states = States()
cuadrantA = Cuadrant("A")
cuadrantB = Cuadrant("B")

dirtyEntry = DirtyEntry(cuadrantA,cuadrantB)
machineController = Controller(machine, perceptions, rules, states, cuadrantA, cuadrantB)

dirtyEntry.start()
machineController.start()
