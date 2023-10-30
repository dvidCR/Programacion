class calculadora:
    
    def __init__(self, expresion):
        self.expresion = expresion
        
    def calcular (self):
        self.desglosarExpresion()
        if (self.operador == "+"):
            return int(self.ope1) + int(self.ope2)
        
        if (self.operador == "-"):
            return int(self.ope1) - int(self.ope2)
        
        if (self.operador == "*"):
            return int(self.ope1) * int(self.ope2)
        
        if (self.operador == "/"):
            return int(self.ope1) / int(self.ope2)
    
    def desglosarExpresion (self):
        self.ope1 = ""
        self.operador = ""
        self.ope2 = ""
        estoyEnELOperador1 = True
        for caracter in self.expresion:
            if (caracter == "+") or (caracter == "-") or (caracter == "*") or (caracter == "/"):
                self.operador = caracter
                estoyEnELOperador1 = False
            else: 
                if estoyEnELOperador1 == True:
                    self.ope1 = self.ope1 + caracter
                else:
                    self.ope2 = self.ope2 + caracter
 
print (calculadora (input("Escribe la expresión a calcular:")).calcular())   