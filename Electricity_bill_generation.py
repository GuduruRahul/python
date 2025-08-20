#to import time & date

# from pytz import timezone
# from datetime import datetime
# ind_time =datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')




EC=0
FC=0
CC=0
PU1=0
u=float(input("enter yur units="))
EDC=0.06*u

def res(PU,CU):

#if LT=="LT1(A)":
  if u<=100:
      if u<=50:
       FC=10
       CC=40
       #PU1=PU*1.95
       EC=u*1.95
       EDC=0.06*u
       total_bill=FC+CC+EC+EDC
  elif 50<u<=100:
       FC=10
       CC=70
       #PU1=(50*1.95)+(PU-50)*3.1
       EC=(50*1.95)+(u-50)*3.1
       EDC=0.06*u
       total_bill=FC+CC+EC+EDC
return FC,CC,EC,EDC,total_bill

#elif LT=="LT1(B)i":
      if u<=100:
        CC=90
        FC=10
        EC=u*3.4
        #PU1=PU*3.4
        EDC=0.06*u
        total_bill=FC+CC+EC+EDC
        return FC,CC,EC,EDC,total_bill
      elif 100<u<=200:
              CC=90
              FC=10
              EC=(100*3.4)+(u-100)*4.80
              #PU1=(100*3.4)+(PU-100)*4.80
              EDC=0.06*u
              total_bill=FC+CC+EC+EDC
      return FC,CC,EC,EDC,total_bill


  else:
    print("Application Not supported")
def com(PU,CU):
   #if LT=="LT2(A)":
     if u<=50:
      CC=50
      FC=60
      EC=u*7.00
      #PU1=PU*7.00
      EDC=0.06*u
      total_bill=FC+CC+EC+EDC
      return FC,CC,EC,EDC,total_bill
     if u<=100:
      CC=90
      FC=70
      EC=u*8.500
      #PU1=PU*7.00
      EDC=0.06*u
      total_bill=FC+CC+EC+EDC
      return FC,CC,EC,EDC,total_bill
     if 100<u<=300:
      CC=105
      FC=70
      EC=100*8.50+(u-100)*9.90
      #PU1=PU*7.00
      EDC=0.06*u
      total_bill=FC+CC+EC+EDC
      return FC,CC,EC,EDC,total_bill
     if 300<u<=500:
      CC=120
      FC=70
      EC=300*9.90+(u-300)*10.40
      #PU1=PU*7.00
      EDC=0.06*u
      total_bill=FC+CC+EC+EDC
      return FC,CC,EC,EDC,total_bill
     if u>500:
      CC=160
      FC=70
      EC=500*10.40+(u-500)*11
      #PU1=PU*7.00
      EDC=0.06*u
      total_bill=FC+CC+EC+EDC
      return FC,CC,EC,EDC,total_bill
def adv(PU,CU):
  if u==0:   # elif LT=="LT(2C)":
    FC=160
    CC=70
    #PU1=PU*1.95
    EC=u*13
    EDC=0.06*u
    total_bill=FC+CC+EC+EDC
return FC,CC,EC,EDC,total_bill






print("===============================================")
