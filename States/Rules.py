class Rules:
    rules = {
        "donde-estoy": "preguntar-cuadrante",
        "esta-limpio": "preguntar-esta-limpio",
        "mover": "cambiando-cuadrante",
        "limpiar": "limpiando-cuadrante-esperar"
    }

    def getRule(self, code):
        #print("\n Get rule with: ")
        #print("Action: "+code)
        try:
            return self.rules[code]
        except KeyError:
            print("Action: " + code,end="")
            print("Not exist!")
            return code