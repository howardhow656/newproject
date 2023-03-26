#import所需的module


#3. Which country is the hottest one and which is the coldest one?
import pandas as pd
import numpy  as np
import warnings
import matplotlib.pyplot as plt


#關掉警報
warnings.filterwarnings('ignore')


#1. Is there a global warming?
#怎麼證明有全球暖化
#利用溫度差來證明，可以看
#匯入data
dataGT = pd.read_csv('GlobalTemperatures.csv')

#把不需要的數據drop掉
dataGT.replace('',np.nan,inplace=True)#把所有空值變成NAN
dataGT.replace('',np.nan,inplace=True)#把所有空值變成NAN
dataGT.drop('LandMaxTemperature', axis=1 , inplace = True)
dataGT.drop('LandMinTemperature', axis=1 , inplace = True)
dataGT.drop('LandMaxTemperatureUncertainty', axis=1 , inplace = True)
dataGT.drop('LandMinTemperatureUncertainty', axis=1 , inplace = True)
dataGT.drop('LandAndOceanAverageTemperature', axis=1 , inplace = True)
dataGT.drop('LandAndOceanAverageTemperatureUncertainty', axis=1 , inplace = True)



#為了減少uncertainty的誤差，所以如果uncertainty超過某個數值，就讓溫度扣掉那個數值的一半
uncertainty3 = round(dataGT['LandAverageTemperatureUncertainty']) 
for unc in uncertainty3:
    if unc > 3:
        dataGT.loc[unc]['LandAverageTemperature'] -= round(dataGT['LandAverageTemperatureUncertainty']*0.5 , 5)
        
        
#把nan值的行數drop掉，另外如果有年份所擁有的資料少於6個月就全部刪掉
line = 0
count = 0
for num in dataGT['year']:
    if num == dataGT['year'][line]:
        count += 1
        line += 1
    elif num == np.nan:
        line += 1
        dataGT.drop(dataGT[dataGT['year'] == num].index , inplace= True)
    elif num-1 == dataGT['year'][line]:
        if count <= 6:
            line += 1
            dataGT.drop(dataGT[dataGT['year'] == num-1].index , inplace= True)
            count = 0
            continue
        else:
            line += 1
            count = 0

        
#把每年的溫度取平均   

dataGT['year'] = pd.to_datetime(dataGT['dt']).dt.year#把dt變成真正的dt以及year        
result= dataGT.groupby('year')['LandAverageTemperature'].mean()
year = pd.DataFrame(dataGT['year']).drop_duplicates()

#畫圖表
plt.figure(figsize = (50,5))
plt.subplot(1,1,1)
plt.title("the change of the temp")
plt.ylabel('landaveragetemp')
plt.xlabel('years')                
x = year
y = result
plt.plot(x , y , 'b-' , label = 'land average temperature')
plt.legend(loc='best')
plt.show()
#問題:有的年份nan太多，但是還沒找到方法把那些拿掉:主要的問題程式在test2
#有可能跟我把空值全部變成nan值然後嘗試直接drop掉有關，但目前不確定有沒有drop成功，如果沒有成功那應該就是那裡出了問題。



#2. Which period is the fastest temperature growth?




