import  trans_1


rating=float(input("Enter rating of the transformer:"))
pv=float(input("Enter primary voltage of the transformer:"))
sv=float(input("Enter secondary voltage of the transformer:"))
#oc test
vo=float(input("Enter open ckt voltage of the transformer:"))
io=float(input("Enter open ckt current of the transformer:"))
wo=float(input("Enter open ckt power of the transformer:"))
#sc test
vsc=float(input("Enter short ckt voltage of the transformer:"))
isc=float(input("Enter short ckt current of the transformer:"))
wsc=float(input("Enter short ckt power of the transformer:"))
pf=float(input("Enter power factor of the transformer:"))
x=float(input("Enter the value of loading transformer"))

Ro,Xo=trans_1.oc(vo,io,wo)
Rhv,Xh=trans_1.sc(vsc,isc,wsc)
eff,wcu=trans_1.eff(rating,wo,wsc,x,pf)

print(Ro,Xo)
print(Rhv,Xh)
print(eff,wcu)
