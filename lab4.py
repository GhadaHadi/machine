import pandas as pd
import matplotlib.pyplot as plt

dectionary={'x':[1,2,3,4,5],
             'y':[2,4,5,4,5],
             'y^':[2.8,3.4,4,4.6,5.2]}
             

Table=pd.DataFrame(dectionary)
print(Table)

m1=Table['x'].mean()
print("mean of x is   :",m1)

m2=Table['y'].mean()
print("mean of y is   :",m2)
B1=sum((Table['x']-m1)*(Table['y']-m2))/sum((Table['x']-m1)**2)
print("value of B1 is :",B1)
B0=m2-B1*m1
print("value of B0 is :",B0)
plt.scatter(Table['x'],Table['y'])
plt.plot(Table['x'],Table['y^'])
print("_____________________________________________")
print("_____________________________________________")
g1=sum((Table['y^']-m2)**2)
g2=sum((Table['y']-m2)**2)

r2=g1/g2
print("the value of R2 is   :",r2)
print("_____________________________________________")
print("_____________________________________________")
n=len(Table['x'])
s1=sum((Table['y']-m2)**2)
s2=n-2
st=(s1/s2)*0.5
print("STANDORD OF ERROR IS  :",st)


"""    
#B1=number/denum
B0=m2-(B1*m1)

print("value of B1 is   :",B1)
print("value of B0 is   :",B0)

"""




