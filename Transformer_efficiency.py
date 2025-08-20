
#to estimate highest efficiency on different loads


x=float(input("enter the loading of transformer:"))

#taking input from user for transformerA
kvaA=int(input("enter VA rating of transformer A:"))
wiA=int(input("enter wi of transformer A:"))
wcuflA=int(input("enter wcufl of transformer A:"))
pfA=float(input("enter pf of transformer A:"))

#taking input from user for transformerB
kvaB=int(input("enter VA rating of transformer B:"))
wiB=int(input("enter wi of transformer B:"))
wcuflB=int(input("enter wcufl of transformer B:"))
pfB=float(input("enter pf of transformer B:"))

#taking input from user for transformerC
kvaC=int(input("enter VA rating of transformer C:"))
wiC=int(input("enter wi of transformer C:"))
wcuflC=int(input("enter wcufl of transformer C:"))
pfC=float(input("enter pf of transformer C:"))

#maximum efficiency

kmaxA=(wiA/wcuflA)**0.5
kmaxB=(wiB/wcuflB)**0.5
kmaxC=(wiC/wcuflC)**0.5

print("maximum efficiency of transformer A is:",kmaxA)
print("maximum efficiency of transformer B is:",kmaxB)
print("maximum efficiency of transformer C is:",kmaxC)

#EFFICIENCY CALCULATION

effA=(x*kvaA*pfA)*100/((x*kvaA*pfA)+wiA+(wcuflA*x*x))
effB=(x*kvaB*pfB)*100/((x*kvaB*pfB)+wiB+(wcuflB*x*x))
effC=(x*kvaC*pfC)*100/((x*kvaC*pfC)+wiC+(wcuflC*x*x))



#calulationg the copper losses at x -load of transformer
wcuA=(x*x*wcuflA)
wcuB=(x*x*wcuflB)
wcuC=(x*x*wcuflC)

print("1--Expected output")
print(f"Rating of transformer A= {kvaA} Watts")
print(f"core losses of Transformer A= {wiA} Watts")
print(f"Loading Transformer={x}")
print(f"copper losses of Transformer A= {wcuflA} Watts")
print(f"Efficiency of transformer A={effA} %")

print(f"Rating of transformer B= {kvaB} Watts")
print(f"core losses of Transformer B= {wiB} Watts")
print(f"Loading Transformer={x}")
print(f"copper losses of Transformer B= {wcuflB} Watts")
print(f"Efficiency of transformer B={effB} %")

print(f"Rating of transformer C= {kvaC}")
print(f"core losses of Transformer C= {wiC} Watts")
print(f"Loading Transformer={x}")
print(f"copper losses of Transformer C= {wcuflC} Watts")
print(f"Efficiency of transformer C={effC} %")


print("TABLE--2 CALULATIONS")
#printing the efficiency of each transformer
print("the efficiency of transformer A is:",effA)
print("the efficiency of transformer B is:",effB)
print("the efficiency of transformer C is:",effC)

#printing the copper losses at x -load of transformer
print("the copper losses at x-load of transformer A is:",wcuA)
print("the copper losses at x-load of transformer B is:",wcuB)
print("the copper losses at x-load of transformer C is:",wcuC)


print(f"the highest efficiency is {max(effA,effB,effC)}")
