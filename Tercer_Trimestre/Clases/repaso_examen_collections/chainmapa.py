from collections import ChainMap, defaultdict

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
di = defaultdict(int)
with open("./fichero.txt", "r") as f:
    r = f.read().split()
    for i in r:
        di[i] += 1
        
print(ChainMap(adjustments, baseline, di))

l = ChainMap(adjustments, baseline, di)

print(list(l.keys()), list(l.values()))