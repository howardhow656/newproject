#3. Which country is the hottest one and which is the coldest one?



#import所需的module
import pandas as pd
import numpy  as np
import warnings
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#關掉警報
warnings.filterwarnings('ignore')




#匯入所需的data
dataGT = pd.read_csv('GlobalTemperatures.csv')
data = pd.read_csv('GlobalLandTemperaturesByCountry.csv')

#把不需要的數據drop掉
dataGT.replace('',np.nan,inplace=True)#把所有空值變成NAN
dataGT.replace('',np.nan,inplace=True)#把所有空值變成NAN
dataGT.drop('LandMaxTemperature', axis=1 , inplace = True)
dataGT.drop('LandMinTemperature', axis=1 , inplace = True)
dataGT.drop('LandMaxTemperatureUncertainty', axis=1 , inplace = True)
dataGT.drop('LandMinTemperatureUncertainty', axis=1 , inplace = True)
dataGT.drop('LandAndOceanAverageTemperature', axis=1 , inplace = True)
dataGT.drop('LandAndOceanAverageTemperatureUncertainty', axis=1 , inplace = True)
data.drop('AverageTemperatureUncertainty', axis=1 , inplace = True)
data.dropna(inplace=True , axis = 0)  



#1. Is there a global warming?
#怎麼證明有全球暖化
#利用溫度差來證明，可以看
dataGT['year'] = pd.to_datetime(dataGT['dt']).dt.year#把dt變成真正的dt以及year


#數那年有幾個數值，如果少於六個就全部刪掉
count = 0
line = 0
for num in dataGT['year']:
    if num == dataGT['year'][line]:
        count += 1
        line += 1
    elif num == np.nan:
        line += 1
        dataGT.drop(dataGT[dataGT['year'] == num].index , inplace= True)
    elif num-1 == dataGT['year'][line]:
        if count <= 8:
            line += 1
            dataGT.drop(dataGT[dataGT['year'] == num-1].index , inplace= True)
            count = 0
            continue
        else:
            line += 1
            count = 0

temp= dataGT.groupby('year')['LandAverageTemperature'].mean()
year = pd.DataFrame(dataGT['year']).drop_duplicates()

plt.figure(figsize = (10,5))
plt.subplot(1,2,1)
plt.title("The temperature ")
plt.ylabel('landaveragetemp')
plt.xlabel('years')                
x = year['year']
y = temp
plt.scatter(x , y , s = 50)
coefficients = np.polyfit(x, y, 3)
p = np.poly1d(coefficients)
r_squared = r2_score(y, p(x))
plt.plot(x, p(x), color='red')
plt.text(0.6, 0.9, 'R-squared = {:.3f}'.format(r_squared), transform=plt.gca().transAxes)
plt.show()




#2. Which period is the fastest temperature growth?
#做法:應該要先定義多長算是一個period，以目前的資料來說可以試試以10年為一個period來進行計算。可以每十年為一單位，然後找出裡面的最高溫及最低溫，相減取平均，但要注意最高溫在前還是在後，應該要注意年分，這樣就有考慮到正負耗了

#設定幾項空
allratelist1 = []
ratelist1 = []
yearlist1 = []
allratelist2 = []
ratelist2 = []
yearlist2 = []
allratelist3 = []
ratelist3 = []
yearlist3 = []
allratelist4 = []
ratelist4 = []
yearlist4 = []
maxratedate1 = None
maxratedate2 = None
maxratedate3 = None
maxratedate4 = None
ratelist = None
yearlist = None
allratelist = None


#透過不同的時間長度來設立period來做資料分析
for time in year['year']:
    t = int(time) + 10
    if t >= 2016:
        break
    range = dataGT.loc[dataGT['year'].between(time, t)]
    maxtemp = range.loc[range['LandAverageTemperature'].idxmax()]
    mintemp = range.loc[range['LandAverageTemperature'].idxmin()]
    if maxtemp['year'] != mintemp['year']:
        rate = round((maxtemp['LandAverageTemperature'] - mintemp['LandAverageTemperature'])/(maxtemp['year'] - mintemp['year']) , 3)
        if rate >= 0:
            ratelist1.append(rate)
            yearlist1.append(time)
    allratelist1.append(rate)
    if rate >= max(allratelist1):
        maxratedate1 = time
 
 #----------------------------------------------------------------------------------------------------
for time in year['year']:
    t = int(time) + 50
    if t >=2016:
        break
    range = dataGT.loc[dataGT['year'].between(time, t)]
    maxtemp = range.loc[range['LandAverageTemperature'].idxmax()]
    mintemp = range.loc[range['LandAverageTemperature'].idxmin()]
    if maxtemp['year'] != mintemp['year']:
        rate = round((maxtemp['LandAverageTemperature'] - mintemp['LandAverageTemperature'])/(maxtemp['year'] - mintemp['year']) , 3)
        if rate >= 0:
            ratelist2.append(rate)
            yearlist2.append(time)
    allratelist2.append(rate)
    if rate >= max(allratelist2):
        maxratedate2 = time 
        
#----------------------------------------------------------------------------------------------------
for time in year['year']:
    t = int(time) + 100
    if t >= 2016:
        break
    range = dataGT.loc[dataGT['year'].between(time, t)]
    maxtemp = range.loc[range['LandAverageTemperature'].idxmax()]
    mintemp = range.loc[range['LandAverageTemperature'].idxmin()]
    if maxtemp['year'] != mintemp['year']:
        rate = round((maxtemp['LandAverageTemperature'] - mintemp['LandAverageTemperature'])/(maxtemp['year'] - mintemp['year']) , 3)
        if rate >= 0:
            ratelist3.append(rate)
            yearlist3.append(time)
    allratelist3.append(rate)
    if rate >= max(allratelist3):
        maxratedate3 = time 

#----------------------------------------------------------------------------------------------------
for time in year['year']:
    t = int(time) + 200
    if t >= 2016:
        break
    range = dataGT.loc[dataGT['year'].between(time, t)]
    maxtemp = range.loc[range['LandAverageTemperature'].idxmax()]
    mintemp = range.loc[range['LandAverageTemperature'].idxmin()]
    if maxtemp['year'] != mintemp['year']:
        rate = round((maxtemp['LandAverageTemperature'] - mintemp['LandAverageTemperature'])/(maxtemp['year'] - mintemp['year']) , 3)
        if rate >= 0:
            ratelist4.append(rate)
            yearlist4.append(time)
    allratelist4.append(rate)
    if rate >= max(allratelist4):
        maxratedate4 = time 

#用資料來畫出散步圖並列出用其period最高的rate
plt.figure(figsize = (20,10))
plt.subplot(2,2,1)
plt.title("The fastest rate in the range of 10 years")
plt.scatter(yearlist1 , ratelist1 , s=50)
plt.text(0.1 , 0.8 , f"Rate: {max(ratelist1)}\nYear: {maxratedate1} ~ {maxratedate1 + 10}", transform=plt.gca().transAxes , fontsize = 8 , color = "blue")

plt.subplot(2,2,2)
plt.title("The fastest rate in the range of 50 years")
plt.scatter(yearlist2 , ratelist2 , s=50)
plt.text(0.1 , 0.8 , f"Rate :{max(ratelist2)}\nYears:{maxratedate2}~{maxratedate2 + 10}", transform=plt.gca().transAxes , fontsize = 8 , color = "blue")
plt.subplot(2,2,3)
plt.title("The fastest rate in the range of 100 years")
plt.scatter(yearlist3 , ratelist3 , s=50)
plt.text(0.1 , 0.8 , f"Rate :{max(ratelist3)}\nYears:{maxratedate3}~{maxratedate3 + 10}", transform=plt.gca().transAxes , fontsize = 8 , color = "blue")

plt.subplot(2,2,4)
plt.title("The fastest rate in the range of 200 years")
plt.scatter(yearlist4 , ratelist4 , s=50)
plt.text(0.8 , 0.8 , f"Rate :{max(ratelist4)}\nYears:{maxratedate4}~{maxratedate4 + 10}", transform=plt.gca().transAxes , fontsize = 8 , color = "blue")

plt.show()


#3. Which country is the hottest one and which is the coldest one?
#依照國家來分組並算出均溫
result= data.groupby('Country')['AverageTemperature'].mean()
top3 = result.sort_values(ascending= False).head(3)
wst3 = result.sort_values(ascending=True).head(3)
country1 = result.loc[top3.index]
country2 = result.loc[wst3.index]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("The top three hottest countries.")
plt.bar(np.arange(len(country1)), top3.values , width= 0.5)
plt.xticks(np.arange(len(country1)), country1.index)
plt.ylabel('Temperature')

plt.subplot(1,2,2)
plt.title("The top three coldest countries.")
plt.bar(np.arange(len(country2)), wst3.values , width= 0.5)
plt.xticks(np.arange(len(country2)), country2.index)
plt.ylabel('Temperature')

plt.show()
