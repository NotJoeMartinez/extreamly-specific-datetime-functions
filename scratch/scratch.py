from inspect import getmembers, isfunction
from  import methods_31_40
foo = [o for o in getmembers(methods_31_40) if isfunction(o[1])]

print(foo)