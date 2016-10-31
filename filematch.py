import os

somedir = '/Users/abc/lpython'

pyfiles = [name for name in os.listdir(somedir)
           if name.endswith('.py')]

print(pyfiles)
