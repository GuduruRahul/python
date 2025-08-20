 #OC TEST & SC TEST CALCULATRIONS
 X=float(input("Enter the fraction of load:"))
 VA=float(input("Enter the VA rating of transformer:"))
 PV=float(input("Enter the Primary voltage of transformer:"))
 SV=float(input("Enter the Secondary voltage of transformer:"))

 #oc test
 WO=float(input("Enter the oc test wattmeter reading in watts:"))
 VO=float(input("Enter the oc test voltmeter reading in volts:"))
 IO=float(input("Enter the oc test ammeter reading in amps:"))
 COS=WO/(VO*IO)
 IW=IO*COS
 IM=((IO**2)-(IW**2))**0.5
 RO=VO/IW
 XO=VO/IM




 #sc test
 WS=float(input("Enter the sc test wattmeter reading in watts:"))
 VS=float(input("Enter the sc test voltmeter reading in volts:"))
 IS=float(input("Enter the sc test ammeter reading in amps:"))
 RS=WS/(IS**2)
 ZS=VS/IS
 XS=((ZS**2)-(RS**2))**0.5

 WCU=(X**2)*WS
 EFF=(X*VA*100)/((X*VA)+WO+WCU)
 MAXEFF=(WO/WS)**0.5



#printing output
print(f'Primary Voltage={PV} V')
print(f'Secondary Voltage={SV} V')
print(f'Ro={RO} Ohms')
print(f'Xo={XO} Ohms')
print(f'Ro1={RS} Ohms')
print(f'Xo1={XS} Ohms')
print(f'core losses of Transformer={WO} Watts')
print(f'Loading Transformer={X}')
print(f'copper losses of Transformer={WCU} Watts')
print(f'Efficiency of Transformer at Loading={EFF}%')
print(f'Maximum Efficiency at Loading={MAXEFF}')
print(f'no load phase angle between V & I={COS}')
