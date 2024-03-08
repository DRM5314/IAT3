class States:
    states = {
        ("analizando-a1", "mover-a1", "limpio"): "analizando-a2",
        ("analizando-a2", "mover-a2", "limpio"): "analizando-a1",
        ("analizando-a1", "mover-a1", "sucio"): "limpiando-a1",
        ("analizando-a2", "mover-a2", "sucio"): "limpiando-a2",
        ("limpiando-a1", "limpiar-a1", "limpio"): "analizando-a2",
        ("limpiando-a2", "limpiar-a2", "limpio"): "analizando-a1",
        ("limpiando-a1", "limpiar-a1", "sucio"): "limpiando-a1",
        ("limpiando-a2", "limpiar-a2", "sucio"): "limpiando-a2",
    }

    def getStates(self, state, action, perception):
        print("\n Get state with:")
        print("State: "+state)
        print("Action: "+action)
        print("Perception: "+perception)
        try:
            return self.states[(state,action,perception)]
        except KeyError:
            print("I dont have this state, i get default: analizando-a1")
            return "analizando-a1"