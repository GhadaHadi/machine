import pandas as pd
import math 
dectionary={'day':[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
             'quitlook':["sunny","sunny","overcast","rain","rain","rain","overcast","sunny","sunny","rain","sunny","overcast","overcast","RAIN"],
             'temp':["hot","hot","hot","mild","cold","cold","cold","maild","cold","maild","maild","maild","hot","maild"],
             'humidity':["high","high","high","high","normal","normal","normal","high","normal","normal","normal","high","normal","high"],
             'wind':["weak","strong","weak","weak","weak","strong","weak","weak","weak","strong","strong","strong","weak","strong"],
             'play tennis':["no","no","yes","yes","yes","no","yes","no","no","yes","no","yes","yes","no"]}
table=pd.DataFrame(dectionary)
print(table)

e=table['play tennis']
print (e)
l=list(table['play tennis'])
print(l)
y=l.count("yes")
n=l.count("no")
print("number of yse is :", y)
print("number of no is  :", n)
#E=-p log p - q log q
p=y/14
q=n/14
e=-(p*math.log2(p))-(q*math.log2(q))
print(e)
