import json

class simple:
    
    def __init__(self, valor):
        self.valor = valor
        
    def equals(self, obj):
        return self.valor == obj.valor
    
class Traductor(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, simple):
                return obj.__dict__  # Serialize Simple objects as their dictionary representation
            return json.JSONEncoder.default(self, obj)
    
s = simple(7)
print(json.dumps(s, cls=Traductor))