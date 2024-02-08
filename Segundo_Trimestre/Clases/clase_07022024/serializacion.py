import pickle as pickle

class simple:
    
    def __init__(self, valor):
        self.valor = valor
        
    def equals(self, obj):
        return self.valor == obj.valor
    
s = simple(7)
if (s.__eq__):
    print(pickle.dumps(s))
    pickle.dump(s, open("simple1.pkl", "wb"))
    
    print(pickle.dumps(s, protocol=pickle.HIGHEST_PROTOCOL))
    pickle.dump(s, open("simple2.pkl", "wb"), protocol=pickle.HIGHEST_PROTOCOL)
    
x = pickle.load(open("simple1.pkl", "rb"))
print(x.valor)