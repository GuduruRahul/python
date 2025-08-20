#to import time & date

from pytz import timezone
from datetime import datetime
ind_time =datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')


cat=input("select your Catogory(residential/commercial):").lower()
units=0
units=int(input("Enter your units consumed:"))


bill=0
FC=0
CC=0
PU1=0
EDC=0.06*units

if cat=="residential":
  LT=input("select your load type(LT1(A)/LT1(B)i):").upper()
  PU=float(input("Enter your previous units consumed:"))

  if LT=="LT1(A)":
    if units<=100:
      if units<=50:
       FC=10
       CC=40
       PU1=PU*1.95
       bill=units*1.95
      elif 50<units<=100:
       FC=10
       CC=70
       PU1=(50*1.95)+(PU-50)*3.1
       bill=(50*1.95)+(units-50)*3.1


  elif LT=="LT1(B)i":
      if units<=100:
        CC=90
        FC=10
        bill=units*3.4
        PU1=PU*3.4
      elif 100<units<=200:
              CC=90
              FC=10
              bill=(100*3.4)+(units-100)*4.80
              PU1=(100*3.4)+(PU-100)*4.80

  else:
    print("Application Not supported")



elif cat=="commercial":
  LT=input("select your load type(LT2(A) / LT(2C)):").upper()
  PU=int(input("Enter your previous units consumed:"))
  if LT=="LT2(A)":
     if units<=50:
      CC=50
      FC=60
      bill=units*7.00
      PU1=PU*7.00


  elif LT=="LT(2C)":
    CC=160
    FC=70
    bill=units*13
    PU1=PU*13


  else:
    print("Application Not supported")

else:
  print("Application Not supported")

print("===============================================")
print("TGNPDCL")
print("DATE & TIME:",ind_time)
print("===============================================")

if PU==0:
 print(
    f"Present KWH: {PU+units}\n"
    f"Previous KWH: {PU}\n"
    f"Units Consumed: {units}\n"
    f"Energy Charges: {bill}\n"
    f"Fixed Charges: {FC}\n"
    f"Customer Charges:{CC}\n"
    f"Electricity Duty Charges: {EDC}\n"
    f"Bill Amount: {bill+FC+CC+EDC}"
)



elif PU>0:
  print(
    f"Present KWH: {PU+units}\n"
    f"Previous KWH: {PU}\n"
    f"Units Consumed: {units}\n"
    f"Energy Charges: {bill}\n"
    f"Fixed Charges: {FC}\n"
    f"Customer Charges:{CC}\n"
    f"Electricity Duty Charges: {EDC}\n"
    f"Bill Amount: {bill+FC+CC+EDC}"
)


print("===============================================")









