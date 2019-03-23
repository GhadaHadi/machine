import pandas as pd
import matplotlib.pyplot as py
from matplotlib import style
daily_staus={'day':['monday','sunday','tuesday'],
             'sleeping':[12,6,2],
             'working':[50,60,70],
             'excresize':[6,8,12]
            }
print(style.available)
ds=pd.DataFrame(daily_staus)
style.use('Solarize_Light2')
ds['excresize'].plot()
py.show()

#l=['ddd','fff','ggg']
#print(daily_staus)
#print("************************")
#print(ds)