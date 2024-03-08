class Rules:
    rules = {
        "analizando-a1": "mover-a1",
        "analizando-a2": "mover-a2",
        "limpiando-a1": "limpiar-a1",
        "limpiando-a2": "limpiar-a2",
    }

    def getRule(self,code):
        print("\n Get rule with: ")
        print("Action: "+code)
        try:
            return self.rules[code]
        except KeyError:
            print("Action: " + code,end="")
            print("Not exist!")
            return code