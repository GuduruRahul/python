#CALCULATE THE AVERAGE MARKS OF THE LAST SEM
print("Enter all your marks out of 100")
a=int(input("Enter the marks of mca:"))
b=int(input("Enter the marks of lcs:"))
c=int(input("Enter the marks of qalr:"))
d=int(input("Enter the marks of em-2:"))
e=int(input("Enter the marks of AIEE:"))
sum=a+b+c+d+e
m=(sum)//5
print("Avg of your marks is:",m )
print("percentage of your marks is:",m,"%" )
print("CGPA of your marks is:",m/10 )
