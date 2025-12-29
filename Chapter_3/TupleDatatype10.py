tpl = (10,"Rs",[10,17,15],[56,78,64],"OUCET")
print(tpl,type(tpl))

for val in tpl:
    print(val,type(val),type(tpl))

tpl[2].sort()
print(tpl,type(tpl))

tpl[-2].sort(reverse=True)
print(tpl,type(tpl))

tpl[-2].append(58)
print(tpl,type(tpl))


tpl[2].remove(15)
print(tpl,type(tpl))


del tpl[-2][1:3]
print(tpl,type(tpl))


del tpl[-2][::]
print(tpl,type(tpl))



tpl[-3].clear()
print(tpl,type(tpl))