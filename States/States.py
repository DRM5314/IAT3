class States:
    states = {
        ("donde-estoy", "preguntar-cuadrante", "A"): "esta-limpio",
        ("donde-estoy", "preguntar-cuadrante", "B"): "esta-limpio",
        ("esta-limpio", "preguntar-esta-limpio", "sucio"): "limpiar",
        ("esta-limpio", "preguntar-esta-limpio", "limpio"): "mover",
        ("limpiar", "limpiando-cuadrante-esperar", "termine"): "mover",
        ("mover", "cambiando-cuadrante", "termine"): "donde-estoy",
    }

    def getStates(self, state, action, perception):
        #print("\n Get state with:")
        #print("State: "+state)
        #print("Action: "+action)
        #print("Perception: "+perception)
        try:
            return self.states[(state,action,perception)]
        except KeyError:
            print("I dont have this state, i get default: donde-estoy")
            return "donde-estoy"